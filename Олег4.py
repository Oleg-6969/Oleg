store = {
    'bread': 25.5,
    'butter': 72.9,
    'eggs': 54,
    'sugar': 39.5,
    'salt': 17.25,
    'coffee': 210,
    'tea': 145.75,
    'chocolate': 89.9,
    'pasta': 48,
    'oil': 92.4
}


def format_price(price):
    return f"price: {price:.2f} UAH"


def check(products):
    result = {}
    for product in products:
        result[product] = product in store
    return result


def order(products):
    availability = check(products)

    if all(availability.values()):
        total = 0
        for product in products:
            total += store[product]
        return f"Усі товари є! Загальна {format_price(total)}"
    else:
        miss = [product for product, available in availability.items()
                if not available]
        return f"Немає в наявності: {' '.join(miss)}"


def main():
    while True:
        print("1 - Переглянути ціну\n2 - Купити")
        choice = input("Your choice: ")

        user_input = input("Введи товари через пробіл: ")
        products = user_input.split()

        if choice == "1":
            availability = check(products)
            for product, is_available in availability.items():
                if is_available:
                    print(f"{product} – {format_price(store[product])}")
                else:
                    print(f"{product} – нема в наявності")

        elif choice == "2":
            print(order(products))
        else:
            print("Невірний вибір, спробуй ще раз.")


if __name__ == "__main__":
    main()
