# Function to implement Bubble Sort
def bubblesort(array):
    n = len(array)
    # Loop through all elements in the array
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

# Example arrays to be sorted
arrays = [
    [4, 36, 12, 28, 9, 44, 5],
    [15, 8, 31, 47, 2, 19],
    [9, 7, 1, 5, 3, 6, 8]
]

# Sort and print each array
for arr in arrays:
    sorted_array = bubblesort(arr)
    print(f"Sorted array: {sorted_array}")
