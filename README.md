# 🛒 SmartShop — AP Computer Science Principles

**Python · Beginner → Intermediate · 8 lessons · 100 points**

**Student mission:** Develop a console-based online store: product catalog, search, shopping cart, recommendations, automatic discounts, delivery, simulated checkout, receipts and purchase history.

**Teacher:** Ulykbek Sarsenov

## 🚀 Student quick start

1. Read the [full requirements (28 sections)](REQUIREMENTS.md).
2. Learn the essential commands in [Python examples](examples/COMMANDS.md).
3. Open [starter.py](starter.py) in VS Code using Python 3.
4. Complete each TODO function independently, following the [lesson plan](LESSON_PLAN.md).
5. Verify your project against [testing scenarios](TESTING.md).
6. Review [grading rubric](GRADING.md) and [defense questions](DEFENSE.md).
7. If you finish early, try an [advanced challenge](ADVANCED.md).

## Project files

| File | What it includes |
|---|---|
| [REQUIREMENTS.md](REQUIREMENTS.md) | Complete specifications, menu, data formats, function contracts, example output, formulas |
| [starter.py](starter.py) | Scaffolded student program with TODOs — **not a finished solution** |
| [examples/COMMANDS.md](examples/COMMANDS.md) | Beginner explanations of variables, dictionaries, loops, functions, errors and sorting |
| [examples/sample_products.py](examples/sample_products.py) | Catalog data examples |
| [TESTING.md](TESTING.md) | 22 test ideas (submit at least 15 with actual results) |
| [GRADING.md](GRADING.md) | 100-point rubric |
| [DEFENSE.md](DEFENSE.md) | Submission requirements and questions |
| [LESSON_PLAN.md](LESSON_PLAN.md) | Eight lessons of 40 minutes |
| [ADVANCED.md](ADVANCED.md) | Optional features beyond the basic requirements |

## How to run

Download the code (Code → Download ZIP), extract it, open the folder in VS Code, then in the terminal run:

```bash
python starter.py
```

The starter program shows the menu but intentionally contains unfinished features. Your job is to implement the missing logic, test it, and submit the final file as `smartshop.py`.

## Requirements at a glance

- Minimum **10 products** across **3 categories**, modeled with a list of dictionaries.
- Main menu with options **1–8 and 0**.
- Search by partial name or category (case-insensitive).
- Add and remove quantities safely. Stock is deducted **only on successful checkout**.
- Discounts: **0%, 5%, 10%, 15%**, with optional **STUDENT10** promo (highest applicable rate only).
- Free delivery when subtotal is at least **30,000 KZT**, otherwise **1,500 KZT** (empty cart: 0).
- Rule-based recommendations by per-item budget and category, ordered by price.
- Simulated checkout, receipt, history, and invalid input handling.

## Final submission

**smartshop.py**, project documentation, test report (**at least 15 cases**), screen recording (**1–2 minutes**) and short oral defense. The [rubric](GRADING.md) explains the full 100-point score.

**Important:** This is a **classroom AP CSP practice project**, not an official Create Performance Task solution. No real payment data or money is involved. Students must write and understand their own code.
