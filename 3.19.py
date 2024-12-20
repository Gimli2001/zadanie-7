# Pobieranie szereg liczb od użytkownika
user_input = input("Podaj szereg liczb (oddzielonych spacjami): ")

# Konwertowanie wprowadzonego tekstu na listę liczb
numbers = list(map(int, user_input.split())) #funkcja user_input.split dzieli ciag znakow na oddzielne

i=input("O jaka liczbe nowy szereg ma byc wiekszy? ")

new_numbers = [x + i for x in numbers]

# Wyświetlenie nowego szereg
print("Nowy szereg większy o 1 niż podany:")
print(new_numbers)
