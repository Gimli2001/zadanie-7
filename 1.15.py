
###
# Bubble sort
#
def bubble_sort(arr):
   n=len(arr)
   for i in range(n):
      for j in range(n-1-i):
         if arr[j] > arr[j+1]:
             arr[j], arr[j + 1] = arr[j + 1], arr[j]
   return arr


# Przykładowe dane: spalanie paliwa samochodów
car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
print("Przed sortowaniem:", car_fuel_consumption)

# Sortowanie danych
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption)
print("Po sortowaniu:", sorted_car_fuel_consumption)

# Przykładowe dane: transakcje bankowe
bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
print("Przed sortowaniem:", bank_transactions)

# Sortowanie danych
sorted_bank_transactions = bubble_sort(bank_transactions)
print("Po sortowaniu:", sorted_bank_transactions)