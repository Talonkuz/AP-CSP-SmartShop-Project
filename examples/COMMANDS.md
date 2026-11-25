# Python commands for SmartShop — beginner handbook

| Syntax | Simple meaning | SmartShop use |
|---|---|---|
| `print("Hello")` | Show a message | Menu, receipt |
| `input("Name: ")` | Ask a user | Search, checkout |
| `int("5")` | Convert text to integer | Quantity |
| `float("5.5")` | Convert to decimal | Budget if desired |
| `if / elif / else` | Choose a branch | Discounts and validation |
| `for x in items` | Visit each element | Search and totals |
| `while True` | Repeat | Menu |
| `break` | Leave loop | Exit |
| `continue` | Skip to next iteration | Recover from bad input |
| `[]` | List | Products/cart/history |
| `{"name": "Mouse"}` | Dictionary | One product |
| `items.append(x)` | Add element | New cart row |
| `items.remove(x)` | Remove matching element | Delete cart row |
| `len(items)` | Number of elements | Empty cart check |
| `def f(x):` | Define function | Store actions |
| `return x` | Send result back to caller | Total/search |
| `and, or, not` | Combine conditions | Filters |
| `.lower()` | Lowercase text | Case-insensitive search |
| `.strip()` | Remove leading/trailing spaces | Validate name/promo |
| `try/except ValueError` | Catch wrong number input | Menu or quantity |
| `round(x,2)` | Round a number for display | Money output |
| `f"{x}"` | Insert value into string | Receipt |

## 1. Dictionary + list

```python
products = [
    {"id": 1, "name": "Mouse", "price": 8000, "stock": 4, "category": "Accessories"},
    {"id": 2, "name": "Keyboard", "price": 12000, "stock": 3, "category": "Accessories"},
]
print(products[0]["name"])   # Mouse
for product in products:
    print(product["name"], product["price"])
```

**Difference:** `products[0]` means the **first product in the list**; `product["name"]` means the **name field inside one dictionary**.

## 2. Searching text

```python
keyword = input("Search: ").strip().lower()
for product in products:
    if keyword in product["name"].lower():
        print("Found:", product["name"])
```

Try `mou` to find `Mouse`. Check empty search separately.

## 3. Totals

```python
prices = [8000, 12000]
total = 0
for price in prices:
    total = total + price
print(total)   # 20000
```

## 4. Conditions

```python
quantity = 3
stock = 2
if quantity <= 0:
    print("Quantity must be positive")
elif quantity > stock:
    print("Not enough stock")
else:
    print("Can add")
```

## 5. Functions with parameters and return

```python
def line_total(price, quantity):
    return price * quantity

answer = line_total(15000, 2)
print(answer)  # 30000
```

`return` gives a result to the caller; `print` only displays it.

## 6. Error handling

```python
while True:
    try:
        quantity = int(input("Quantity: "))
    except ValueError:
        print("Enter a whole number.")
        continue
    if quantity <= 0:
        print("Quantity must be > 0")
        continue
    break
```

## 7. Sorting recommendations

```python
items = [{"name": "Mouse", "price": 8000}, {"name": "Notebook", "price": 2500}]
items.sort(key=lambda product: product["price"])
print([item["name"] for item in items])  # ['Notebook', 'Mouse']
```

## 8. Demo of `max` for discounts

```python
auto_discount = 15
promo_discount = 10
chosen = max(auto_discount, promo_discount)
print(chosen)  # 15; do NOT add them
```

## 9. IDs and quantities

`stock` = actual products in the shop. `quantity` in cart = items requested but **not yet purchased**. For a new request, check `already_carted + requested <= stock`.

## 10. Helpful study sequence

Understand the data first → display it → search it → add/remove cart lines → compute totals → discounts/delivery → recommend → checkout → test.

These examples teach the commands but do **not** constitute a completed SmartShop solution.
