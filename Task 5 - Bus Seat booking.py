class Bus:
    def book_seat(self):
        seat = [['' for col in range(5)] for row in range(2)]

        seat[0][0] = 'D'
        seat[0][1] = 'AB'
        seat[0][2] = 'MD'
        seat[1][4] = 'LL'
        seat[1][0] = 'ES'
        seat[1][2] = 'T'

        for row in range(2):
            print(seat[row])

        # TODO 1: ask the user for their initials,
        # and a row and column for their seat
        initials = input("Enter your initials: ").upper()

        while initials == '':
            print("Initials cannot be empty.")
            initials = input("Enter your initials: ").upper()

        booked = False

        while booked == False:
            row_input = input("Enter a row number from 0 to 1: ")
            column_input = input("Enter a column number from 0 to 4: ")

            if row_input.isdigit() and column_input.isdigit():
                row = int(row_input)
                column = int(column_input)

                if row >= 0 and row < 2 and column >= 0 and column < 5:

                    # TODO 2: check whether that row and
                    # column is free (equal to '')
                    if seat[row][column] == '':

                        # TODO 3: if it is free, store the
                        # initials at that row and column
                        seat[row][column] = initials
                        booked = True
                        print("Seat booked successfully.")

                    else:
                        # TODO 4: if it is not free, display
                        # an error message and ask again
                        print("That seat is already booked.")

                else:
                    print("Invalid row or column.")

            else:
                print("Please enter numbers only.")

        print("Updated seating plan:")

        for row in range(2):
            print(seat[row])


bus = Bus()
bus.book_seat()
