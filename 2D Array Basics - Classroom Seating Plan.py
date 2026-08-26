'''
A school hall has 4 rows of 6 seats. Empty seats are represented by '-' and occupied seats by 'X'. The starter code below creates the seating plan but does not display it correctly.

Challenge:
Complete the nested loop so that the whole 2D array is created with every seat set to '-.
Adapt the code so that it prints the seating plan as a neat grid (one row per line, seats separated by a space), rather than printing each row as a Python list.
Add code that marks seats (1,1), (2,4) and (3,0) as occupied ('X') before the grid is displayed.
Add a loop that counts and displays how many seats are free.


'''

rows = 4
cols = 6

seats = [['-' for col in range(cols)] for row in range(rows)]

# TODO 1: fill every seat with '-'
for row in range(rows):
    for col in range(cols):
        seats[row][col] = '-'

# TODO 3: mark seats (1,1), (2,4) and (3,0) as 'X'
seats[1][1] = 'X'
seats[2][4] = 'X'
seats[3][0] = 'X'

# TODO 2: display the grid neatly, one row per line
for row in range(rows):
    row_text = ''

    for col in range(cols):
        row_text = row_text + seats[row][col] + ' '

    print(row_text)

# TODO 4: count and display the number of free seats
free_seats = 0

for row in range(rows):
    for col in range(cols):
        if seats[row][col] == '-':
            free_seats = free_seats + 1

print("Free seats:", free_seats)
