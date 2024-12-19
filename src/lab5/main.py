from src.lab5.orderprocessor import OrderProcessor

def main() -> None:
    processor = OrderProcessor(input_file='txtfiles/orders.txt')
    processor.process(non_valid_orders_file='txtfiles/non_valid_orders.txt',
                      valid_orders_file='txtfiles/order_country.txt')


if __name__ == "__main__":
    main()