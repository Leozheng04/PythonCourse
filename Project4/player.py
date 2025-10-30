import random 
import math 
class Player:
    def __init__(self, letter):
        self.letter = letter
    def get_move(self,game):
        pass
class ComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)
    def get_move(self,game):
        return random.choice(game.avaliable_moves())
class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)
    def get_move(self,game):
        valid_sqaure = False
        val = None
        while not valid_sqaure:
            sqaure = input(f"{self.letter}'s turn. Input move (0-9)")
            try:
                val = int(sqaure)
                if val not in game.avaliable_moves():
                    raise ValueError
                valid_sqaure = True
            except ValueError:
                print("Invalid Sqaure. Try again.")
        return val