# Function to convert a 2D array into a 1D array
def convert_2d_to_1d(arr):
    """
    This function converts a 2D array into a 1D array by flattening the 2D array.
    
    :param arr: The 2D array (list of lists) to be converted
    :return: A 1D list containing all elements from the 2D array
    """
    # Use list comprehension to flatten the 2D array into a 1D list
    return [element for row in arr for element in row]

# Function to print the 1D array
def print_1d_array(array):
    """
    This function prints a 1D array as a space-separated string.
    
    :param array: The 1D list to be printed
    """
    print(" ".join(map(str, array)))  # Join each element of the array with space and print

# Define the 2D arrays
matrix1 = [
    [2, 3],
    [1, 5]
]

matrix2 = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]

matrix3 = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]

# Print the 1D arrays after converting the 2D arrays

# Convert and print the first matrix
print("1D Array for Matrix 1:")
array1d_matrix1 = convert_2d_to_1d(matrix1)
print_1d_array(array1d_matrix1)
print()  # Empty line for spacing

# Convert and print the second matrix
print("1D Array for Matrix 2:")
array1d_matrix2 = convert_2d_to_1d(matrix2)
print_1d_array(array1d_matrix2)
print()  # Empty line for spacing

# Convert and print the third matrix
print("1D Array for Matrix 3:")
array1d_matrix3 = convert_2d_to_1d(matrix3)
print_1d_array(array1d_matrix3)
