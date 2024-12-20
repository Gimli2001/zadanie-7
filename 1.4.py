###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4,]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[4])
ostatnia_wartosc=len(arr)-1
print('Last value',ostatnia_wartosc)
suma=arr[0]+len(arr)-1
print('Suma to ', suma)
srodkowa_wartosc=arr[(len(arr)-1)//2]
print('Srodkowa to ', srodkowa_wartosc)
for i in range(0,len(arr)):
    print(arr[i], end=' ')

