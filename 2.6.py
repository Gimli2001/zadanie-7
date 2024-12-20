# Define the square matrix
matrix = [
   [0, 0, 0],
   [0, 0, 0],
   [0, 0, 0]
]
n = len(matrix)

# Zamiana jedynek na diagonalnej
for i in range(n):
    matrix[i][i] = 1

for row in matrix:
    print(row)
