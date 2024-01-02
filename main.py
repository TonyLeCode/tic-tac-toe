from ticTacToe import TicTacToeBoard, decode


def prompt_move():
    return int(input("Make a move: "))


def game_loop():
    board = TicTacToeBoard()
    result = 0

    while result == 0:
        board.print()
        move = prompt_move()
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
