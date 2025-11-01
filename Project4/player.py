import random 
class Player:
    def __init__(self, letter):
        self.letter = letter
    def get_move(self,game):
        pass
class ComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)
    def get_move(self,game):
        return random.choice(game.available_moves())
class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)
    def get_move(self,game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f"{self.letter}'s turn. Input move (1-9): ")
            try:
                val = int(square) - 1
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")
        return val