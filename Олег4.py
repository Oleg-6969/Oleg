def format_price(price: float) -> str:
    return f"ціна: {price:.2f} грн"

def check_availability(*products) -> dict:
    store = {
        "хліб": True,
        "молоко": True,
        "масло": False,
        "сир": True,
        "яблука": True,
        "цукор": False
    }
    return {product: store.get(product, False) for product in products}

def process_order(order: list, action: str):
    prices = {
        "хліб": 25.5,
        "молоко": 32.0,
        "масло": 70.75,
        "сир": 120.0,
        "яблука": 45.25,
        "цукор": 30.0
    }
    availability = check_availability(*order)
    if not all(availability.values()):
        print("Деякі товари відсутні в магазині:")
        for product, available in availability.items():
            if not available:
                print(f"- {product} (немає)")
        return
    total = sum(prices[product] for product in order)
    if action == "переглянути":
        print("Ваше замовлення:")
        for product in order:
            print(f"{product} - {format_price(prices[product])}")
        print(f"Загальна {format_price(total)}")
    elif action == "купити":
        print("Замовлення успішно оформлено!")
        print(f"До сплати: {format_price(total)}")

while True:
    choice = input("\nОберіть дію (купити / переглянути / вихід): ").lower()
    if choice == "вихід":
        break
    items = input("Введіть товари через кому: ").lower().split(",")
    items = [item.strip() for item in items if item.strip()]
    process_order(items, choice)
