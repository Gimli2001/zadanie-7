arr = [15, 8, 31, 47, 2, 19]  # Input array
total = 0  # Initialize total sum variable

for num in arr:  # Loop through each element to add them
    total += num

mean = total / len(arr)  # Calculate the arithmetic mean
print("Array:", *arr)  # Print the original array
print("Mean:", mean)  # Print the arithmetic mean
