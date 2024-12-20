arr = [15, 8, 31, 47, 2, 19] 
print("existed array:", *arr)  # Print the original array

reverse_arr = []  
for i in range(len(arr) - 1, -1, -1):  # Loop from last index to first
    reverse_arr.append(arr[i])  # Append each element to the reversed list

print("reverse array:", *reverse_arr)  # Print the reversed array
