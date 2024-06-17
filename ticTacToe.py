import numpy as np
import copy


# Player is x(1) and computer is O(2)
class space:
    spaceType = 0  # 0 = empty, 1 = X, 2 = O

    def __init__(self, type):
        self.spaceType = type

    def returnSpace(self):
        return self.spaceType

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


# run to set up the board
def initGame():
    global board
    board = np.empty((3, 3), dtype=object)

    for y in range(3):
        for x in range(3):
            board[x][y] = space(0)


# prints the board
def printBoard():
    ret = "   A B C"

    for y in range(3):
        ret += "\n" + str(y + 1) + " |"
        for x in range(3):
            ret += str(board[x][y].printSpace()) + "|"

    ret += "\n"

    return ret


# returns false if player hasnt won and true if player has won
def hasPlayerWon(player):
    spaceValue = player

    # check if won in x direction
    for y in range(3):
        if (
            board[0][y].returnSpace()
            == spaceValue & board[1][y].returnSpace()
            == spaceValue & board[2][y].returnSpace()
            == spaceValue
        ):
            return True

    # check if won in y direction
    for x in range(3):
        if (
            board[x][0].returnSpace()
            == spaceValue & board[x][1].returnSpace()
            == spaceValue & board[x][2].returnSpace()
            == spaceValue
        ):
            return True

    # check if won diagonally
    if (
        board[0][0].returnSpace()
        == spaceValue & board[1][1].returnSpace()
        == spaceValue & board[2][2].returnSpace()
        == spaceValue
    ):
        return True

    if (
        board[2][0].returnSpace()
        == spaceValue & board[1][1].returnSpace()
        == spaceValue & board[0][2].returnSpace()
        == spaceValue
    ):
        return True

    return False


# combine with hasPlayerWon later
def hasTheoreticalPlayerWon(player, g):

    spaceValue = player
    grid = g

    # check if won in x direction
    for y in range(3):
        if (
            g[0][y].returnSpace()
            == spaceValue & g[1][y].returnSpace()
            == spaceValue & g[2][y].returnSpace()
            == spaceValue
        ):
            return True

    # check if won in y direction
    for x in range(3):
        if (
            g[x][0].returnSpace()
            == spaceValue & g[x][1].returnSpace()
            == spaceValue & g[x][2].returnSpace()
            == spaceValue
        ):
            return True

    # check if won diagonally
    if (
        g[0][0].returnSpace()
        == spaceValue & g[1][1].returnSpace()
        == spaceValue & g[2][2].returnSpace()
        == spaceValue
    ):
        return True

    if (
        g[2][0].returnSpace()
        == spaceValue & g[1][1].returnSpace()
        == spaceValue & g[0][2].returnSpace()
        == spaceValue
    ):
        return True

    return False


# returns 0 if game not won, 1 if X has won, 2 if O has won
def isGameWon():
    if hasPlayerWon(1):
        return 1
    elif hasPlayerWon(2):
        return 2
    return 0


# returns winner in string form
def retWinner():
    winner = isGameOver()

    if winner == 1:
        return "X has won"
    elif winner == 2:
        return "O has won"
    elif winner == 3:
        return "tie, Good Game!"
    else:
        return ""


# runs the players turn
def playerTurn():

    validMoove = False
    validX = False
    validY = False

    xcord = 0
    ycord = 0

    # Make sure the move is legit
    while validMoove == False:

        validX = False
        validY = False

        Xmove = input("Enter X Coordinate: ")
        Ymove = input("Enter Y Coordinate: ")

        if Xmove == "A" or Xmove == "a":
            xcord = 0
            validX = True
        elif Xmove == "B" or Xmove == "b":
            xcord = 1
            validX = True
        elif Xmove == "C" or Xmove == "c":
            xcord = 2
            validX = True
        else:
            print("Invalid x coordinate")

        if Ymove == "1":
            ycord = 0
            validY = True
        elif Ymove == "2":
            ycord = 1
            validY = True
        elif Ymove == "3":
            ycord = 2
            validY = True
        else:
            print("Invalid y coordinate")

        if validX & validY:

            if board[xcord][ycord].returnSpace() == 0:
                validMoove = True
            else:
                print("Space is full, try another one")

    board[xcord][ycord].changeSpace(1)


# return 0 if no, 1 if one won, 2 if computer won, 3 if stalemate
def isGameOver():

    winner = isGameWon()

    if winner != 0:
        return winner

    for y in range(3):
        for x in range(3):
            if board[x][y].returnSpace() == 0:
                return 0

    return 3


# game runner Note - will need to initgame before running runGame
def runGame():

    replay = True

    while replay:
        # Game loop
        print(printBoard())
        while isGameOver() == 0:
            # Player's move
            playerTurn()
            print(printBoard())

            # Computer turn
            computerTurn()
            print(printBoard())

        print(retWinner())

        play = input("do you want another game? y/n: ")
        if play == "n" or play == "N":
            replay = False
        if play == "y" or play == "Y":
            initGame()


# uses hasPlayerWon to find if there is any move that would allow a player to win
def finalMove(player):

    boardCopy = copy.deepcopy(board)
    ret = np.array([0, 0, 0])  # player, x cord, y cord

    for y in range(3):
        for x in range(3):
            boardCopy = copy.deepcopy(board)

            if boardCopy[x][y].returnSpace() == 0:

                boardCopy[x][y].changeSpace(1)
                if hasTheoreticalPlayerWon(1, boardCopy) and ret[0] != 2:
                    ret = np.array([1, x, y])

                boardCopy[x][y].changeSpace(2)
                if hasTheoreticalPlayerWon(2, boardCopy):
                    ret = np.array([2, x, y])

    return ret


# returns -1, -1 if no winning move and coordinates if there is a winning move
def winningMove():

    ret = np.array([-1, -1])
    b = finalMove(2)

    if b[0] == 2:
        ret[0] = b[1]
        ret[1] = b[2]

    return ret


# returns -1, -1 if no move required to block a win, coordinates if blocking move is neccesary
def blockingMove():

    ret = np.array([-1, -1])
    b = finalMove(1)

    if b[0] == 1:
        ret[0] = b[1]
        ret[1] = b[2]

    return ret


# returns best weighted offensive turn
def offense():

    xCord = 0
    yCord = 0

    # List of all 9 spaces (0 is top left and 8 is bottom right): give each space a weighted avg and whichever has the highest avg wins
    moves = np.array(
        [[0, 1, 0], [1, 2, 1], [0, 1, 0]]
    )  # initial weightings of each move

    counter = 0
    # Go through each space and if there is an O next to it in some direction assign a higher weight

    yCheck = 0
    xCheck = 0

    for y in range(3):
        for x in range(3):

            # loop around the current space
            for yA in range(3):
                for xA in range(3):

                    # Find the space currently being checked
                    if yA == 0:
                        yCheck = y - 1
                    elif yA == 1:
                        yCheck = y
                    elif yA == 2:
                        yA = y + 1

                    if xA == 0:
                        xCheck = x - 1
                    elif xA == 1:
                        xCheck = x
                    elif xA == 2:
                        xCheck = x + 1

                    # Check if its legal and give it a ranking
                    if (
                        yCheck >= 0
                        and yCheck <= 2
                        and xCheck >= 0
                        and xCheck <= 2
                        and (xCheck != x and yCheck != y)
                    ):
                        if board[xCheck][yCheck].returnSpace() == 2:
                            moves[x][y] = moves[x][y] + 1

    x = 0
    y = 0
    largest = 0

    for y in range(3):
        for x in range(3):
            if board[x][y].returnSpace() != 1 and board[x][y].returnSpace() != 2:
                if moves[x][y] > largest:
                    xCord = x
                    yCord = y
                    largest = moves[x][y]

    ret = np.array([xCord, yCord])
    return ret


# the computers turn: evaluates each type of turn and decides which is the best
def computerTurn():

    # first do the winning move if its a winning move
    coordinates = winningMove()
    if coordinates[0] != -1:
        x = coordinates[0]
        y = coordinates[1]
        board[x][y].changeSpace(2)
        return

    # if no winning move available check if a block is needed to stop oppnent from winning
    coordinates = blockingMove()
    if coordinates[0] != -1:
        x = coordinates[0]
        y = coordinates[1]
        board[x][y].changeSpace(2)
        return

    # if neither of the other two ran, do an offensive move
    coordinates = offense()
    x = coordinates[0]
    y = coordinates[1]
    board[x][y].changeSpace(2)


# Code running section
initGame()
runGame()
