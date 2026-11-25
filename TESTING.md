# Testing report — SmartShop

**Instructions:** For every case write *inputs*, *expected result*, *actual result*, *Pass/Fail*. Run at least **15 different cases**. Do not merely write "works".

| # | Test input / action | Expected result |
|---:|---|---|
| 1 | Select Show products | All products with stock and prices |
| 2 | Search `head` | Finds Headphones |
| 3 | Search ` HEAD ` | Same result; case and spaces ignored |
| 4 | Search nonsense keyword | No products found |
| 5 | Add 1 Mouse | Cart contains Mouse × 1 |
| 6 | Add 2 more Mouse | One line Mouse × 3 |
| 7 | Add more than stock | Reject, cart unchanged |
| 8 | Add quantity -2 or 0 | Reject, cart unchanged |
| 9 | Remove 1 from Mouse × 3 | Mouse × 2 |
| 10 | Remove remaining 2 | Mouse no longer in cart |
| 11 | Cart: Headphones × 2, Keyboard × 1, Mouse × 1 | Subtotal exactly 50 000 KZT |
| 12 | Subtotal 19 999; 20 000; 50 000; 100 000 | Automatic rates 0%, 5%, 10%, 15% |
| 13 | Subtotal 100 000 + promo STUDENT10 | 15%, not 25% |
| 14 | Subtotal 29 999 vs 30 000 | Delivery 1 500 vs 0 KZT |
| 15 | Recommendation, Accessories, budget 10 000 | Mouse only (if stocked) |
| 16 | Budget below checkout final total | No purchase, stock/cart/history unchanged |
| 17 | Cancel checkout confirmation | No purchase, stock/cart/history unchanged |
| 18 | Successful checkout with valid budget | Correct receipt; stock reduced; cart cleared; history increased |
| 19 | Enter letters for quantity | Error prompt, no crash |
| 20 | Empty cart checkout | No purchase; meaningful message |
| 21 | Search with empty keyword | Ask for keyword, no accidental match-all |
| 22 | Purchase same product in two orders | Two unique order IDs and correct accumulated history |

**Boundary examples:** 20 000, 30 000, 50 000, 100 000. The thresholds refer to the **original cart subtotal**, before discount.

### Student report template

| Test # | Input | Expected | Actual | Pass/Fail | Explanation |
|---|---|---|---|---|---|
| 1 | Show products | All catalog items | ... | ... | ... |
| 2 | ... | ... | ... | ... | ... |

### Program invariants (must always be true)

- `stock >= 0` for every product;
- Cart quantities are positive and no more than stock;
- At most one cart line per product ID;
- Discounts are not added together;
- A failed/cancelled checkout changes **nothing** in cart, stock or history;
- Order history stores purchased details that do not change if the catalog later changes.
