from BoardHelper import *
from HitorySolver import *


def main():
    print(hue.bold("Hitory solver"))
    print(hue.cyan("Мы очень устали:("))
    print(hue.lcyan("Но ждем доску!"))
    board = input_board()
    show(board)

    while True:
        print(hue.bold('Чем могу помочь?: выход, подсказка, решение | '), end='')
        action = input().strip()
        if action == 'выход':
            break
        if action == 'подсказка':
            board = hint(board)
            show(board)
            continue

        if action == 'решение':  # repeatedly try hint and smart-mark board
            while not cannot_hint(board):
                board = hint(board)
                for i in range(len(board)):
                    for j in range(len(board[0])):
                        (num, indicator) = board[i][j]
                        if indicator == 3:
                            mark(board, i, j, 1)  # safe preserve
                            continue
                        if indicator == 4:
                            mark(board, i, j, 2)  # mark shaded
                            continue
                        continue
                    continue
                continue
            show(no_hint(board))
            continue


if __name__ == '__main__':
    main()
