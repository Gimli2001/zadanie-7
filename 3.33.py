# Function to swap the first and last column of a 2D array
def swap_first_last_column(arr):
    """
    This function swaps the first column and the last column of the 2D array.
    :param arr: 2D array (list of lists)
    :return: The array with the first and last columns swapped
    """
    # Loop through each row of the array
    for row in arr:
        # Swap the first column (index 0) with the last column (index -1) in each row
        row[0], row[-1] = row[-1], row[0]

# Example 3x5 array with integer values
array = [
    [1, 2, 3, 4, 5],   # First row
    [6, 7, 8, 9, 10],  # Second row
    [11, 12, 13, 14, 15]  # Third row
]

# Print the array before swapping
print("Array before swapping:")
for row in array:
    print(row)  # Print each row in the array

# Swap the first and last column by calling the function
swap_first_last_column(array)

# Print the array after swapping
print("\nArray after swapping:")
for row in array:
    print(row)  # Print each row in the updated array
