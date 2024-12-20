names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"] 

# Initialize the longest name as the first name in the list
longest_name = names[0]

# Loop through each name in the list
for name in names:
    if len(name) > len(longest_name):  # Check if the current name is longer
        longest_name = name  # Update the longest name


print("Names:", *names)
print("Longest name:", longest_name)
