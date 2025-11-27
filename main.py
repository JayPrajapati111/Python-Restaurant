menu = {
    'pizza': 60,
    'Pasta': 40,
    'Burger': 60,
    'Healthysalad': 70,
    'coffee': 80,
}

print("Welcome to Python Restaurant.")
print("pizza: 60 Rs\npasta: 40 Rs\nBurger: 60 Rs\nHealthysalad: 70 Rs\ncoffee: 80 Rs")

order_total = 0

while True:
    item = input("Enter the item you want to order: ").lower()
    if item in menu:
        order_total += menu[item]
        print(f"Your item {item} has been added to your order")
    else:
        print("Sorry, we don't have that item on the menu")

    another_order = input("Do you want to add another item? (yes/no): ").lower()
    if another_order != 'yes':
        break

print(f"The total amount to pay is {order_total} Rs")