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

fish = Player('fish.jpg',0, 100, 10, (70, 200), window)
fish2 = Player('fish.jpg',500, 100, 10, (70, 200), window)

FPS = 30
clock = time.Clock()


game = True
finish = False
while game:

    # Установка ФПС
    clock.tick(FPS)

    for e in event.get():
        # обработай событие «клик по кнопке "Закрыть окно"»
        if e.type == QUIT:
            game = False


    if not finish:
        window.blit(background, (0, 0))
        fish.reset()
        fish.update_l()

        fish2.reset()
        fish2.update_r()
        display.update()
