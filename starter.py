"""SmartShop student starter — fill in the TODOs, don't submit unfinished placeholders."""
from datetime import datetime

products = [
    {"id": 1, "name": "Laptop", "price": 250000, "stock": 5, "category": "Electronics"},
    {"id": 2, "name": "Headphones", "price": 15000, "stock": 12, "category": "Electronics"},
    {"id": 3, "name": "Keyboard", "price": 12000, "stock": 8, "category": "Accessories"},
    {"id": 4, "name": "Mouse", "price": 8000, "stock": 15, "category": "Accessories"},
    {"id": 5, "name": "Backpack", "price": 20000, "stock": 7, "category": "Education"},
    {"id": 6, "name": "Notebook", "price": 2500, "stock": 30, "category": "Education"},
    # TODO: Add at least four more distinct products.
]
cart = []
history = []


def show_products(products):
    # TODO: Use a loop. Print ID, name, price, category, stock, OUT OF STOCK when 0.
    pass


def find_product(products, product_id):
    # TODO: Return matching product dictionary by ID; otherwise return None.
    pass


def search_products(products, keyword):
    # TODO: Case-insensitive partial match of product name or category.
    # Return list of matched product dictionaries. Empty keyword -> [].
    return []


def add_to_cart(products, cart, product_id, quantity):
    # TODO: Check ID, positive quantity, stock including quantity already in cart.
    # Existing entry: increase quantity; otherwise append {"product_id": ..., "quantity": ...}.
    # Do NOT change stock yet.
    pass


def remove_from_cart(cart, product_id, quantity):
    # TODO: Validate quantities. Decrease or remove row when quantity reaches zero.
    pass


def show_cart(products, cart):
    # TODO: Show item names, quantities, line subtotals, total.
    pass


def calculate_total(products, cart):
    # TODO: Sum price * quantity for each cart entry.
    return 0


def calculate_discount(total):
    # TODO: Return integer discount percentage: 0 / 5 / 10 / 15.
    return 0


def calculate_delivery(total):
    # TODO: Original subtotal 0 -> 0; below 30000 -> 1500; else 0.
    return 0


def recommend_products(products, budget, category):
    # TODO: Stock > 0, price <= budget, category equals ignoring case.
    # Sort ascending price; return recommendation list.
    return []


def checkout(products, cart, history):
    # TODO:
    # 1. Reject empty cart and revalidate stock.
    # 2. Ask customer name, budget, promo.
    # 3. Subtotal, automatic discount, promo STUDENT10, max rate, delivery, final total.
    # 4. Reject insufficient budget; request yes/no confirmation.
    # 5. On success ONLY: reduce stock, snapshot ordered items, append history, clear cart.
    # 6. Print receipt with unique order ID, datetime, itemized amounts, and remaining budget.
    pass


def show_history(history):
    # TODO: Print orders, number of orders, total sales and discounts.
    pass


def main():
    while True:
        print("\n===== SMARTSHOP ONLINE STORE =====")
        print("1. Show products")
        print("2. Search products")
        print("3. Add product to cart")
        print("4. Remove product from cart")
        print("5. Show shopping cart")
        print("6. Recommend products")
        print("7. Checkout")
        print("8. Purchase history")
        print("0. Exit")

        choice = input("Select an option: ").strip()
        if choice == "1":
            show_products(products)
        elif choice == "2":
            keyword = input("Search by name/category: ")
            # TODO: Call search_products and show the results.
        elif choice == "3":
            # TODO: Ask for product ID/quantity safely and call add_to_cart.
            print("TODO: add product")
        elif choice == "4":
            # TODO: Ask for product ID/quantity safely and call remove_from_cart.
            print("TODO: remove product")
        elif choice == "5":
            show_cart(products, cart)
        elif choice == "6":
            # TODO: Ask budget/category; call recommend_products and print results.
            print("TODO: recommendations")
        elif choice == "7":
            checkout(products, cart, history)
        elif choice == "8":
            show_history(history)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
