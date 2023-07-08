import pygame

from COLORS import *

"""
Class Button

pos - координаты кнопки
size - размер 
clr - цвет кнопки 
cngclr - цвет кнопки при наведении мышкой 
func - функция которая срабатывает при нажатии 
text - надпись на кнопке
font - шрифт для текста на кнопке
font_size - размер шрифта
font_clr - цвет шрифта

func "draw" занимается отрисовкой самой кнопки
func "mouseover" возвращает изначальный цвет кнопки, если убрать с нее курсор


Class Text

text - выводимый текст 
pos - координаты текста
clr - цвет текста
font - шрифт текста
font_size - размер шрифта
mid - находится ли по центру экрана

func "draw" занимается отрисовкой самого текста
"""


class Button:
    def __init__(self, pos, size=(100, 50), clr=WHITE, cngclr=RED, func=None, text='', font="Times New Roman",
                 font_size=16, font_clr=(0, 0, 0)):

        self.clr = clr
        self.size = size
        self.func = func
        self.surf = pygame.Surface(size)
        self.rect = self.surf.get_rect(center=pos)

        if cngclr:
            self.cngclr = cngclr
        else:
            self.cngclr = clr

        if len(clr) == 4:
            self.surf.set_alpha(clr[3])

        self.font = pygame.font.SysFont(font, font_size)
        self.txt = text
        self.font_clr = font_clr
        self.txt_surf = self.font.render(self.txt, 1, self.font_clr)
        self.txt_rect = self.txt_surf.get_rect(center=[wh // 2 for wh in self.size])

    def draw(self, screen):
        self.mouseover()
        self.surf.fill(self.curclr)
        self.surf.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surf, self.rect)

    def mouseover(self):
        self.curclr = self.clr
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.curclr = self.cngclr


class Text:
    def __init__(self, text, pos, clr=(100, 100, 100), font="Segoe Print", font_size=15, mid=False):
        self.position = pos
        self.font = pygame.font.SysFont(font, font_size)
        self.txt_surf = self.font.render(text, 1, clr)

        if len(clr) == 4:
            self.txt_surf.set_alpha(clr[3])

        if mid:
            self.position = self.txt_surf.get_rect(center=pos)

    def draw(self, screen):
        screen.blit(self.txt_surf, self.position)
