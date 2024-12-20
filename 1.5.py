arr=[1,2,3,4,5]
def sub(arr):
    arr[0]-=1
    print(arr)

def inc(arr):
    arr[len(arr)-1]+=4
    print(arr)

def mul(arr):
    arr[(len(arr)-1)//2]*=2
    print(arr)

def menu():
    while True:
        print('\nWybierz Opcje: ')
        print('1:Odejmowanie')
        print('2:dodawanie')
        print('3:mnozenie')
        print('4:wyjscie')
        wybor=input('Twoj wybor: ')
        if wybor=='1':
            sub(arr)
        elif wybor=='2':
            inc(arr)
        elif wybor=='3':
            mul(arr)
        elif wybor=='4':
            print('Zdecydowales sie na wyjscie z programu')
            break
        else:
            print('Wybrales zla opcje sprobuj ponownie')

menu()



