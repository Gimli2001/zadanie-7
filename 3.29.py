# Define the function to create a 2D array
def create_2d_arr(x, y):
    # Create a 2D array with 'x' rows and 'y' columns filled with 0
    # The outer list comprehension generates 'x' rows
    # The inner list comprehension generates 'y' zeros for each row
    return [[0 for _ in range(y)] for _ in range(x)]

# Create a 3x5 array using the function
array = create_2d_arr(3, 5)

# Print the created array row by row
for row in array:
    print(row)  # Print each row in the 2D array
