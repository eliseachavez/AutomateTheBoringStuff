# 1) the dict below is a data struture
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 
        'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
        'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

# 2) the def below INTERPRETS the data structure
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# 3) the code below makes the data structure interactive
turn = 'X'
for i in range(9): # a for loop that goes 9 times because there are 9 spaces to potentially fill/play
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'
    #check for a win
    checkForWin(theBoard, move, turn)


#can i add something so that it checks at the end of each loop for a win? 3 in a row, horz, vert, or diagonal?
#this will be my code

def checkForWin(board, lastMove, turn):
    #what is the last move? look at what's around it
    # 1) is it mid-M? need to check all 8 boxes around it. also needs to be first bc it is most specific
    # 2) is it any other -M? check left and right of middle column
    # 3) is it any other -L? check the row (2 cells to the right)
    # 4) is it any other -R? check the row (2 cells to the left) 
    #corner and middle need diagonals checked...
    
    count = 0 
    
    if lastMove == 'mid-M':
            #need a count. once you've hit two...
            while count < 3:
                for k,v in board:
                    if k is 'mid-M':
                        #don't count
                    else:
                        if v is turn:
                            count++

    #elif 
