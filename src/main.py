from components.menu import Menu
from styles.theme import COLORS

import pygame

pygame.init()

width = 1280
height = 720

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Main Menu')

clock = pygame.time.Clock()
FPS = 60


playing = True


while playing:
    clock.tick(FPS)

    Menu(screen).display_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    pygame.display.update()

pygame.quit()
