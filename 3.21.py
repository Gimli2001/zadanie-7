def is_subset(array1, array2):

    #Checks if array1 is a subset of array2.
# Check each element of array1
    for element in array1:
        if element not in array2:
            return False

    return True
array1 = [1, 2, 3]
array2 = [1, 2, 3, 4, 5]
if is_subset(array1, array2):
    print("Array1 is a subset of Array2.")
else:
    print("Array1 is NOT a subset of Array2.")

