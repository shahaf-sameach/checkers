from game_consts import WHITE, BLACK

get_middle_tile = lambda t1,t2 : (int(abs(t2[0] + t1[0]) / 2), int(abs(t2[1] + t1[1]) / 2))

other_player = lambda p : WHITE if p == BLACK else BLACK







