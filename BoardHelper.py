import huepy as hue


def show(board):
    def convert(cell):
        (x, i) = cell
        num = '{n:>2}'.format(n=str(x))
        if i == 0:
            return hue.black(num)
        if i == 1:
            return hue.lightgreen(num)
        if i == 2:
            return hue.lightpurple(num)
        if i == 3 or i == 4:
            return hue.lcyan(num)
    display = [[convert(cell) for cell in row] for row in board]
    display = [' '.join(row) for row in display]
    display = '\n'.join(display)
    print(display)
    return


def input_board():
    print('Количество строк: ', end='')
    row_count = int(input().strip())
    print('Количество столбцов: ', end='')
    col_count = int(input().strip())
    board = []
    for _ in range(row_count):
        board.append([])
    print('Введите паззл с пробелом между столбцами:')
    for i in range(row_count):
        row_nums = [int(s) for s in input().strip().split(' ')]
        if len(row_nums) != col_count:
            raise ValueError('Input invalid')
        nums = [(n, 0) for n in row_nums]
        board[i] = nums
    return board
