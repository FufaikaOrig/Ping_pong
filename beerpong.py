from pygame import *
from GameSprite import GameSprite
from Player import Player
import pygame.time
import random

# создай окно игры
window = display.set_mode((700, 500))
display.set_caption("Пиво понг")


# задай фон сцены
background = transform.scale(image.load("jermbo.png"), (700, 500))

fish = Player('fish.jpg',0, 100, 10, (40, 200), window)
fish2 = Player('fish.jpg',600, 100, 10, (40, 200), window)

speed_x = 5
speed_y = 5

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('FISH 1 LOSE', True, (100, 0, 0))
font2 = font.Font(None, 35)
lose2 = font2.render('FISH 2 LOSE', True, (100, 0, 0))

FPS = 30
clock = time.Clock()

Ball = GameSprite('pivo.jpg', 100, 100, 10, (80, 80), window)

game = True
finish = False
while game:

    # Установка ФПС
    clock.tick(FPS)
    window.blit(background, (0, 0))

    for e in event.get():
        # обработай событие «клик по кнопке "Закрыть окно"»
        if e.type == QUIT:
            game = False

    if finish != True:
        Ball.rect.x += speed_x
        Ball.rect.y += speed_y

        if Ball.rect.y > 500 - 50 or Ball.rect.y < 0:
            speed_y *= -1

        if Ball.rect.x < -10:
            window.blit(lose1, (200, 200))
            finish = True


        if Ball.rect.x > 700:
            window.blit(lose2, (200, 200))
            finish = True


        if sprite.collide_rect(fish, Ball) or sprite.collide_rect(fish2, Ball):
            speed_x *= -1


        fish.reset()
        fish.update_l()

        Ball.reset()
        Ball.update()

        fish2.reset()
        fish2.update_r()

        display.update()
