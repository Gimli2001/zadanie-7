# Function to check if a number occurs in the array
def occurs(number, array):
    return number in array  # Returns True if number is in the array, otherwise False

# Input from the user
number = int(input("Enter a number: "))  # Ask for input and convert to integer

# Define the array
array = [15, 38, 7, 23, 14]

# Print the entered number and the array
print(f"Number: {number}")
print(f"Array: {' '.join(map(str, array))}")  # Print the array

# Check if the number is in the array and print the result
if occurs(number, array):
    print(f"Result: number {number} appears in the array")
else:
    print(f"Result: number {number} does not appear in the array")
