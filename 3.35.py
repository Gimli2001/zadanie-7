# Function to transpose a matrix
def transpose_matrix(m):
    """
    This function returns the transpose of a matrix.
    The transpose of a matrix is obtained by swapping its rows and columns.
    
    :param m: The matrix to be transposed (2D list)
    :return: The transposed matrix
    """
    # Use zip and list comprehension to transpose the matrix
    return [list(row) for row in zip(*m)]

# Function to print a 2D matrix in rows and columns
def print_matrix(matrix):
    """
    This function prints the 2D matrix row by row.
    
    :param matrix: The 2D list (matrix) to be printed
    """
    for row in matrix:
        print(" ".join(map(str, row)))  # Join each element in the row with a space and print

# Define the input matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0],
    [5, 6, 7, 8]
]

# Print the transposed matrices

# Transpose and print the first matrix
print("Transposed Matrix 1:")
transposed_matrix1 = transpose_matrix(matrix1)
print_matrix(transposed_matrix1)
print()  # Empty line for spacing

# Transpose and print the second matrix
print("Transposed Matrix 2:")
transposed_matrix2 = transpose_matrix(matrix2)
print_matrix(transposed_matrix2)
