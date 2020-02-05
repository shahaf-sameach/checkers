import sys

from file_reader import FileReader
from game import Game
from game_consts import WHITE, BLACK, EMPTY, ILLEGAL_MOVE_ERROR, STATUS_OK, STATUS_ERROR, INCOMPLETE_GAME_ERROR

if __name__ == "__main__":
    filename = ""
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        print("Error, filename is required")
        exit(1)

    moves = FileReader.read(filename)

    game = Game()

    result = game.play(moves)

    if result[0] == STATUS_OK:
        if result[1] == WHITE:
            print("first")
        elif result[1] == BLACK:
            print("second")
        elif result[1] == EMPTY:
            print("draw")
    elif result[0] == STATUS_ERROR:
        if result[1] == ILLEGAL_MOVE_ERROR:
            print("line {} illegal move".format(result[2]))
        elif result[1] == INCOMPLETE_GAME_ERROR:
            print("incomplete game")







