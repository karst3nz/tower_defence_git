import tower
from tower import *
from button import Button, Text
from defs import time_stamp, print_ts
from COLORS import *
import enemy
from enemy import *
import pygame

"""
Это основной цикл игры, который обрабатывает события,
отображает элементы интерфейса и взаимодействует с
игрой в зависимости от ее текущего состояния.
"""

# Инициализация pygame
pygame.init()
pygame.font.init()

# ограничение кадров игры (игровых тиков)
clock = pygame.time.Clock()
fps = 60

# Размеры экрана
screen_w = 800
screen_h = 600

# Создание окна игры
screen = pygame.display.set_mode((screen_w, screen_h))
screen.fill(BLACK)

# переменные для работы игры
running = True
main_menu = True
crash_warn_menu = False
game_test_place = False
debug_menu = False
game_running = False
main_game_bg_is_load = False
main_game_tower_place_is_load = False
money = 200
# wave = 1
font = pygame.font.SysFont("Arial", 16)

# Таймер для спавна врага
enemy_spawn_timer = pygame.time.get_ticks()
enemy_spawn_delay = 1500  # 1,5 секунды (в миллисекундах)

# Таймер для выстрелов башни
bullet_cd = 1000  # 1 секундa (в миллисекундах)
last_shot_time = pygame.time.get_ticks()  # Время последнего выстрела

# Основной цикл игры
while running:
    clock.tick(fps)
    pygame.display.set_caption(f"{time_stamp()} | Game")
    # настройки кнопок

    crash_button = Button(pos=(screen_w // 2 - 50, screen_h // 2 + 50), clr=WHITE, cngclr=RED,
                          text="Выход")
    play_button = Button(pos=(screen_w // 2 - 50, screen_h // 2 - 25), clr=WHITE, cngclr=RED,
                         text="Играть")
    debug_button = Button(pos=(70, screen_h - 70), clr=WHITE, cngclr=RED, text="Debug")
    restart_button = Button(pos=(70, screen_h - 530), clr=WHITE, cngclr=RED, text="Restart")
    exit_button = Button(pos=(screen_w // 2 + 70, screen_h // 2), clr=WHITE, cngclr=RED, text="Да")
    not_exit_button = Button(pos=(screen_w // 2 - 70, screen_h // 2), clr=WHITE, cngclr=RED, text="Нет")
    debug_test_place_button = Button(pos=(screen_w // 2 + 70, screen_h // 2), clr=WHITE, cngclr=RED,
                                     text="TEST_PLACE")
    tower_place_1 = Button(pos=(180, 90), size=(60, 60), cngclr=RED)
    tower_place_2 = Button(pos=(190, 295), size=(60, 60), cngclr=RED)
    tower_place_3 = Button(pos=(350, 190), size=(60, 60), cngclr=RED)
    tower_place_4 = Button(pos=(450, 295), size=(60, 60), cngclr=RED)
    tower_place_5 = Button(pos=(600, 200), size=(60, 60), cngclr=RED)
    tower_place_6 = Button(pos=(725, 345), size=(60, 60), cngclr=RED)
    money_text = Text(text=f"Золото - {money}", pos=(20, 20), clr=BLACK, font="Times New Roman", font_size=18)

    # лист с кнопками для отрисовки
    main_menu_button_list = [play_button, crash_button]
    debug_button_list = [debug_button, restart_button]
    warning_button_list = [exit_button, not_exit_button]
    debug_menu_button_list = [debug_test_place_button]
    place_for_tower_list = [tower_place_1, tower_place_2, tower_place_3, tower_place_4, tower_place_5, tower_place_6]
    text_list = [money_text]

    ##############################
    # Отображение главного меню
    ##############################

    if main_menu:
        # Отображение кнопок главного меню
        for b in main_menu_button_list:
            b.draw(screen)
    else:
        main_menu_button_list.clear()
        pygame.display.update()

    # if running:
    #     for d in debug_button_list:
    #         d.draw(screen)

    ##############################
    # Отображение меню предупреждения о выходе
    ##############################

    if crash_warn_menu:
        main_menu = False
        for w in warning_button_list:
            if w.rect.collidepoint(pos):
                if w == exit_button:
                    print_ts("EXIT")
                    running = False

                elif w == not_exit_button:
                    print_ts("NOT_EXIT")
                    main_menu = True
                    crash_warn_menu = False
                    screen.fill(BLACK)

    # if debug_menu:
    #     main_menu = False
    #     for d in debug_menu_button_list:
    #         if d.rect.collidepoint(pos):
    #             if d == debug_test_place_button:
    #                 print_ts("TEST_PLACE")
    #                 test_place.start()
    #                 debug_menu = False

    ##############################
    # Отображение игры
    ##############################

    if game_running:
        bg_image = pygame.image.load("img/BG.png")
        screen.blit(bg_image, (0, 0))
        main_menu = False
        # отрисовка текста в левойверхней части экрана
        # for i in text_list:
        #     i.draw(screen)
        if not main_game_bg_is_load:
            bg_image = pygame.image.load("img/BG.png")
            screen.blit(bg_image, (0, 0))
            main_game_bg_is_load = True
        # ячейки для башен
        for i in place_for_tower_list:
            i.draw(screen)
            main_game_tower_place_is_load = True
        for event in pygame.event.get():
            # Обработка событий в игре
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    for b in place_for_tower_list:
                        if b.rect.collidepoint(pos):
                            # Обработка нажатий кнопок для размещения башен
                            if b == tower_place_1:
                                print_ts('tower_place_1')
                                create(pos=(b.rect.x, b.rect.y), tower_place="tower_place_1")
                            elif b == tower_place_2:
                                print_ts('tower_place_2')
                                create(pos=(b.rect.x, b.rect.y), tower_place="tower_place_2")
                            elif b == tower_place_3:
                                print_ts('tower_place_3')
                                create(pos=(b.rect.x, b.rect.y), tower_place="tower_place_3")
                            elif b == tower_place_4:
                                print_ts('tower_place_4')
                                create(pos=(b.rect.x, b.rect.y), tower_place="tower_place_4")
                            elif b == tower_place_5:
                                print_ts('tower_place_5')
                                create(pos=(b.rect.x, b.rect.y), tower_place="tower_place_5")
                            elif b == tower_place_6:
                                print_ts('tower_place_6')
                                create(pos=(b.rect.x, b.rect.y), tower_place="tower_place_6")
        current_time = pygame.time.get_ticks()
        if current_time - enemy_spawn_timer >= enemy_spawn_delay:
            # Выполнить спавн врага
            spawn(0, 330)
            enemy_spawn_timer = current_time  # Сбросить таймер спавна
        all_sprites.update()  # Обновление спрайтов
        all_sprites.draw(screen)  # Отрисовка спрайтов на экране
        for enemy_sprite in enemies:
            for circle in circles:
                if enemy_sprite.rect.colliderect(circle.rect):
                    for enemy in enemies:
                        if enemy.rect.colliderect(circle.rect):
                            bullet_current_time = pygame.time.get_ticks()
                            if bullet_current_time - last_shot_time >= bullet_cd:
                                for tower, circle in zip(towers, circles):
                                    enemies_in_radius = pygame.sprite.spritecollide(circle, enemies, dokill=False)
                                    if enemies_in_radius:
                                        target_enemy = enemies_in_radius[0]  # Выбираем первого врага в радиусе
                                        tower.shoot(target_enemy)
                                bullet_cd = bullet_current_time  # Сбросить таймер спавна
                                # Пример вызова метода shoot() для первой башни


        # mouse_pos = pygame.mouse.get_pos()
        # mouse_text = font.render(f"Mouse position: {mouse_pos}", True, (0, 0, 0))
        # screen.blit(mouse_text, (10, 10))

    ##############################
    # Обработка событий и нажатий в игре
    ##############################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                for b in main_menu_button_list:
                    if b.rect.collidepoint(pos):

                        if b == play_button:
                            main_menu = False
                            print_ts("play")
                            game_running = True

                        elif b == crash_button:
                            main_menu = False
                            crash_warn_menu = True
                            print_ts("crash")
                            screen.fill(BLACK)
                            for warn in warning_button_list:
                                warn.draw(screen)
                            pygame.display.update()

                for b in debug_button_list:
                    if b.rect.collidepoint(pos):
                        if b == debug_button:
                            print_ts("DEBUG")
                            for d in debug_menu_button_list:
                                screen.fill(BLACK)
                                d.draw(screen)
                                main_menu = False
                                debug_menu = True

                        elif b == restart_button:
                            print_ts("RESTART")
                            main_menu = True
                            screen.fill(BLACK)

    pygame.display.flip()
