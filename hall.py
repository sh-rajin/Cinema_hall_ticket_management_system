class Star_cinema:
    hall_list = []

    def entry_hall(self,hall):
        Star_cinema.hall_list.append(hall)
    
class Hall(Star_cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        self.seats = {}
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.show_list = []
        super().__init__()
        self.entry_hall(self)
        
    def entry_show(self,id,movie_name,time):
        self.id = id
        self.movie_name = movie_name
        self.time = time
        show_l = (id,movie_name,time)
        self.show_list.append(show_l)
        self.seats[id] = [[0 for i in range(self.cols)] for j in range(self.rows)]
    
    def book_show(self,show_id,tuple_list):
        print('\n')
        for row,col in tuple_list:
            if row < 0 or row >= self.rows or col < 0 or col >= self.cols:                    
                print(f"Invalid seat ({row}, {col}).")
            elif self.seats[show_id][row][col] == 1:
                print(f"Seat ({row}, {col}) is already booked.")
            else:
                self.seats[show_id][row][col] = 1
                print(f"Seat ({row}, {col}) booked successfully.")    
                        
    def view_show_list(self):
        for show_id, movie_name, time in self.show_list:
            print(f'Show ID: {show_id}\tMovie Name: {movie_name}\tTime: {time}')
    def view_available_seats(self,show_id):
        if show_id in self.seats:
            print('\n<------------Available Seats------------>\n') 
            for row in range(self.rows):
                for col in range(self.cols):
                    if self.seats[show_id][row][col] == 0:
                        print(f'available : {row}{col}')
                    else:
                        print(f'Booked : {row}{col}')
        else:
            print('\nInvalid Show Id.\n')
            
            
hall1 = Hall(5,5,1)
hall1.entry_show('11','Toofan','11:30 PM')                
hall1.entry_show('22','Jawan','9:30 PM')   

while True:
    print('\nOption :')
    print('1. View All Show Today.')
    print('2. View Avaiable Seats.')
    print('3. Book Ticket.')
    print('4. Exit.')
    op = int(input('Select Option : '))
    
    if op == 1:
        print('\n<-------------------All Show-------------------->\n')
        hall1.view_show_list()    
    elif op == 2:
        s_id = input('Enter Show Id : ')
        hall1.view_available_seats(s_id)
    elif op == 3:
        s_id = input('Enter Show Id : ')
        ticket_list = []
        if s_id in hall1.seats:
            quantity = int(input('Numbor of Ticket : '))
            for i in range(quantity):
                row = int(input('Enter Row : '))
                col = int(input('Enter Column : '))
                tup = (row,col)
                ticket_list.append(tup)
            hall1.book_show(s_id,ticket_list)
        else:
            print('\nInvalid Show Id.\n')
    elif op == 4:
        print('\n<----------------Thank You for visiting This System------------------->\n')
        break      
          