arr = [7, 9, 2, 4, 5, 6]

# wyrażenie (wartos for element in iterowalny_obiekt if warunek
even_numbers = [x for x in arr if x % 2 == 0]
odd_numbers = [x for x in arr if x % 2 != 0]

new_arr = even_numbers + odd_numbers

print(new_arr)
