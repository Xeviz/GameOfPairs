import pygame


class StartButton(pygame.sprite.Sprite):

    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.Surface([316, 96])
        self.rect = self.image.get_rect(topleft=(screen_width / 2 - 158, screen_height / 2 - 48))
        self.pos_x = screen_width / 2 - 158
        self.pos_y = screen_height / 2 - 48
        self.sprites = []
        self.sprites.append(pygame.image.load("visuals/start_button/start_button.png"))
        self.sprites.append(pygame.image.load("visuals/start_button/start_button1.png"))
        self.sprites.append(pygame.image.load("visuals/start_button/start_button2.png"))
        self.sprites.append(pygame.image.load("visuals/start_button/start_button3.png"))
        self.sprites.append(pygame.image.load("visuals/start_button/start_button4.png"))
        self.sprites.append(pygame.image.load("visuals/start_button/start_button5.png"))
        self.sprites.append(pygame.image.load("visuals/start_button/start_button6.png"))
        self.current_sprite = 0
        self.button_img = self.sprites[self.current_sprite]
        self.was_clicked = False

    def is_clicked(self):
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.was_clicked = True
            return True

    def update(self):
        if self.was_clicked:
            self.current_sprite += 0.10
        if self.current_sprite >= len(self.sprites):
            return -1

        self.button_img = self.sprites[int(self.current_sprite)]
