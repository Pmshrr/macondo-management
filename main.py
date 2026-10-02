import sales
def get_command() -> int:
    while True:
        print("1. Add order")
        print("2. Show orders")
        print("3. Remove orders")
        print("4. Checkout")
        print("0. Exit")
        try:
            command = int(input("Choose: "))
            if command in (0, 1, 2, 3, 4):
                return command
            print("invalid command")
        except ValueError:
            print("Please enter a valid number")

def select_drink() -> dict:
    while True:
        item = input("Enter drink name: ").lower()
        result = sales.find_drink(item)
        if result is not None:
            return result
        print("Invalid drink name")
def show_orders() -> None:
    orders = sales.load_orders()
    if not orders:
        print("No orders yet")
        return
    for i, order in enumerate(orders, start=1):
        print(f"{i}. {order['drink']} : {order['price']}")
def main() -> None:
    while True:
        command = get_command()
        if command == 1:
            item = select_drink()
            sales.add_order(item)
        elif command == 2:
            show_orders()
        elif command == 3:
            remove_order_ui()
        elif command == 4:
            clear_orders_ui()
        elif command == 0:
            break
def get_order_number() -> int:
    while True:
        try:
            order_number = int(input("Enter order number: "))
            if order_number > 0:
                return order_number
            print("Invalid order number")
        except ValueError:
            print("Please enter a valid number")
def remove_order_ui() -> None:
    show_orders()
    number = get_order_number()
    success = sales.remove_order(number)
    if success:
        print("Order removed")
    else:
        print("Order does not exist")
def clear_orders_ui() -> None:
    orders = sales.load_orders()
    if not orders:
        print("No orders to clear")
        return
    total = sum(order['price'] for order in orders)
    print(f"Total: {total}")
    sales.clear_orders()
    print("Orders cleared")
if __name__ == "__main__":
    main()