
class Player(object):
    def __init__(self) -> None:
        self.name = None
        self.place = None

    #Print a player
    def __str__(self) -> str:
        return self.name