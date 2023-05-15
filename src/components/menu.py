from components.button import Button
from screens.screens import Screens

import pygame


class Menu():
    def __init__(self, screen) -> None:
        self.__screen = screen
        self.__position_mouse = None

    def __update_image(self, buttons):
        for button in buttons:
            button.update(self.__screen)

    def display_menu(self):
        play = Button(pygame.image.load("src/imgs/background_buttom.png"), "Jogar", 640, 80, 0.7)
        instructions = Button(pygame.image.load("src/imgs/background_buttom.png"), "Instruções", 640, 200, 0.7)
        on_off = Button(pygame.image.load("src/imgs/background_buttom.png"), "Ligar/Desligar", 640, 320, 0.8)
        sound = Button(pygame.image.load("src/imgs/background_buttom.png"), "Som", 640, 440, 0.7)

        self.__update_image([play, instructions, on_off, sound])
        running = True

        while running:
            self.__position_mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play.checkForInput(self.__position_mouse):
                        Screens(self.__screen).first_phase()
                    if instructions.checkForInput(self.__position_mouse):
                        pass
                    if on_off.checkForInput(self.__position_mouse):
                        pass
                    if sound.checkForInput(self.__position_mouse):
                        pass

            pygame.display.update()

        pygame.quit()
