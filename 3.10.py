# Define the two arrays
array1 = [4, 36, 12, 28, 9, 44, 5]
array2 = [5, 1, 36]

# Loop through each element in array1 and check if it is not in array2
for num in array1:
    if num not in array2:
        print(num)  # Print the number if it's not in array2
