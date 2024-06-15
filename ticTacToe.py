import numpy as np

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


# returns 0 if game not won, 1 if X has won, 2 if O has won
def isGameWon():
    if hasPlayerWon(1):
        return 1
    elif hasPlayerWon(2):
        return 2
    return 0


# returns winner in string form
def retWinner():
    winner = isGameWon()

    if winner == 1:
        return "X has won"
    elif winner == 2:
        return "O has won"
    else:
        return ""


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


# game runner Note - will need to initgame before running runGame
def runGame():

    print(printBoard())

    # Game loop
    while isGameWon() == 0:
        # Player's move
        playerTurn()
        print(printBoard())

        # Computer turn
        computerTurn()
        print(printBoard())

    print(retWinner())


def computerTurn():
    # The x and y cordinate that the computer will put down
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

    # end of the function
    print(str(xCord) + ", " + str(yCord))
    board[xCord][yCord].changeSpace(2)


# Code running section
initGame()
runGame()
