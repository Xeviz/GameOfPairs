import pygame.sprite


class Card(pygame.sprite.Sprite):

    def __init__(self, value, pos_x, pos_y):
        super().__init__()
        front_path = 'visuals/card_images/card' + str(value) + '.png'
        self.image = pygame.Surface([126, 178])
        self.rect = self.image.get_rect(topleft=(pos_x, pos_y))
        self.cover_img = pygame.image.load('visuals/card_images/card_back.png')
        self.front_img = pygame.image.load(front_path)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.value = value
        self.status = 0
        self.able_to_flop = True

    def change_status(self):
        if self.status == 0:
            self.status = 1
        else:
            self.status = 0

    def get_value(self):
        return self.value

    def update(self, event_list):

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    if self.able_to_flop:
                        self.change_status()
                    return True
            return False

    def draw_card(self):
        if self.status == 1:
            return self.get_front()
        else:
            return self.get_cover()

    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

    def get_front(self):
        return self.front_img

    def get_cover(self):
        return self.cover_img

    def draw_img(self):
        pygame.draw.rect(self.image, (255, 255, 255), pygame.Rect(self.pos_x, self.pos_y, 126, 178))




