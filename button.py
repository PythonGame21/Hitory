import pygame as pg


class Button:
    color = (255, 255, 255)

    def __init__(self, pos, width, height, txt, txt_pos, txt_size):
        self.height = height
        self.width = width
        self.text = txt
        self.rect = pg.Rect(pos[0], pos[1], width, height)
        self.txt_pos = txt_pos
        self.txt_size = txt_size

    def highlight(self, mouse_pos):
        if self.in_boards(mouse_pos):
            self.color = (0, 255, 255)
        else:
            self.color = (255, 255, 255)

    def in_boards(self, mouse_pos):
        if self.rect.x <= mouse_pos[0] <= self.rect.x + self.width:
            if self.rect.y <= mouse_pos[1] <= self.rect.y + self.height:
                return True
        return False

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)
        font = pg.font.Font(None, self.txt_size)
        text = font.render(self.text, True, (0, 0, 0))
        screen.blit(text, self.txt_pos)