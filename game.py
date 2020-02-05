from game_consts import WHITE, BLACK, EMPTY, ILLEGAL_MOVE_ERROR, INCOMPLETE_GAME_ERROR, STATUS_OK, STATUS_ERROR
from game_utils import get_middle_tile, other_player


class Game(object):

    def __init__(self):
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.__setup()
        self.player = WHITE

    def play(self, moves):
        for idx, move in enumerate(moves, 1):
            status = self.__apply_move(move)
            if status:
                if status[0] == STATUS_ERROR:
                    return status[0], status[1], idx

                return status

        return STATUS_ERROR, INCOMPLETE_GAME_ERROR, "Incomplete Game"

    def __apply_move(self, move):
        src, dst = move

        for t in [src, dst]:
            if not self.__is_valid_tile(t):
                return STATUS_ERROR, ILLEGAL_MOVE_ERROR, "Invalid tile {}".format(t)

        if not self.__is_src_valid(src):
            return STATUS_ERROR, ILLEGAL_MOVE_ERROR, "Invalid src {}".format(src)

        if not self.__is_dst_valid(dst):
            return STATUS_ERROR, ILLEGAL_MOVE_ERROR, "Invalid dst {}".format(dst)

        if not self.__is_forward_move(move):
            return STATUS_ERROR, ILLEGAL_MOVE_ERROR, "Not a forward move {}".format(move)

        eating_moves = self.__eating_moves(src)
        if len(eating_moves) > 0:
            if dst in eating_moves:
                mid = get_middle_tile(src, dst)
                self.board[mid[0]][mid[1]] = 0
            else:
                return STATUS_ERROR, ILLEGAL_MOVE_ERROR, "Eat is possible, but wasn't chose"

        self.board[src[0]][src[1]] = 0
        self.board[dst[0]][dst[1]] = self.player

        if len(eating_moves) > 0 and len(self.__eating_moves(dst)) > 0:
            pass
        else:
            self.player = other_player(self.player)

        w_count, b_count = self.__player_count()
        if self.__is_game_over() or w_count == 0 or b_count == 0:
            if w_count > b_count:
                return STATUS_OK, WHITE
            elif w_count < b_count:
                return STATUS_OK, BLACK
            else:
                return STATUS_OK, EMPTY

        return None

    def __setup(self):
        for i in range(3):
            for j in range(1 if i % 2 == 0 else 0, 8, 2):
                self.board[i][j] = BLACK

        for i in range(5, 8):
            for j in range(1 if i % 2 == 0 else 0, 8, 2):
                self.board[i][j] = WHITE

    def __eating_moves(self, src):
        moves = []
        row, col = src
        other_p = other_player(self.player)

        if self.player == WHITE:
            if row - 2 >= 0:
                if col - 2 >= 0 and self.board[row - 1][col - 1] == other_p and self.board[row-2][col-2] == 0:
                    moves.append((row - 2, col - 2))
                if col + 2 <= 7 and self.board[row - 1][col + 1] == other_p and self.board[row-2][col+2] == 0:
                    moves.append((row - 2, col + 2))

        elif self.player == BLACK:
            if row + 2 <= 7:
                if col - 2 >= 0 and self.board[row + 1][col - 1] == other_p and self.board[row + 2][col - 2] == 0:
                    moves.append((row + 2, col - 2))
                if col + 2 <= 7 and self.board[row + 1][col + 1] == other_p and self.board[row + 2][col + 2] == 0:
                    moves.append((row + 2, col + 2))

        return moves

    def __is_valid_tile(self, tile):
        return (tile[0] % 2 == 0 and tile[1] % 2 == 1) or \
               (tile[0] % 2 == 1 and tile[1] % 2 == 0)

    def __is_src_valid(self, tile):
        return self.board[tile[0]][tile[1]] == self.player and self.player != EMPTY

    def __is_dst_valid(self, tile):
        return self.board[tile[0]][tile[1]] == EMPTY

    def __is_forward_move(self, move):
        src, dst = move
        if self.player == WHITE and dst[0] - src[0] < 0:
            return True
        if self.player == BLACK and dst[0] - src[0] > 0:
            return True
        return False

    def __is_game_over(self):
        for i in range(8):
            for j in range(8):
                moving_tiles = []
                if self.board[i][j] == WHITE:
                    if i - 1 >= 0:
                        if j - 1 >= 0:
                            moving_tiles.append((i - 1, j - 1))
                        if j + 1 <= 7:
                            moving_tiles.append((i - 1, j + 1))
                elif self.board[i][j] == BLACK:
                    if i + 1 >= 0:
                        if j - 1 >= 0:
                            moving_tiles.append((i + 1, j - 1))
                        if j + 1 <= 7:
                            moving_tiles.append((i + 1, j + 1))

                for m in moving_tiles:
                    if self.board[m[0]][m[1]] == EMPTY:
                        return False

        return True

    def __player_count(self):
        white_count = 0
        black_count = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == WHITE:
                    white_count += 1
                elif self.board[i][j] == BLACK:
                    black_count +=1

        return (white_count, black_count)





