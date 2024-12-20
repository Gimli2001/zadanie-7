# Define the 2D array with the given numbers
array = [
    [7, 3, 7, 9, 0],  # First row
    [2, 9, 0, 1, 5],  # Second row
    [3, 8, 6, 4, 7],  # Third row
    [8, 7, 1, 1, 5]   # Fourth row
]

# Initialize a variable to store the sum of the last column
last_column_sum = 0

# Loop through each row in the 2D array
for row in array:
    # Add the value from the last column (last element in the row) to the sum
    last_column_sum += row[-1]

# Print the result: sum of values in the last column
print("Sum of values in the last column:", last_column_sum)

