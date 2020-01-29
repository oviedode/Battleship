from typing import Iterable
from .Move import Move

class Player(object):
    def __init__(self,  other_player: Iterable("Player")) -> None:
        self.name = self.get_name_from_player(other_player)
        self.place = None

    # Gets name from players
    def get_name_from_player(self, other_player: Iterable("Player")) -> str:
        already_used_names = set(player.name for player in other_player)
        while True:
            name = input("Please Enter Your Name: ")
            if name not in already_used_names:
                return name
            else:
                print(f'{name} has already been used.')

    @staticmethod
    def get_place_from_player(self, other_player: Iterable("Player")) -> str:
        already_used_places = set(player.place for player in other_player)
        while True:
            place = input("Please Enter The Place: "), strip()
            if len(place) > 1:
                print("The place may only be a single character. Pick another  ")
            elif place = blank_character:
                print("")
            elif place in already_used_places
            else:
                print(f'{name} has already been used.')

    # Print a player
    def __str__(self) -> str:
        return self.name

    def take_turn(self) -> None:
        move = self.getmove()
        move_do()

    def get_move(self):
        while True:
            str_move  = input("")
            try:
                return Move(str_move)
            except MoveError:
                print(MoveError)