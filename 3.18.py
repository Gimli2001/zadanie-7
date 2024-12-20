numbers=[7,8,92,10,131,1122,1323,1431,152,161,171,18,129]

def substraction(numbers):
    smallest=numbers[0]
    largest=numbers[0]
    for num in numbers:
        if num < smallest:
            smallest=num
    for num in numbers:
        if num > largest:
            largest=num
    return largest-smallest

def second_largest(numbers):
    largest=numbers[0]
    second=numbers[0]
    for num in numbers:
        if num > largest:
            second = largest #Przesuwamy wartocs largest do second!!!
            largest = num
        elif num > second and num != largest:
            second = num
    return second

def mediana(numbers):
    sorted_numbers = sorted(numbers)  # Sortujemy listę
    n = len(sorted_numbers)

    if n % 2 != 0:
        med = sorted_numbers[n // 2]
    else:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        med = (mid1 + mid2) / 2
    return med

def two_elements(numbers):
    largest=numbers[0]
    smallest=numbers[0]
    for num in numbers:
        if num > largest:
            largest=num
        if num < smallest:
            smallest=num
    new_numbers=[largest,smallest]
    return new_numbers

def string_array(numbers):
    return '-'.join(str(num) for num in numbers)


print(substraction(numbers))
print(second_largest(numbers))
print(mediana(numbers))
print(two_elements(numbers))
print(string_array(numbers))
