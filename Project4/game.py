class TicTacToe:
    def __init__(self):
        self.board = [['' for n in range(3)] for n in range(3)]
        self.current_winner = None 

    def print_board(self):
        for i in range(3):
            for j in range(3):
                print(f"| {self.board[i][j]} ", end = '')
            print("|")

    def win(self,c:str) -> bool:
        if ((self.board[0][0] == c and self.board[0][1] == c and self.board[0][2] == c) or
            (self.board[1][0] == c and self.board[1][1] == c and self.board[1][2] == c) or 
            (self.board[2][0] == c and self.board[2][1] == c and self.board[2][2] == c)):
            return True
        if ((self.board[0][0] == c and self.board[1][0] == c and self.board[2][0] == c) or
            (self.board[0][1] == c and self.board[1][1] == c and self.board[2][1] == c) or
            (self.board[0][2] == c and self.board[1][2] == c and self.board[2][2] == c) ):
            return True
        if ((self.board[0][0] == c and self.board[1][1] == c and self.board[2][2] == c) or
            (self.board[2][0] == c and self.board[1][1] == c and self.board[0][2] == c)):
            return True
        return False
    
    def game(self):
        pass