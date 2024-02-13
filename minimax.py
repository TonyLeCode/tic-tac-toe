class Minimax:
    def __init__(self, ai_turn = 1):
        self.ai_turn = ai_turn
    
    def setAiTurn(self, ai_turn):
        self.ai_turn = ai_turn

    def getMove(self, board):
        bestVal = -1000
        bestMove = -1

        # Uses backtracking
        available_moves = board.get_available_moves()
        for move in available_moves:
            board.make_move(move)
            # AI is the maximizer because it's always given score of 10 if it wins
            # However, a move will be made above, therefore false will be passed in
            # the following function since it will be evaluating the opponent's move
            moveValue = self.__algorithm(board, 0, False)
            board.clear_index(move)
            board.toggle_player()
            if moveValue > bestVal:
                bestMove = move
                bestVal = moveValue
        print("The value of the best Move is :", bestVal) 
        return bestMove

    def __algorithm(self, board, depth, isMaximizer):
        # We do not use depth, but it is useful for more complex games
        score = self.__evaluate(board)
        if (score == 10 or score == -10):
            board.toggle_player()
            return score
        if (len(board.get_available_moves()) == 0):
            board.toggle_player()
            return 0
        board.toggle_player()

        if (isMaximizer):
            best = -1000
            available_moves = board.get_available_moves()
            for move in available_moves:
                board.make_move(move)
                best = max(best, self.__algorithm(
                    board, depth+1, not isMaximizer))
                board.clear_index(move)
                board.toggle_player()
            return best
        else:
            best = 1000
            available_moves = board.get_available_moves()
            for move in available_moves:
                board.make_move(move)
                best = min(best, self.__algorithm(
                    board, depth+1, not isMaximizer))
                board.clear_index(move)
                board.toggle_player()
            return best

    def __evaluate(self, board):
        # 0: unfinished game or draw
        # -10: player/opponent is winning
        # 10: ai is winning
        result = board.check_win()
        if result == 0 or result == 2:
            return 0
        if board.current_player == self.ai_turn:
            return 10
        else:
            return -10
