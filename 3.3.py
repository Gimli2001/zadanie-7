arr = [8, 2, 5, 1, 9]  # Input array
print("Array:", *arr)  # Print the original array
print("2nd power:", *[x**2 for x in arr])  # Compute and print the square of each element using list comprehension
