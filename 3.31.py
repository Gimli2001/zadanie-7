# Function to find the smallest and largest values in the array and their positions
def find_min_max(arr):
    # Initialize variables to store the minimum and maximum values and their positions
    min_val = float('inf')  # Set to infinity initially for minimum value
    max_val = float('-inf') # Set to negative infinity initially for maximum value
    min_pos = None          # Position of the minimum value
    max_pos = None          # Position of the maximum value

    # Loop through each row in the 2D array
    for i in range(len(arr)):
        # Loop through each column in the current row
        for j in range(len(arr[i])):
            # Check if the current value is smaller than the current minimum value
            if arr[i][j] < min_val:
                min_val = arr[i][j]  # Update minimum value
                min_pos = (i, j)     # Update position of minimum value
            
            # Check if the current value is larger than the current maximum value
            if arr[i][j] > max_val:
                max_val = arr[i][j]  # Update maximum value
                max_pos = (i, j)     # Update position of maximum value

    # Return the minimum and maximum values along with their positions
    return min_val, min_pos, max_val, max_pos

# Example 2D array
array = [[-38.19], [5.40], [-7.11], [29.16]]

# Find the smallest and largest values and their positions
min_val, min_pos, max_val, max_pos = find_min_max(array)

# Print the results
print(f"Smallest value: {min_val} at position (row {min_pos[0]}, column {min_pos[1]})")
print(f"Largest value: {max_val} at position (row {max_pos[0]}, column {max_pos[1]})")
