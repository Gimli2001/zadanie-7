# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
   suma=0
   for row in cinema_seats:
       for seats in row:
           suma+=1
   return suma

def seats_available(seats):
    wolne_miejsca=0
    for row in cinema_seats:
        for seats in row:
            if seats == 'A':
                wolne_miejsca+=1
    return wolne_miejsca

def seats_booked(seats):
    zajete_miejsca = 0
    for row in cinema_seats:
        for seats in row:
            if seats == 'B':
                zajete_miejsca += 1
    return zajete_miejsca

def seat_status(seats, row, place):
    if cinema_seats[row-1][place-1] == 'A':
        return True
    return False

print('CINEMA INFORMATION TABLE')
print('Total seats:',seats_total(cinema_seats))
print('Seats available:',seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))