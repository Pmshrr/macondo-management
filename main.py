import sales
def get_command():
    while True:
        print("1. Add order")
        print("2. Show orders")
        print("0. Exit")
        try:
            command = int(input("Choose: "))
            if command in (0, 1, 2):
                return command
            print("invalid command")
        except ValueError:
            print("Please enter a valid number")

def select_drink():
    while True:
        item = input("Enter drink name: ").lower()
        result = sales.find_drink(item)
        if result is not None:
            return result
        print("Invalid drink name")
def show_orders():
    orders = sales.load_orders()
    if not orders:
        print("No orders yet")
        return
    for order in orders:
        print(f"{order['drink']} : {order['price']}")
def main():
    while True:
        command = get_command()
        if command == 1:
            item = select_drink()
            sales.add_order(item)
        elif command == 2:
            show_orders()
        elif command == 0:
            break
if __name__ == "__main__":
    main()