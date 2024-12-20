categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

# Znalezienie indeksu najdroższego wydatku
max_expense_index = expenses.index(max(expenses))

# Wyświetlenie najdroższej kategorii
print(f"The most expensive category is {categories[max_expense_index]} with an expense of {expenses[max_expense_index]}")
