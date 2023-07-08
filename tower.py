import pygame

from COLORS import BLACK
from defs import time_stamp, print_ts
from enemy import all_sprites, screen, enemies

pygame.init()
pygame.font.init()
tower_1_is_created = 0
tower_2_is_created = 0
tower_3_is_created = 0
tower_4_is_created = 0
tower_5_is_created = 0
tower_6_is_created = 0
circles = []  # Список для хранения созданных кругов
towers = []


class TowerSprite(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = pygame.Rect(pos[0], pos[1], self.image.get_width(), self.image.get_height())
        self.bullets = pygame.sprite.Group()  # Группа для хранения патронов

    def update(self):
        screen.blit(self.image, self.rect)
        self.bullets.update()  # Обновление патронов
        self.bullets.draw(screen)  # Отрисовка патронов

    def shoot(self, target):
        bullet = Bullet(self.rect.center, target)
        self.bullets.add(bullet)  # Добавление патрона в группу
        all_sprites.add(bullet)  # Добавление патрона в общую группу спрайтов

    def delete(self):
        pass


class Circle(pygame.sprite.Sprite):
    def __init__(self, pos, radius, color, width, transparency):
        super().__init__()
        self.radius = radius
        self.color = color
        self.width = width
        self.transparency = transparency
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=pos)

        self.speed = 5
        self.direction = pygame.Vector2(1, 0)  # Направление движения (вправо)

    def update(self, ):
        pygame.draw.circle(self.image, (*self.color, self.transparency), (self.radius, self.radius), self.radius)


def create(pos=(0, 0),
           tower_place=None,
           tower_img=pygame.image.load("img/tower.png")):
    global tower_1_is_created, tower_2_is_created, tower_3_is_created, tower_4_is_created, tower_5_is_created, \
        tower_6_is_created
    tower_img = pygame.transform.scale(tower_img, (60, 60))
    if tower_place == "tower_place_1" and tower_1_is_created == 0:
        print(f'{time_stamp()} tower_1 has been created!')
        tower_1_is_created = 1
        # Создание спрайта башни
        tower_sprite_1 = TowerSprite(tower_img, pos)
        towers.append(tower_sprite_1)
        # Создание круга
        circle_1 = Circle((pos[0] + 30, pos[1] + 30), 120, (0, 0, 0), 2, 0)
        circles.append(circle_1)  # Добавление круга в список

        # Добавление спрайта башни в группу all_sprites
        all_sprites.add(tower_sprite_1)
        all_sprites.add(circle_1)




    elif tower_place == "tower_place_2" and tower_2_is_created == 0:
        print(f'{time_stamp()} tower_2 has been created!')
        tower_2_is_created = 1
        # Создание спрайта башни
        tower_sprite_2 = TowerSprite(tower_img, pos)
        towers.append(tower_sprite_2)
        # Создание круга
        circle_2 = Circle((pos[0] + 30, pos[1] + 30), 120, (0, 0, 0), 2, 0)
        circles.append(circle_2)
        all_sprites.add(tower_sprite_2)
        all_sprites.add(circle_2)

    elif tower_place == "tower_place_3" and tower_3_is_created == 0:
        print(f'{time_stamp()} tower_3 has been created!')
        tower_3_is_created = 1
        # Создание спрайта башни
        tower_sprite_3 = TowerSprite(tower_img, pos)
        towers.append(tower_sprite_3)
        circle_3 = Circle((pos[0] + 30, pos[1] + 30), 120, (0, 0, 0), 2, 0)
        circles.append(circle_3)
        # Добавление спрайта башни в группу all_sprites
        all_sprites.add(tower_sprite_3)
        all_sprites.add(circle_3)

    elif tower_place == "tower_place_4" and tower_4_is_created == 0:
        print(f'{time_stamp()} tower_4 has been created!')
        tower_4_is_created = 1
        # Создание спрайта башни
        tower_sprite_4 = TowerSprite(tower_img, pos)
        towers.append(tower_sprite_4)
        circle_4 = Circle((pos[0] + 30, pos[1] + 30), 120, (0, 0, 0), 2, 0)
        circles.append(circle_4)
        # Добавление спрайта башни в группу all_sprites
        all_sprites.add(tower_sprite_4)
        all_sprites.add(circle_4)

    elif tower_place == "tower_place_5" and tower_5_is_created == 0:
        print(f'{time_stamp()} tower_5 has been created!')
        tower_5_is_created = 1
        # Создание спрайта башни
        tower_sprite_5 = TowerSprite(tower_img, pos)
        towers.append(tower_sprite_5)
        circle_5 = Circle((pos[0] + 30, pos[1] + 30), 120, (0, 0, 0), 2, 0)
        circles.append(circle_5)
        # Добавление спрайта башни в группу all_sprites
        all_sprites.add(tower_sprite_5)
        all_sprites.add(circle_5)

    elif tower_place == "tower_place_6" and tower_6_is_created == 0:
        print(f'{time_stamp()} tower_6 has been created!')
        tower_6_is_created = 1
        # Создание спрайта башни
        tower_sprite_6 = TowerSprite(tower_img, pos)
        towers.append(tower_sprite_6)
        circle_6 = Circle((pos[0] + 30, pos[1] + 30), 120, (0, 0, 0), 2, 0)
        circles.append(circle_6)
        # Добавление спрайта башни в группу all_sprites
        all_sprites.add(tower_sprite_6)
        all_sprites.add(circle_6)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, target):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=pos)
        self.target = target
        self.speed = 5

    def update(self):
        if self.rect.colliderect(self.target.rect):
            self.target.hit()
            self.kill()
        else:
            dx = self.target.rect.centerx - self.rect.centerx
            dy = self.target.rect.centery - self.rect.centery
            distance = max(abs(dx), abs(dy))
            if distance > 0:
                self.rect.x += dx / distance * self.speed
                self.rect.y += dy / distance * self.speed
            else:
                self.kill()
