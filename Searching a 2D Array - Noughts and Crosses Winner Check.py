''' 
The 3x3 board below has already been filled in as a completed game of noughts and crosses. Adapt the code so that it searches the array and reports whether 'X', 'O' or nobody has won.

Challenge:
Write a loop that checks each row to see if all three cells match and are not blank.
Write a loop that checks each column in the same way.
Check both diagonals for a match.
If a winning line is found, print which player won and the row/column (or 'diagonal') where the win occurred. If no line matches, print 'No winner'.


'''


board = [
    ['X', 'X', 'X'],
    ['O', 'X', 'O'],
    ['O', 'O', 'X']
]

for row in range(3):
    print(board[row])

winner = ''

# TODO 1: check rows
for row in range(3):
    if board[row][0] != '' and board[row][0] == board[row][1] == board[row][2]:
        winner = board[row][0]
        print(winner, 'won on row', row + 1)

# TODO 2: check columns
for col in range(3):
    if board[0][col] != '' and board[0][col] == board[1][col] == board[2][col]:
        winner = board[0][col]
        print(winner, 'won on column', col + 1)

# TODO 3: check diagonals
if board[0][0] != '' and board[0][0] == board[1][1] == board[2][2]:
    winner = board[0][0]
    print(winner, 'won on diagonal')

if board[0][2] != '' and board[0][2] == board[1][1] == board[2][0]:
    winner = board[0][2]
    print(winner, 'won on diagonal')

# TODO 4: report the result
if winner == '':
    print('No winner')
else:
    print(winner, 'has won')

