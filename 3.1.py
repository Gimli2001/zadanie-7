
arr = [34, 7, 19, 4, 21, 8]  

count_even = 0  # Counter for even numbers
index = 0  # Index for iterating through the array

while index < len(arr):  # Loop until the index reaches the length of the array
    if arr[index] % 2 == 0:  # Check if the current element is even
        count_even += 1  # Increment the counter if the number is even
    index += 1  

print("Number of even values:", count_even)  
