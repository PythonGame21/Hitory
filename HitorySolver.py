def hint(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j][1] == 0:
                (num, indicator) = board[i][j]
                for _j in range(len(board[0])):
                    if _j != j and board[i][_j][0] == num and board[i][_j][1] == 1:
                        indicator = 4
                        break
                if indicator == 4:
                    board[i][j] = (num, indicator)
                    continue
                for _i in range(len(board)):
                    if _i != i and board[_i][j][0] == num and board[_i][j][1] == 1:
                        indicator = 4
                        break
                if indicator == 4:
                    board[i][j] = (num, indicator)
                    continue
                if 0 < j < len(board[0]) - 1:
                    if board[i][j - 1][0] == board[i][j + 1][0]:
                        indicator = 3
                if 0 < i < len(board) - 1:
                    if board[i - 1][j][0] == board[i + 1][j][0]:
                        indicator = 3
                if indicator == 3:
                    board[i][j] = (num, indicator)
                    continue
                no_reason = True
                for _j in range(len(board[0])):
                    if _j != j and board[i][_j][0] == num and board[i][_j][1] != 2:  # has reason
                        no_reason = False
                        break
                for _i in range(len(board)):
                    if not no_reason:
                        break
                    if _i != i and board[_i][j][0] == num and board[_i][j][1] != 2:
                        no_reason = False
                        break
                if no_reason:
                    board[i][j] = (num, 3)
                    continue
                two_one_shade = False
                for _j in range(len(board[0]) - 1):
                    if j not in [_j, _j + 1] and board[i][_j][0] == num and board[i][_j + 1][0] == num:
                        two_one_shade = True
                        break
                for _i in range(len(board) - 1):
                    if two_one_shade:
                        break
                    if i not in [_i, _i + 1] and board[_i][j][0] == num and board[_i + 1][j][0] == num:
                        two_one_shade = True
                        break
                if two_one_shade:
                    board[i][j] = (num, 4)
                    continue
                continue
            if board[i][j][1] == 1:
                top_indicator = board[i - 1][j][1] if i > 0 else 2
                bottom_indicator = board[i + 1][j][1] if i < len(board) - 1 else 2
                left_indicator = board[i][j - 1][1] if j > 0 else 2
                right_indicator = board[i][j + 1][1] if j < len(board[0]) - 1 else 2
                checker = (2 ** top_indicator) * (3 ** bottom_indicator) * (5 ** left_indicator) * (
                        7 ** right_indicator)
                if checker == 4 * 9 * 25:
                    board[i][j + 1] = (board[i][j + 1][0], 3)
                    continue
                if checker == 4 * 9 * 49:
                    board[i][j - 1] = (board[i][j - 1][0], 3)
                    continue
                if checker == 4 * 25 * 49:
                    board[i + 1][j] = (board[i + 1][j][0], 3)
                    continue
                if checker == 9 * 25 * 49:
                    board[i - 1][j] = (board[i - 1][j][0], 3)
                    continue
                continue
            continue
    return board


def cannot_hint(board):
    board = hint(board)
    for row in board:
        for cell in row:
            indicator = cell[1]
            if indicator in [3, 4]:
                return False
    return True


def mark(board, i, j, indicator):
    num = board[i][j][0]
    board[i][j] = (num, indicator)
    if indicator == 2:
        i_start = i - 1 if i > 0 else i
        i_end = i + 1 if i < len(board) - 1 else i
        j_start = j - 1 if j > 0 else j
        j_end = j + 1 if j < len(board[0]) - 1 else j
        for _i in range(i_start, i_end + 1):
            for _j in range(j_start, j_end + 1):
                if (_i != i and _j == j) or (_i == i and _j != j):  # neighbor cell
                    board[_i][_j] = (board[_i][_j][0], 1)
    return


def no_hint(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j][1] in [3, 4]:
                board[i][j] = (board[i][j][0], 0)
    return board
