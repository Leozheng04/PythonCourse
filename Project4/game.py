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
    def avaliable_moves(self):
        avaliable = []
        for i,move in enumerate(self.board):
            if move == " ":
                avaliable.append(move)
        return move