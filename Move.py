from.Player import Player


class Move(object):
    def __init__(self,maker:"Player", row:int, col:int) -> None:
        self.maker = maker
        self.row = row
        self.col = col

    @classmethod
    def from_str(self, maker:"Player", str_move: str) -> 'Move':

        try:
            row,col = str_move.split(',')
        except ValueError:
            raise MoveError(f'{str_move} is not in the form row, col')

        try:
            row = int(row)
        except ValueError:
            raise MoveError (f'row needs to be an integer. {row} is not an integer')

    # for X's and O's
    def hits_and_misses(self, other):



