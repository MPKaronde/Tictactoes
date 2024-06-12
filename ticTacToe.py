import numpy as np

class space:
    spaceType = 0 #0 = empty, 1 = X, 2 = O

    def __init__(self, type):
        self.spaceType = type

    def returnSpace(self):
        return  self.spaceType
    
    def changeSpace(self, type):
        self.spaceType = type
    
    def printSpace(self):
        ret = ""

        if self.spaceType == 0:
            ret = " "
        
        elif self.spaceType == 1:
            ret = "X"

        else:
            ret = "O"
        
        return ret

#run to set up the board
def initGame():
    global board
    board = np.empty((3, 3), dtype=object)

    for y in range(3):
        for x in range(3):
            board[x][y] = space(0)

#prints the board
def printBoard():
    ret = "   A B C"

    for y in range(3):
        ret += "\n" + str(y + 1) + " |"
        for x in range(3):
            ret += str(board[x][y].printSpace()) + "|"
    
    ret += "\n"

    return ret

#returns false if player hasnt won and true if player has won
def hasPlayerWon(player):
    spaceValue = player

    #check if won in x direction 
    for y in range(3):
        if board[0][y].returnSpace() == spaceValue & board[1][y].returnSpace() == spaceValue & board[2][y].returnSpace() == spaceValue:
            return True
        
    #check if won in y direction 
    for x in range(3):
        if board[x][0].returnSpace() == spaceValue & board[x][1].returnSpace() == spaceValue & board[x][2].returnSpace() == spaceValue:
            return True
        
    #check if won diagonally
    if board[0][0].returnSpace() == spaceValue & board[1][1].returnSpace() == spaceValue & board[2][2].returnSpace() == spaceValue:
        return True
    
    if board[2][0].returnSpace() == spaceValue & board[1][1].returnSpace() == spaceValue & board[0][2].returnSpace() == spaceValue:
        return True
 
    return False

#returns 0 if game not won, 1 if X has won, 2 if O has won
def isGameWon():
    if hasPlayerWon(1):
        return 1
    elif hasPlayerWon(2):
        return 2
    return 0

#returns winner in string form
def retWinner():
    winner = isGameWon()

    if winner == 1:
        return "X has won"
    elif winner == 2:
        return "O has won"
    else:
        return ""
    
#Code running section
initGame()
print(printBoard())
board[0][0].changeSpace(2)
board[1][0].changeSpace(2)
board[2][0].changeSpace(2)

print(printBoard())
print(retWinner())


