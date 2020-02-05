

foo = lambda move : abs(7 - move)

class FileReader(object):

    @staticmethod
    def read(filename):
        with open(filename) as f:
            lines = f.readlines()

        lines_moves = [[int(s) for s in l.strip().split(",")] for l in lines]

        moves = []
        for move in lines_moves:
            src = (foo(move[1]), foo(move[0]))
            dst = (foo(move[3]), foo(move[2]))
            moves.append((src, dst))

        return moves


if __name__ == "__main__":
    lines = None
    with open('incomplete.txt') as f:
        lines = f.readlines()

    moves_b = [[int(s) for s in l.strip().split(",")] for l in lines]

    moves = []
    for idx, m in enumerate(moves_b):
        src = (foo(m[1]), foo(m[0]))
        dst = (foo(m[3]), foo(m[2]))
        moves.append((src, dst))

    board = [[0 for j in range(8)] for i in range(8)]

    arrange(board)
    draw(board)
    next_player = 1
    for idx, move in enumerate(moves,1):
        print("applying move[{}] {} of player {}".format(idx, move, next_player))
        next_player = apply_move(board, move, next_player)
        draw(board)





    # for idx, move in enumerate(moves):
    #     if idx % 2 == 0:
    #         print("white: ", end='')
    #     else:
    #         print("black: ", end='')
    #     print(move)
