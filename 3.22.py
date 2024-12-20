import random

def rand_elem(array):
 
    #Returns a randomly selected element from the array.
    #protection if user tries to define something else than array
    if not array:
        raise ValueError("Array is empty.")
    return random.choice(array)
array = [10, 20, 30, 40, 50]
print("Randomly selected elements:")
for _ in range(5):
    print(rand_elem(array))
