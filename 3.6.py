arr = [15, 8, 31, 47, 2, 19]  # Input array
total = 0  # Initialize total sum variable
index = 0  # Initialize index variable

while index < len(arr):  # Loop through the array
    total += arr[index]  # Add the element at the current index to the total sum
    index += 1  # Move to the next index

mean = total / len(arr)  # Calculate the arithmetic mean
print("Array:", *arr)  # Print the original array
print("Mean:", mean)  # Print the arithmetic mean
