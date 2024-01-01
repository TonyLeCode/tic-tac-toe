def decode(int):
    if int == 0:
        return "-"
    elif int == 1:
        return "X"
    elif int == 2:
        return "O"


class TicTacToeBoard:
    def __init__(self, board=[0, 0, 0, 0, 0, 0, 0, 0, 0], current_player=1):
        # 0 is empty, 1 is X, 2 is O
        self.board = board
        self.current_player = current_player

    def print(self):
        print(decode(self.board[0]), decode(
            self.board[1]), decode(self.board[2]))
        print(decode(self.board[3]), decode(
            self.board[4]), decode(self.board[5]))
        print(decode(self.board[6]), decode(
            self.board[7]), decode(self.board[8]))

    def validate_move(self, index):
        return self.board[index] == 0

    def get_available_moves(self):
        avaiable_moves = []
        for index in self.board:
            if self.validate_move(index):
                avaiable_moves.append(index)
        return avaiable_moves

    def make_move(self, index):
        self.board[index] = self.current_player

    def toggle_player(self):
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1

    def check_win(self):
        # 0: unfinished
        # 1: win
        # 2: draw
        # Check for horizontal win
        for i in range(3):
            if (
                self.board[(i * 3)] == self.current_player
                and self.board[(i * 3) + 1] == self.current_player
                and self.board[(i * 3) + 2] == self.current_player
            ):
                return 1
        # Check for vertical win
        for i in range(3):
            if (
                self.board[i] == self.current_player
                and self.board[i + 3] == self.current_player
                and self.board[i + 6] == self.current_player
            ):
                return 1
        # Check for diagonal win
        if (
            self.board[0] == self.current_player
            and self.board[4] == self.current_player
            and self.board[8] == self.current_player
        ):
            return 1
        if (
            self.board[2] == self.current_player
            and self.board[4] == self.current_player
            and self.board[6] == self.current_player
        ):
            return 1

        for i in range(9):
            if self.board[i] == 0:
                return 0
        return 2
