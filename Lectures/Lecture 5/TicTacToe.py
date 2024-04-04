class Tictactoe:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = [] # board saved as a list
        for x in range(0, 9):
            self.board.append(str(x + 1))
        self.playerOneTurn = True
        self.winner = False

    def turn(self):
        return self.player1 if self.playerOneTurn else self.player2

    def gameWon(self):
        won = False
        for x in range(0, 3):
            y = x * 3
            if (self.board[y] == self.board[(y + 1)] and self.board[y] == self.board[(y + 2)]):
                won = True
            if (self.board[x] == self.board[(x + 3)] and self.board[x] == self.board[(x + 6)]):
                won = True

        if ((self.board[0] == self.board[4] and self.board[0] == self.board[8]) or
                (self.board[2] == self.board[4] and self.board[4] == self.board[6])):
            won = True
        return (won, self.player2 if self.playerOneTurn else self.player1)

    def makeMove(self, choice):
        if self.playerOneTurn:
            self.board[choice - 1] = 'X'
        else:
            self.board[choice - 1] = 'O'
        self.playerOneTurn = not self.playerOneTurn

    def getBoardTxt(self):
        board = f"""
        +===+===+===+
        | {self.board[0]} | {self.board[1]} | {self.board[2]} |
        +===+===+===+
        | {self.board[3]} | {self.board[4]} | {self.board[5]} |
        +===+===+===+
        | {self.board[6]} | {self.board[7]} | {self.board[8]} |
        +===+===+===+
        """
        return board

if __name__== "__main__":
    game = Tictactoe("Sam", "Joe")
    while not game.gameWon()[0]:
        print (game.getBoardTxt())
        try:
            print (game.turn(), end = " ")
            choice = int(input(">> "))
        except:
            print("please enter a valid field")
            continue
        if game.board[choice - 1] == 'X' or game.board[choice - 1] == 'O':
            print("illegal move, plase try again")
            continue

        game.makeMove(choice)
        end, winner = game.gameWon()
        if end:
            print(game.getBoardTxt())
            print("Player " + str(winner) + " wins!\n")