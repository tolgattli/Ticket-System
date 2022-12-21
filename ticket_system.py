
seats = ['A','B','C','D']
rows = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
prices = [230.0,180.0,130.0,80.0]

def show_menu():
    print('Welcome to the Ticket System\nHere are the seats position')
    for x in range(4):
        print(seats[x], rows[x])
    print('Prices for Seats are')
    for _ in range(len(seats)):
        print(seats[_] ,'Seat -->',str(prices[_]))
    print('Please select seat suitable for you(First seat then location (Ex: A 1)')
    print('If your selection is not suitable (filled) you will return to the menu\nYou can exit by pressing -1')

def selection():
    show_menu()
    select_row = 0
    select_seat = 0
    charge = 0
    while select_row != '-1':
        select_row = (input('Enter Row '))
        if select_row != '-1':
            select_seat = int(input('Enter Seat '))
        else:
            None   
        if select_row == 'A':
            rows[0][select_seat-1] = 1
            charge += prices[0]
            show_menu()
        if select_row == 'B':
            rows[1][select_seat-1] = 1
            charge += prices[1]
            show_menu()
        if select_row == 'C':
            charge += prices[2]
            rows[2][select_seat-1] = 1
            show_menu()
        if select_row == 'D':
            charge += prices[3]
            rows[3][select_seat-1] = 1
            show_menu()
        if select_row == '-1':
            print()
            print()
            print('Your seat is selected. Your charge is', str(charge))
            print()
            print('Your selections are looking like that ')
            for x in range(4):
                print(seats[x], rows[x])

        
selection()
                

                

        
        



        



