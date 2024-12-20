# Function to return a string of n asterisks
def star(n):
    return '*' * n  # Return n asterisks as a string

# Array of integers
arr = [2, 6, 4, 9, 7]

# Loop through each number in the array
for num in arr:
    print(f"{num}: {star(num)}")  # Print the number followed by the corresponding number of asterisks
