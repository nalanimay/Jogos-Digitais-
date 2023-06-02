import pygame
from pygame.sprite import Sprite


class Character(Sprite):
    def __init__(self, screen) -> None:
        super().__init__()
        self.life = 3
        self.points = 0
        self.__walking = False
        self.__sprite = pygame.image.load("src/imgs/manPlayer.png")
        self.__sprite_list = []
        for index in range(4):
            character_image = self.__sprite.subsurface((index * 57.25, 85), (57.25, 73))
            character_image = pygame.transform.scale(character_image, (int(character_image.get_width() * 1.2), (int(character_image.get_height() * 1.2))))
            self.__sprite_list.append(character_image)

        self.index_initial_character = 0
        self.image = self.__sprite_list[self.index_initial_character]
        self.rect = self.image.get_rect()
        self.rect.center = (80, 720 - 80)

    def to_walk(self):
        self.__walking = True
        if self.index_initial_character > 2:
            self.index_initial_character = 0
        self.index_initial_character += 1

    def animate(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.to_walk()
            self.rect.x -= 4.5
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.to_walk()
            self.rect.x += 4.5

    def update(self):
        if self.__walking is True:
            self.to_walk()
            self.image = self.__sprite_list[int(self.index_initial_character)]
            self.__walking = False
