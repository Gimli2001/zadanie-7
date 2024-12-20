# Define a 2x4 two-dimensional array
array = [
    [1, 2, 3, 4],  # First row of the array
    [5, 6, 7, 8]   # Second row of the array
]

# Print the array values row by row
print("Array values in rows:")
for row in array:
    # Print the entire row as a list
    print(row)

# Print the array values in rows and columns format
print("\nArray values in rows and columns:")
for i in range(len(array)):
    for j in range(len(array[i])):
        # Print the specific element with its row and column index
        print(f"Element at row {i+1}, column {j+1}: {array[i][j]}")
    # Add a blank line after each row for better readability
    print()
