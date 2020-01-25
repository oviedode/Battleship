import sys

 if __name__ == '__main__':
     # to make sure that board dimension is provided
     if len(sys.argv >= 2):
         board_dim = int(sys.argv[1])
         game = Battleship(board_dim)
         game.play()



