# Define the array
arr = [2, 3, 2, 5, 8, 1, 9, 8]

# Create an empty list to store unique elements
unique_elements = []

# Loop through the array and find elements that appear only once
for num in arr:
    if arr.count(num) == 1:
        unique_elements.append(num)  # Add the unique element to the list

# Print the original array and the unique elements
print("Array:", *arr)
print("Unique elements:", *unique_elements)
