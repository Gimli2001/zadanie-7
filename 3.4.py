arr = [-15, 8, -31, 47, -2, 19]  # Input array

# Initialize max and min with the first element
max_num = arr[0]
min_num = arr[0]

for num in arr:  # Loop through each element in the array
    if num > max_num:  # Update max if a larger number is found
        max_num = num
    if num < min_num:  # Update min if a smaller number is found
        min_num = num

print("Max:", max_num)  # Print the maximum value
print("Min:", min_num)  # Print the minimum value
