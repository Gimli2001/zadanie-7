import random 

arr1 = [3, 7, 1, 0, 4]  # A simple list of integers
arr2 = [[2, 3], [7, 1], [0, 4]]  # Two-dimensional array (list of lists)
arr3 = [7 for i in range(5)]  # A list of five 7's
arr4 = [i for i in range(1, 10)]  # A list of integers from 1 to 9 (inclusive)
arr5 = [i * 2 for i in range(1, 10)]  # Doubled values from 1 to 9
arr6 = [random.randint(1, 20) for i in range(10)]  # A list of 10 random integers between 1 and 20
arr7 = [[] for i in range(5)]  # A list of 5 empty lists
arr8 = [[1 for i in range(2)] for j in range(4)]  # Two-dimensional array with 4 rows and 2 columns filled with 1's
arr9 = [[random.randint(1, 20) for i in range(3)] for j in range(5)]  # Two-dimensional array with 5 rows and 3 columns filled with random integers
arr10 = [4, 0, 3]  # A list with the values 4, 0, 3
arr11 = [0 for _ in range(15)]  # A list of fifteen 0's
arr12 = [i for i in range(1, 31)]  # A list of integers from 1 to 30 (inclusive)
arr13 = [random.randint(0, 1) for _ in range(20)]  # A list of 20 random 0's and 1's
arr14 = [[False for _ in range(2)] for _ in range(5)]  # Two-dimensional array with 5 rows and 2 columns filled with False

print("arr1:", arr1)  
print("arr2:", arr2)  
print("arr3:", arr3) 
print("arr4:", arr4) 
print("arr5:", arr5) 
print("arr6:", arr6) 
print("arr7:", arr7) 
print("arr8:", arr8)  
print("arr9:", arr9)  
print("arr10:", arr10)  
print("arr11:", arr11) 
print("arr12:", arr12)  
print("arr13:", arr13) 
print("arr14:", arr14) 
