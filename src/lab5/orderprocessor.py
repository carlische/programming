from typing import List, Tuple, Optional
from src.lab5.order import Order

class OrderProcessor:
    def __init__(self, orders_data: Optional[List[List[str]]] = None, input_file: Optional[str] = None):
        """
        Инициализирует объект для обработки заказов.
        """
        self.orders: List[Order] = []
        self.errors: List[Tuple[str, str, str]] = []

        if orders_data:
            self.orders = [Order(order_data) for order_data in orders_data]
        elif input_file:
            self.read_orders_from_file(input_file)
        else:
            raise ValueError("Необходимо предоставить либо orders_data, либо input_file")

    def read_orders_from_file(self, input_file: str) -> None:
        """
        Читает заказы из файла и создает объекты Order.
        """
        with open(input_file, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():
                    order_data = line.strip().split(';')
                    order = Order(order_data)
                    self.orders.append(order)

    def validate_orders(self) -> None:
        """
        Проверяет все заказы и собирает ошибки.
        """
        for order in self.orders:
            order.validate()
            if not order.is_valid():
                for error_type, error_value in order.errors:
                    self.errors.append((order.order_number, error_type, error_value))

    def write_non_valid_orders(self, file_path: str) -> None:
        """
        Записывает невалидные заказы в файл.
        """
        with open(file_path, 'w', encoding='utf-8') as file:
            for error in self.errors:
                file.write(f"{error[0]};{error[1]};{error[2]}\n")

    def get_valid_orders(self) -> List[Order]:
        """
        Возвращает список валидных заказов.
        """
        return [order for order in self.orders if order.is_valid()]

    def sort_orders(self, orders: List[Order]) -> List[Order]:
        """
        Сортирует заказы по стране и приоритету доставки.
        """
        return sorted(orders, key=lambda o: (o.get_country(), o.get_priority_value()))

    def write_valid_orders(self, orders: List[Order], file_path: str) -> None:
        """
        Записывает валидные заказы в файл после форматирования.
        """
        with open(file_path, 'w', encoding='utf-8') as file:
            for order in orders:
                formatted_products = order.format_products()
                formatted_address = order.format_address()
                file.write(f"{order.order_number};{formatted_products};{order.customer_name};"
                           f"{formatted_address};{order.phone_number};{order.priority}\n")

    def process(self, non_valid_orders_file: Optional[str] = None, valid_orders_file: Optional[str] = None) -> None:
        """
        Выполняет полный цикл обработки заказов.
        """
        self.validate_orders()
        if non_valid_orders_file:
            self.write_non_valid_orders(non_valid_orders_file)
        valid_orders = self.get_valid_orders()
        sorted_orders = self.sort_orders(valid_orders)
        if valid_orders_file:
            self.write_valid_orders(sorted_orders, valid_orders_file)