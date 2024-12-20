monthly_expenses = [
   [200, 50, 100],
   [180, 60, 110],
   [220, 55, 105],
   [210, 65, 95]
]

# Inicjalizacja sum
food_total = 0
transport_total = 0
utilities_total = 0
monthly_total = 0
week_totals = [0,0,0,0]

# Obliczanie wydatków
for i, week in enumerate(monthly_expenses):
    food_total += week[0]       # Food total
    transport_total += week[1]  # Transport total
    utilities_total += week[2]  # Utilities total
    week_totals[i]=sum(week)  # Total for the current week
    monthly_total+=week_totals[i]

# Wyświetlenie wyników
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food_total)
print('Transport:', transport_total)
print('Utilities:', utilities_total)
print('Week 1:', week_totals[0])
print('Week 2:', week_totals[1])
print('Week 3:', week_totals[2])
print('Week 4:', week_totals[3])
print('---------------')
print('TOTAL:', monthly_total)
