from ticTacToe import TicTacToeBoard, decode
from minimax import Minimax


class AI:
    def __init__(self, ai=None):
        self.ai = ai

    def setAI(self, ai):
        self.ai = ai

    def makeMove(self, board):
        self.ai.makeMove(board)


def prompt_move():
    return int(input("Make a move: "))


def game_loop():
    ai = AI()
    print("0: Minimax")
    # print("1: Alpha-beta Pruning")
    # print("2: Monte Carlo Tree Search")
    # print("3: Neural Network")
    aiInput = int(input("Choose an AI: "))
    while aiInput not in [0]:
        print("Invalid choice.")
        aiInput = int(input("Choose an AI: "))
    match aiInput:
        case 0:
            minimaxAI = Minimax()
            ai.setAI(minimaxAI)
        case _:
            print("default ai")
            pass

    playerTurn = int(input("Choose 0(X) or 1(O): "))
    while playerTurn != 0 or playerTurn != 1:
        print("Invalid choice.")
        playerTurn = int(input("Choose 0(X) or 1(O): "))
    board = TicTacToeBoard()
    result = 0

    while result == 0:
        board.print()
        move = None
        if board.current_player == playerTurn:
            move = prompt_move()
        else:
            move = ai.makeMove(board)

        if not isinstance(move, int):
            print("Invalid input")
            continue

        if board.validate_move(move):
            board.make_move(move)
            result = board.check_win()
            if result == 0:
                board.toggle_player()
        else:
            print("Invalid move!")

    print("Game has ended.")
    if result == 1:
        print(f"{decode(board.current_player)} won!")
    elif result == 2:
        print("Draw!")
    board.print()


game_loop()
