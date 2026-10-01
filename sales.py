import json
import os
menu = [
    {"drink": "latte", "price": 200000},
    {"drink": "espresso", "price": 140000},
    {"drink": "americano", "price": 150000}
]
def load_orders() -> list:
    if os.path.exists("orders.json"):
        try:
            with open("orders.json", "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    else:
        with open("orders.json", "w") as file:
            json.dump([], file)
        return []
def save_orders(orders: list) -> None:
    with open("orders.json", "w") as file:
        json.dump(orders, file)
def add_order(order: dict) -> None:
    orders = load_orders()
    orders.append(order)
    save_orders(orders)
def find_drink(drink: str) -> dict | None:
    for item in menu:
        if item["drink"] == drink:
            return item
    return None
