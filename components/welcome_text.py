import pygame


class WelcomeText(pygame.sprite.Sprite):

    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.Surface([798, 150])
        self.rect = self.image.get_rect(topleft=(screen_width / 2 - 399, screen_height - 700))
        self.pos_x = screen_width / 2 - 399
        self.pos_y = screen_height - 700
        self.sprites = []
        self.sprites.append(pygame.image.load("visuals/welcome_button/welcome.png"))
        self.sprites.append(pygame.image.load("visuals/welcome_button/welcome1.png"))
        self.sprites.append(pygame.image.load("visuals/welcome_button/welcome2.png"))
        self.sprites.append(pygame.image.load("visuals/welcome_button/welcome3.png"))
        self.sprites.append(pygame.image.load("visuals/welcome_button/welcome4.png"))
        self.sprites.append(pygame.image.load("visuals/welcome_button/welcome5.png"))
        self.sprites.append(pygame.image.load("visuals/welcome_button/welcome6.png"))
        self.current_sprite = 0
        self.button_img = self.sprites[self.current_sprite]
        self.was_clicked = False

    def is_clicked(self):
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.was_clicked = True

    def update(self):
        if self.was_clicked:
            self.current_sprite += 0.10

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = int(len(self.sprites)-1)
            self.was_clicked = False

        self.button_img = self.sprites[int(self.current_sprite)]
