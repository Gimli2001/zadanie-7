# Function to compare two arrays
def compare(array1, array2):
    return array1 == array2  # Return True if arrays are the same, False otherwise

# Arrays to be compared
arrays = [
    (["water", "book", "sky"], ["water", "book", "sky"]),
    ([True, False], [True, False, True]),
    ([5, 3, 1], [5, 3, 1]),
    ([3, 2, 1], [3, 2])
]

# Loop through each pair of arrays and compare them
for arr1, arr2 in arrays:
    print(f"Array1: {' '.join(map(str, arr1))}")  # Print array1
    print(f"Array2: {' '.join(map(str, arr2))}")  # Print array2
    result = "arrays are the same" if compare(arr1, arr2) else "arrays are different"  # Check if arrays are the same
    print(f"Comparison: {result}\n")  # Print the result of comparison
