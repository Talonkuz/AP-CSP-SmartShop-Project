# SmartShop — FULL STUDENT PROJECT REQUIREMENTS

**Course:** AP Computer Science Principles — Python | **Difficulty:** Beginner–Intermediate  
**Project:** SmartShop — Intelligent Shopping System | **Time:** 6–8 lessons (recommended: 8 × 40 minutes)  
**Work mode:** Individual | **Total:** 100 points | **Output:** Console application (no GUI required)

## 1. The project goal

Imagine a company hires you to build a small online shop. Your Python program must let a buyer browse and find products, choose quantities, manage a cart, get discounts and delivery, see products suitable for their budget, complete a simulated purchase and view purchase history.

**Do not copy a completed program.** Use the starter file, the examples, your notes and teacher feedback to implement the missing parts yourself. You must understand and explain your code.

## 2. Required main menu

```text
====================================
       SMARTSHOP ONLINE STORE
====================================
1. Show products
2. Search products
3. Add product to cart
4. Remove product from cart
5. Show shopping cart
6. Recommend products
7. Checkout
8. Purchase history
0. Exit
Select an option:
```

The menu repeats until `0` is selected. Invalid choices show an error and return to the menu. Functions perform actions; don't put all logic in one large loop.

## 3. Required data model

Create **at least 10 distinct products across at least 3 categories**.

```python
products = [
    {"id": 1, "name": "Laptop", "price": 250000, "stock": 5, "category": "Electronics"},
    {"id": 2, "name": "Headphones", "price": 15000, "stock": 12, "category": "Electronics"},
]
cart = [{"product_id": 2, "quantity": 2}]
history = []
```

Each product needs a unique positive integer `id`; non-empty `name`/`category`; positive integer `price` in KZT; non-negative integer `stock`. Each cart item refers to one existing product and stores a positive integer quantity. There must be **at most one cart entry per product ID**.

## 4. Mandatory Python skills

`print`, `input`, `int`, `float`, `if/elif/else`, `for`, `while`, `break`, `continue`, lists, dictionaries, `append`, `remove`, `len`, `def`, `return`, `and`, `or`, `not`, `.lower()`, `.strip()`, `try/except ValueError`, `round`, f-strings, comparison and arithmetic operators. Some commands need not appear artificially; use them where appropriate.

See [examples/COMMANDS.md](examples/COMMANDS.md).

## 5. Stage 1 — product catalog

Create `products` as a **list of dictionaries**. One product:
```python
{"id": 1, "name": "Laptop", "price": 250000, "stock": 5, "category": "Electronics"}
```

`product["name"]` gets its name; `product["price"]` gets its price. Print the catalog to verify the structure. Do not use negative prices or stocks.

## 6. Stage 2 — main menu

Use `while True`, `input()`, `if/elif/else`, and `break`. Each choice must call the matching function. An invalid choice must not crash or exit.

## 7. Stage 3 — showing products

Create `show_products(products)`. Display **ID, name, price in KZT, stock and category** for all products using a `for` loop. When stock is `0`, display **OUT OF STOCK**.

```python
def show_products(products):
    for product in products:
        print(f"ID: {product['id']}")
        print(f"Name: {product['name']}")
        print(f"Price: {product['price']} KZT")
        print(f"Stock: {product['stock']}")
        if product["stock"] == 0:
            print("OUT OF STOCK")
```

## 8. Stage 4 — search

Implement `search_products(products, keyword)` and return a list of matches. User may search using a **partial product name or category**. Search must ignore letter case and leading/trailing spaces.

Hint:
```python
keyword = keyword.strip().lower()
# If keyword is empty, return [] and ask for a search term in the user interface.
# Compare against product["name"].lower() and product["category"].lower().
```

If no matches exist, display **No products found**.

## 9. Stage 5 — adding to cart

Implement `find_product(products, product_id)` (returns the matching dictionary or `None`). Implement `add_to_cart(products, cart, product_id, quantity)`.

Rules:
1. Product ID must exist and quantity must be a **positive integer** (reject booleans as numbers if doing advanced validation).
2. Existing cart quantity **plus requested quantity** cannot exceed `product["stock"]`.
3. If product is already in cart, **increase its quantity**, do not duplicate the row.
4. If validation fails, **do not change the cart**.
5. **Do not decrease stock when adding to the cart**. Only a successful checkout changes stock.

Example: stock 5, already in cart 3, user tries to add 4 → reject (total 7 > 5).

## 10. Stage 6 — removing from cart

Implement `remove_from_cart(cart, product_id, quantity)`.

Check the entry exists and quantity is a positive integer not exceeding the currently carted quantity. Decrease by that quantity. If remaining quantity reaches `0`, remove the entry with `cart.remove(item)`. Never change stock during cart removal.

## 11. Stage 7 — cart and totals

Implement `show_cart(products, cart)` and `calculate_total(products, cart)`.

For each item, show **name × quantity = line subtotal**. Total is:

```text
total = sum(price_of_product * quantity_in_cart)
```

Example: 2 × 15 000 + 1 × 12 000 + 1 × 8 000 = **50 000 KZT**.

The cart's total must reflect current quantities; an empty cart totals 0.

## 12. Stage 8 — automatic discounts and promo

Implement `calculate_discount(total)` returning an **integer percentage**:

| Cart subtotal BEFORE discount | Discount |
|---:|---:|
| < 20 000 | 0% |
| 20 000–49 999 | 5% |
| 50 000–99 999 | 10% |
| ≥ 100 000 | 15% |

Optional promo input `STUDENT10` gives 10% (ignore surrounding spaces and capitalization). **Do not stack discounts**. Apply the higher of the automatic percentage and promo percentage.

```python
discount_percent = max(auto_discount, promo_discount)
discount_amount = total * discount_percent / 100
total_after_discount = total - discount_amount
```

## 13. Stage 9 — delivery

Implement `calculate_delivery(total)` using the **original cart subtotal before discount**:

| Subtotal | Delivery |
|---:|---:|
| Empty cart (=0) | 0 KZT |
| 1 to 29 999 | 1 500 KZT |
| ≥ 30 000 | 0 KZT |

`final_total = total - discount_amount + delivery`.

## 14. Stage 10 — recommendation algorithm

Implement `recommend_products(products, budget, category)`: return a new list with products where:
- `price <= budget`;
- `stock > 0`;
- `category` equals selected category (case-insensitive).

Sort the list by `price` **ascending**, e.g.:
```python
recommendations.sort(key=lambda product: product["price"])
```

If nothing matches, print **No suitable products found**.

**Important:** The recommender compares the **price of each one unit** with the requested budget. It does **not** solve a full cart optimization problem. This is a **rule-based system, not machine learning**.

## 15. Stage 11 — checkout / simulated payment

Implement `checkout(products, cart, history)`. Prompt for customer name (non-empty), customer budget (non-negative), and optional promo code. Follow this precise sequence:

1. Reject an empty cart.
2. Re-check every product ID, quantities and stock immediately before checkout.
3. Calculate subtotal, highest applicable discount percentage, discount amount, delivery and final total.
4. Check that `budget >= final_total`. If not, print the missing amount; keep stock/cart/history unchanged.
5. Display order summary, ask for `yes/no` confirmation.
6. If the user cancels, keep stock/cart/history unchanged.
7. Only on successful confirmation, subtract each purchased quantity from stock; make an order record; append it to history; clear the cart.

All transactions are simulations. No real payment information must be collected.

## 16. Stage 12 — electronic receipt

After a completed purchase, print:
- Unique order number (e.g. 1001, 1002...), current date, non-empty customer name;
- Product names, unit prices, quantities and line subtotals;
- Subtotal, chosen discount %, discount amount, delivery, final total;
- User's original budget, remaining budget (= budget - final total);
- **PAYMENT SUCCESSFUL**.

Use `from datetime import datetime` and `datetime.now()`, f-strings and `round()` for a clear display.

Example:
```text
SMARTSHOP — ORDER #1001
Customer: Alex
Headphones × 2: 30 000 KZT
Keyboard × 1: 12 000 KZT
Mouse × 1: 8 000 KZT
Subtotal: 50 000 KZT
Discount 10%: -5 000 KZT
Delivery: 0 KZT
TOTAL: 45 000 KZT
Budget: 60 000 KZT
Remaining: 15 000 KZT
PAYMENT SUCCESSFUL
```

## 17. Stage 13 — history and statistics

Each order record must include `order_id`, `customer`, `date`, `items` (snapshot of purchased product names, unit prices and quantities), `subtotal`, `discount` (amount), `delivery`, `total`, `status="Completed"`.

Implement `show_history(history)`: display past orders, number of completed purchases, sum of final totals (sales) and sum of discount amounts. Show **No purchases yet** for empty history.

## 18. Stage 14 — invalid input

Never crash on user mistakes. Use `try/except ValueError` around number conversion and explicit range checks. Reject unknown IDs, zero/negative quantities, insufficient stock, empty customer name, negative budget, malformed choices. Re-prompt when suitable.

## 19. Required function names and signatures

```python
show_products(products)
find_product(products, product_id)
search_products(products, keyword)
add_to_cart(products, cart, product_id, quantity)
remove_from_cart(cart, product_id, quantity)
show_cart(products, cart)
calculate_total(products, cart)
calculate_discount(total)
calculate_delivery(total)
recommend_products(products, budget, category)
checkout(products, cart, history)
show_history(history)
main()
```

You may add helpers such as `read_positive_int(prompt)` and `read_budget(prompt)`. Put the menu inside `main()` and call it under `if __name__ == "__main__":`.

## 20. AP CSP concepts to demonstrate

| Concept | Where to show it |
|---|---|
| Input / Output | Menu, prompts, receipts |
| Data abstraction | Product list, cart, history |
| Procedural abstraction | Named functions and parameters |
| Sequencing | Checkout's ordered steps |
| Selection | Validation, discounts, recommendations |
| Iteration | Catalog search, totals and main menu |
| Testing | Positive, boundary and invalid scenarios |

This is a classroom practice assignment. Official AP Create requirements and independent-work rules must be checked separately.

## 21. Required test report

Test **at least 15 cases** (see [TESTING.md](TESTING.md)). For each test record input, expected outcome, actual outcome, pass/fail and a screenshot or short note if helpful.

## 22. Final submission

1. `smartshop.py` — fully working Python source file.
2. `DOCUMENTATION.md` or PDF — purpose, users, data model, algorithms and one self-made improvement.
3. Test report with **15+ tests**.
4. Screen recording of **1–2 minutes** demonstrating catalog, cart, recommendation and successful checkout.
5. Oral defense: explain functions, parameters, lists, conditionals, loops, `return` and one bug you fixed.

## 23. Timing

Recommended eight lessons: catalog/menu; search; cart; pricing; recommendations; checkout/history; validation/testing; extension/defense. See [LESSON_PLAN.md](LESSON_PLAN.md).

## 24. Grading

100 points in ten categories, plus optional bonus capped at 100. See [GRADING.md](GRADING.md).

## 25. Extensions

Possible enhancements: JSON persistence; admin panel; inventory editing; random promo codes; bestseller statistics; tkinter GUI; sales charts; budget-basket optimization. See [ADVANCED.md](ADVANCED.md).

## 26. Defense

Be ready to answer what problem the system solves, how a list differs from a dictionary, why the menu uses a loop, how `append()` differs from `remove()`, why `return` differs from `print()`, when stock should be reduced, how the recommendation works, and why invalid input must be handled. [All questions](DEFENSE.md).

## 27. Academic honesty

Write your own missing functions. Do not submit someone else's completed project. You must be able to modify any part of your program during the defense. Credit outside examples or sources used.

## 28. Definition of done

A student is done when **all nine menu options**, all required functions, 10+ products in 3+ categories, correct cart inventory rules, search, discounts, promo, delivery, recommendation, checkout, receipt, history, error handling, tests, documentation and oral explanation are completed.
