# Optional advanced challenges (after the main project works)

1. **JSON persistence** — save/load catalog and order history. Use `json.dump()`, `json.load()`, `with open(...)`. Catch missing-file errors.
2. **Admin panel** — password-protected *simulated* inventory management; don't store real personal passwords in plain text.
3. **Edit inventory** — add, rename, restock, deactivate products; preserve unique IDs.
4. **Random promo tokens** — use `import random` to generate classroom-only codes.
5. **Bestseller ranking** — count units from the snapshots in order history, sort descending.
6. **Desktop GUI** — `tkinter`, a standard Python GUI toolkit on supported installations.
7. **Sales chart** — `matplotlib` to plot simulated sales by category.
8. **Budget basket optimization** — find a combination of multiple products subject to one total budget. Distinguish this from the basic recommender, which only compares single-item prices.

### Advanced feature report

For the extension, explain (1) user benefit, (2) new data/functions, (3) one success test, (4) one failure/boundary test. A stylish interface alone is not sufficient if the underlying logic is incorrect.
