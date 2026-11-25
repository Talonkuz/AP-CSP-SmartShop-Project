"""Example product catalog for classroom exercises. Edit and extend it."""
products = [
    {"id": 1, "name": "Laptop", "price": 250000, "stock": 5, "category": "Electronics"},
    {"id": 2, "name": "Headphones", "price": 15000, "stock": 12, "category": "Electronics"},
    {"id": 3, "name": "Keyboard", "price": 12000, "stock": 8, "category": "Accessories"},
    {"id": 4, "name": "Mouse", "price": 8000, "stock": 15, "category": "Accessories"},
    {"id": 5, "name": "Backpack", "price": 20000, "stock": 7, "category": "Education"},
    {"id": 6, "name": "Notebook", "price": 2500, "stock": 30, "category": "Education"},
]
if __name__ == "__main__":
    for item in products:
        print(f"{item['id']}. {item['name']}: {item['price']} KZT ({item['stock']} left)")
