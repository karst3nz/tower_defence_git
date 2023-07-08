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


# Класс полоски здоровья
# class HealthBar(pygame.sprite.Sprite):
#     def __init__(self, max_health):
#         super().__init__()
#         self.max_health = max_health
#         self.current_health = max_health
#         self.width = 30
#         self.height = 5
#         self.image = pygame.Surface((self.width, self.height))
#         self.rect = self.image.get_rect()
#
#     def update(self, pos):
#         self.rect.centerx = pos[0]
#         self.rect.centery = pos[1] - 15
#
#         health_ratio = self.current_health / self.max_health
#         health_width = int(self.width * health_ratio)
#
#         pygame.draw.rect(self.image, (0, 255, 0), pygame.Rect(0, 0, health_width, self.height))
#         pygame.draw.rect(self.image, (255, 0, 0), pygame.Rect(health_width, 0, self.width - health_width, self.height))


# Группы спрайтов
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()


# Функция спавна врага
def spawn(x, y):
    enemy = Enemy(x, y)
    all_sprites.add(enemy)
    enemies.add(enemy)
    print_ts("Enemy spawned!")


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, health=100):
        super().__init__()
        self.image = pygame.image.load("img/enemy.png")  # Загрузка изображения
        self.image = pygame.transform.scale(self.image, (30, 30))  # Изменение размера
        self.rect = self.image.get_rect(center=(x, y))
        self.rect.x = x
        self.rect.y = y
        self.speed = 3
        self.target_positions = [(90, 330), (100, 150), (280, 150), (250, 368), (517, 387), (520, 270), (1000, 270)]
        self.current_target = 0
        self.health = health

        # Создание полоски здоровья
        # self.health_bar = HealthBar(health)
        # self.health_bar.update(self.rect.center)
        # all_sprites.add(self.health_bar)

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
            # self.health_bar.kill()
            print_ts("Enemy killed!")

    def hit(self):
        self.health -= 2.5
        # self.health_bar.current_health = self.health
        if self.health <= 0:
            self.kill()
            # self.health_bar.kill()
            print_ts("Enemy killed by Tower!")
