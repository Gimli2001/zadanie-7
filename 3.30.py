# Create a function that generates a multiplication table of size 5x5
def create_multiplication_table():
    # Initialize a 5x5 array with zeros
    table = [[0 for _ in range(5)] for _ in range(5)]
    
    # Fill the array with multiplication table values using nested loops
    for i in range(5):  # Iterate through rows (1 to 5)
        for j in range(5):  # Iterate through columns (1 to 5)
            # Fill the table with multiplication values
            table[i][j] = (i + 1) * (j + 1)
    
    return table

# Create the multiplication table array
multiplication_table = create_multiplication_table()

# Print the multiplication table
print("Multiplication Table (5x5):")
for row in multiplication_table:
    print(row)  # Print each row of the table
