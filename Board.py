from typing import Iterator, List

class Board(object):
    def __init__(self, num_rows:int, num_cols:int, blank_char:str) -> None:
        self.contents = [[blank_char for col in (num_cols)] for row in range(num_rows)]
        self.blank_char = blank_char

    @property
    def num_rows(self)-> int:
        return len(self[0])


    # Be able to print the board
    # Get the max of lengths and leave spaces; makes everything prettier
    def __str__(self) -> str:
        sep = ' ' * (max([len(str(self.num_rows)) , len(str(self.num_cols))])) + '/n'
        rep = sep + sep.join((str(i) for i in range(self.num_cols)))
        for row_index, row in enumerate(self):
            rep += str(row_index) + sep + sep.join(row) + '/n'
        return rep


    # Be able to iterate through board.
    # Class will not be Iterable unless you implement this method. return contents
    def __iter__(self) -> Iterator[List[str]]:
        return iter(self.contents)


    # Get element from board
    def __getitem__(self, index:int) -> List[str]:
        return self.contents[index]

    #def is _full(self) -> bool:
        #return all(
            #(space != self.blank_char for row in self for space in row))