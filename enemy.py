import pygame
import random

from COLORS import *
from defs import print_ts

# Инициализация Pygame
pygame.init()

# Размеры экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Класс врага


# Группы спрайтов
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()


# Функция спавна врага
def spawn(x, y):
    enemy = Enemy(x, y)
    all_sprites.add(enemy)
    enemies.add(enemy)
    print_ts("Enemy spawned!")


import pygame





class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("img/enemy.png")  # Загрузка изображения
        self.image = pygame.transform.scale(self.image, (30, 30))  # Изменение размера
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 3
        self.target_positions = [(90, 330), (100, 150), (280, 150), (250, 368), (517, 387), (520, 270), (1000, 270)]
        self.current_target = 0
        self.health = 100


    def update(self):
        target_x, target_y = self.target_positions[self.current_target]
        dx = target_x - self.rect.x
        dy = target_y - self.rect.y
        distance = (dx ** 2 + dy ** 2) ** 0.5


        if distance > self.speed:
            self.rect.x += dx / distance * self.speed
            self.rect.y += dy / distance * self.speed
        else:
            self.current_target = (self.current_target + 1) % len(self.target_positions)

        if self.rect.x > screen_width or self.rect.y > screen_height:
            self.kill()
            print_ts("Enemy killed!")

    def hit(self):
        self.health -= 2.5
        if self.health <= 0:
            self.kill()
            print_ts("Enemy killed by Tower!")
