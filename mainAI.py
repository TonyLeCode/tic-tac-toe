from ticTacToe import TicTacToeBoard, decode
from minimax import Minimax
from alphaBetaPruning import AlphaBetaPruning


class AI:
    def __init__(self, ai=None):
        self.ai = ai

    def setAI(self, ai):
        self.ai = ai

    def getMove(self, board):
        return self.ai.getMove(board)
    
    def setAiTurn(self, ai_turn: int):
        self.ai.setAiTurn(ai_turn)


def prompt_move():
    return int(input("Make a move: "))


def game_loop():
    ai = AI()
    print("0: Minimax")
    print("1: Alpha-beta Pruning")
    # print("2: Monte Carlo Tree Search")
    # print("3: Neural Network")
    aiInput = int(input("Choose an AI: "))
    while aiInput not in [0,1]:
        print("Invalid choice.")
        aiInput = int(input("Choose an AI: "))
    match aiInput:
        case 0:
            minimaxAI = Minimax()
            ai.setAI(minimaxAI)
        case 1:
            alphaBetaPruningAI = AlphaBetaPruning()
            ai.setAI(alphaBetaPruningAI)
        case _:
            print("default ai")
            pass

    playerTurn = int(input("Choose 1(X) or 2(O): "))
    while playerTurn not in [1,2]:
        print("Invalid choice.")
        playerTurn = int(input("Choose 1(X) or 2(O): "))
    if (playerTurn == 1):
        ai.setAiTurn(2)
    else:
        ai.setAiTurn(1)
    board = TicTacToeBoard()
    # board = TicTacToeBoard([0, 1, 2, 0, 1, 0, 0, 2, 0])
    result = 0
    board.get_available_moves()

    while result == 0:
        board.print()
        move = None
        if board.current_player == playerTurn:
            move = prompt_move()
        else:
            move = ai.getMove(board)

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
