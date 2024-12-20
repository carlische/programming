import re
from typing import List, Tuple

class Order:
    def __init__(self, order_data: List[str]):
        """
        Инициализирует объект заказа на основе списка атрибутов.
        """
        self.order_number = order_data[0]
        self.products = order_data[1]
        self.customer_name = order_data[2]
        self.address = order_data[3]
        self.phone_number = order_data[4]
        self.priority = order_data[5]

        self.errors: List[Tuple[str, str]] = []  # Список ошибок для данного заказа

    def validate(self) -> None:
        """
        Проверяет заказ на соответствие правилам и заполняет список ошибок.
        """
        if not self.address or len(self.address.strip().split('. ')) != 4:
            error_value = self.address if self.address else "no data"
            self.errors.append(('1', error_value))

        if not self.phone_number:
            self.errors.append(('2', "no data"))
        else:
            pattern = r'^\+\d-\d{3}-\d{3}-\d{2}-\d{2}$'
            if not re.match(pattern, self.phone_number):
                self.errors.append(('2', self.phone_number))

    def is_valid(self) -> bool:
        """
        Проверяет, является ли заказ валидным.
        """
        return len(self.errors) == 0

    def format_products(self) -> str:
        """
        Форматирует строку с продуктами.
        """
        product_list = [p.strip() for p in self.products.split(',')]
        product_count = {}
        for product in product_list:
            product_count[product] = product_count.get(product, 0) + 1

        formatted_products = []
        for product, count in product_count.items():
            if count > 1:
                formatted_products.append(f"{product} x{count}")
            else:
                formatted_products.append(product)
        return ', '.join(formatted_products)

    def format_address(self) -> str:
        """
        Форматирует строку с адресом.
        """
        address_parts = self.address.split('. ')
        return '. '.join(address_parts[1:]) if len(address_parts) > 1 else self.address

    def get_country(self) -> str:
        """
        Извлекает страну из адреса.
        """
        address_parts = self.address.split('. ')
        return address_parts[0] if address_parts else ''

    def get_priority_value(self) -> int:
        """
        Возвращает числовое значение приоритета для сортировки.
        """
        priority_mapping = {'MAX': 1, 'MIDDLE': 2, 'LOW': 3}
        return priority_mapping.get(self.priority, 4)