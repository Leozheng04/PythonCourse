from player import HumanPlayer, ComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for n in range(9)]
        self.current_winner = None 
    def print_board(self):
        for i in range(3):
            row = self.board[i*3:(i+1)*3]
            print("| " + " | ".join(row) + " |")
    @staticmethod
    def print_board_number():
        temp = [str(i+1) for i in range(9)]
        for i in range(3):
            row = temp[i*3:(i+1)*3]
            print("| " + " | ".join(row) + " |")
    def available_moves(self):
        available = []
        for i,move in enumerate(self.board):
            if move == " ":
                available.append(i)
        return available
    def empty_squares(self):
        return " " in self.board
    def num_empty_square(self):
        return self.board.count(" ")
    def make_move(self,square,letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False
    def winner(self,square,letter):
        row_index = square // 3
        result = self.board[row_index*3:(row_index+1)*3]
        if all(spot == letter for spot in result):
            return True
        col_index = square % 3
        result = self.board[col_index::3]
        if all(spot == letter for spot in result):
            return True
        if square % 2 == 0:
            main_diag = [self.board[i] for i in [0,4,8]]
            anti_diag = [self.board[i] for i in [2,4,6]]
            if all(spot == letter for spot in main_diag) or all(spot == letter for spot in anti_diag):
                return True
        return False
def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_number()
    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square,letter):
            if print_game:
                print(f"{letter} makes a move to square {square}")
                game.print_board()
                print("")

        if game.current_winner:
            if print_game:
                print(f"{letter} wins!")
            return letter
        letter = 'O' if letter == 'X' else 'X'
    if print_game:
        print("It's a tie!")

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = ComputerPlayer('O')
    t = TicTacToe()
    play(t,x_player,o_player,print_game=True)
