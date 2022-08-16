import random
board=["_","_","_"
       "_","_","_"
       "_","_","_"]
gameRunning=True
winner=None
current_player="x"


#game board
    def printboard(board):
        print(board[0] + "|" + board[1] + "|" + board[2])
        print(board[3] + "|" + board[4] + "|" + board[5])
        print(board[6] + "|" + board[7] + "|" + board[8])

#game board
def playerInput(board):
    inp=int(input("select a spot 1-9:"))
    if board[inp-1]=="-":
        board[inp-1]=currentPlayer
    else:
        print("oops player is already at that spot.")

   #check for win or tie
def checkHorizontale(board):
    global winner
    if board[0]==board[1]==board[2] and board[0]!="-":
        winner=board[0]
        return True
    elif board[3]==board[4]==board[5] and board[3]!="-":
        winner=board[3]
        return True
    elif board[6]==board[7]==board[8] and board[6]!="-":
         winner=board[6]
         return True

def checkDiag(board):
    global winner
    if board[0]==board[4]==board[8] and board[0]!="-":
        winner=board[0]
        return True
    elif board[2]==board[4]==board[6] and board[4]!="-":
        winner=board[2]
        return True
    elif board[2]==board[5]==board[8] and board[2]!="-":
         winner=board[2]
         return True

def checkIfWin(board):
    global gameRunning
    if checkHorizontle(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning=False

    elif checkRow(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning=False


    elif checkDiag(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning=False

def checkIfTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("it is a tie!")
        gameRunning=False

#switch player
def switchPlayer():
    global current_player
    if currentPlayer=="x":
        currentPlayer="0"
    else:
        currentPlayer="x"

def computer(board):
    while currentPlayer=="0":
        position=random.radint(0,8)
        if board[position] =="-":
            board[position] ="0"
            switchPlayer()

while gameRunning:
    printboard(board)
    playerInput(board)
    checkIfwin(board)
    checkIfTie(board)
    switchplayer()
    computer(board)
    checkIfwin(board)
    checkIfTie(board)
