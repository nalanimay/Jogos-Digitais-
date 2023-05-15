from styles.theme import COLORS
from components.button import Button
# from components.menu import Menu

import pygame


class Screens():
    def __init__(self, screen) -> None:
        self.__screen = screen
        self.__position_mouse = None

    def first_phase(self):
        points = 0
        scale = 0.7

        image = pygame.image.load('src/imgs/example_fase_one.png')
        background = pygame.transform.scale(image, (int(image.get_width() * scale), (int(image.get_height() * scale))))
        rect = background.get_rect()
        self.__screen.blit(background, rect)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        self.__game_over(points)

            pygame.display.update()

        pygame.quit()

    def __game_over(self, points):
        title = pygame.font.Font("src/fonts/font.ttf", 20).render("GameOver", True, COLORS["black"])
        punctuation = pygame.font.Font("src/fonts/font.ttf", 20).render("Pontuação", True, COLORS["black"])
        point = pygame.font.Font("src/fonts/font.ttf", 20).render(f"{points} Pontos", True, COLORS["black"])

        self.__screen.fill(COLORS["primary"])
        self.__screen.blit(title, (560, 50))
        self.__screen.blit(punctuation, (560, 200))
        self.__screen.blit(point, (560, 260))
        try_again = Button(pygame.image.load("src/imgs/background_buttom.png"), "Tentar Novamente", 640, 460, 1)
        menu = Button(pygame.image.load("src/imgs/background_buttom.png"), "Menu Principal", 640, 600, 1)

        try_again.update(self.__screen)
        menu.update(self.__screen)

        running = True
        while running:
            self.__position_mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if try_again.checkForInput(self.__position_mouse):
                        self.first_phase()
                # if menu.checkForInput(self.__position_mouse):

            pygame.display.update()

        pygame.quit()
