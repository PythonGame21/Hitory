from HitorySolver import *
import pygame as pg
from button import Button
from random import randint


def main():
    pg.init()
    screen = pg.display.set_mode((600, 600))
    clock = pg.time.Clock()
    s_b = Button((50, 500), 150, 50, 'Решить', (75, 510), 40)
    h_b = Button((400, 500), 180, 50, 'Подсказать', (410, 510), 40)
    r_b = Button((223, 480), 150, 50, 'Рандом', (243, 490), 40)
    l_b = Button((223, 540), 150, 50, 'Загрузить', (230, 550), 40)

    board = [[(-1, 0)]]
    run = True
    while run:
        clock.tick(60)
        mouse_pos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if s_b.in_boards(mouse_pos):
                    board = solve(board)
                elif h_b.in_boards(mouse_pos):
                    board = hint(board)
                elif r_b.in_boards(mouse_pos):
                    board = random_board()
                elif l_b.in_boards(mouse_pos):
                    board = input_board()
        screen.fill((255, 255, 255))
        draw_board(screen, board)
        s_b.draw(screen)
        s_b.highlight(mouse_pos)
        h_b.draw(screen)
        h_b.highlight(mouse_pos)
        r_b.draw(screen)
        r_b.highlight(mouse_pos)
        l_b.draw(screen)
        l_b.highlight(mouse_pos)
        pg.display.flip()


def draw_board(surface, board):
    w = 400
    x = 100
    y = 50
    a = int(w / len(board))
    for i in range(len(board)):
        for j in range(len(board[0])):
            draw_sqr(surface, x + a*i, y + a*j, a, board[i][j][0], get_color(board[i][j][1]))


def get_color(i):
    if i == 0:
        return (110, 110, 110)
    if i == 1:
        return (0, 255, 0)
    if i == 2:
        return (255, 51, 255)
    if i == 3 or i == 4:
        return (0, 255, 255)


def draw_sqr(surface, x, y, a, num: int, color):
    points = [(x, y), (x + a, y), (x + a, y + a), (x, y + a)]
    pg.draw.polygon(surface, color, points)
    pg.draw.polygon(surface, (0, 0, 0), points, int(a / 15))
    font = pg.font.Font(None, a)
    text = font.render(str(num), True, (0, 0, 0))
    tx = int(x + a/3) if num < 10 else int(x + a/8)
    ty = int(y + a/5)
    surface.blit(text, (tx, ty))


def solve(board):
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
    return no_hint(board)


def input_board():
    board = []
    with open('input.txt', 'r') as f:
        with open('input.txt', 'r') as f:
            for line in f.readlines():
                board.append([(int(s), 0) for s in line.strip().split()])
    check_board(board)
    return board


def random_board():
    w = randint(4, 11)
    while True:
        board = []
        try:
            for i in range(w):
                board.append([(randint(1, 10), 0) for _ in range(w)])
            check_board(board)
            return board
        except:
            continue
    return board


def check_board(board):
    n = len(board)
    for row in board:
        sum = 0
        for cell, cl in row:
            sum += cell
        if 1 * n < sum < n**2:
            continue
        raise ValueError('Сумма чисел в строках некорректна')
    for i in range(n):
        summ = 0
        for row in board:
            cell, cl = row[i]
            summ += cell
        if 1 * n < summ < n**2:
            continue
        raise ValueError('Сумма чисел в столбцах некорректна')


if __name__ == '__main__':
    main()
