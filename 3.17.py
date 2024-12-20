data=([10,20,10,10],"tuple", [10,20],10)

number_of_ocurrences=0

for x in data:
    if x == 10:
        number_of_ocurrences += 1
    #sprawdzamy czy element jest lista
    elif isinstance(x,list):
        #iteracje po elementach listy
        for i in x:
            if i == 10:
                number_of_ocurrences += 1

print(number_of_ocurrences)