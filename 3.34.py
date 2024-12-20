# Function to create an identity matrix of size n
def identity_matrix(n):
    """
    This function returns an identity matrix of size n.
    An identity matrix has ones on the diagonal and zeros elsewhere.
    
    :param n: The size of the matrix (n x n)
    :return: A 2D list representing the identity matrix
    """
    # Initialize an empty list to hold the rows of the matrix
    matrix = []

    # Loop through each row index
    for i in range(n):
        # Create a row that has 1 at the i-th index and 0 elsewhere
        row = [1 if j == i else 0 for j in range(n)]
        matrix.append(row)
    
    return matrix

# Function to print a 2D array in rows and columns
def print_matrix(matrix):
    """
    This function prints the 2D array (matrix) row by row.
    
    :param matrix: The 2D list (matrix) to be printed
    """
    for row in matrix:
        print(" ".join(map(str, row)))  # Print each row with space-separated values

# Main program to create and print identity matrices of sizes 3, 5, and 8
# Identity matrix of size 3
print("Identity Matrix of size 3:")
matrix_3 = identity_matrix(3)
print_matrix(matrix_3)
print()  # Empty line for spacing

# Identity matrix of size 5
print("Identity Matrix of size 5:")
matrix_5 = identity_matrix(5)
print_matrix(matrix_5)
print()  # Empty line for spacing

# Identity matrix of size 8
print("Identity Matrix of size 8:")
matrix_8 = identity_matrix(8)
print_matrix(matrix_8)
