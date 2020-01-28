from typing import Iterator
class Board(object):
    def __init__(self, num_rows:int, num_cols:int, blank_char:str) -> None:
        self.contents = [[blank_char for col in (num_cols)] for row in range(num_rows)]
        self.blank_char = blank_char

    @property
    def num_rows(self)-> int:
        return len(self[0])


    # Be able to print the board
    def __str__(self) -> str:
        return super().__str__()

    # Be able to iterate through board
    def __iter__(self):
        iter(self.contents)

    # Get element from board
    def __getitem__(self, index:int):
