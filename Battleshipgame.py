from .Board import Board

class BattleshipGame(object):

    def __init__(self,dimensions:int) -> None:
        self.Board = Board(dimensions, dimensions)
        self.players = []

    def play(self)->None:
        #makes the player move
        #create the movement
        #make the player change turns
        while not self.is_game_over():
            self.display_game()
            the_move = current_player.move()
            the_move.make()
            self.change_turn()

        self.display_winner()

    #Prints the board
    def display_game(self) -> None:
        print(self.Board)

    #Game is over when one wins
    def is_game_over(self):
        return self.winner()

    def winner(self) -> bool:
        return self.all_ships_terminated() or self.partially_terminated()

    def change_turn(self) -> None:
        self.turn_currrent_player = (self.turn_current_player + 1) % 2







