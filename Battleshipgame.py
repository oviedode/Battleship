

class BattleshipGame(object)
    def __init__(self,dimensions:int) -> None:
        self.board = None
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
        print(self.board)

    #Game is over when one wins
    def is_game_over(self):
        return self.winner()

    def winner(self) -> bool:
        pass





