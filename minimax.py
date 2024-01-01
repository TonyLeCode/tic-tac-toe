import copy
import random

class Minimax:
    def getMove(self, board):
        available_moves = board.get_available_moves()
        move = random.choice(available_moves)
        return move
    def __algorithm(self):
        pass
    def __evaluate(self, board):
        # 0: unfinished game or draw
        # -10: O is winning
        # 10: X is winning
        result = board.check_win()
        if result == 0 or result == 2:
            return 0
        if board.current_player() == "X":
            return 10
        else:
            return -10