import pygame

from game_info.game_stances import gameplay_stance, main_menu_stance, game_end_stance
from game_info.global_state import GlobalState

pygame.init()
clock = pygame.time.Clock()
clock.tick(60)


def main():
    while True:
        if GlobalState.game_state == 0:
            main_menu_stance()
        elif GlobalState.game_state == 1:
            gameplay_stance()
        elif GlobalState.game_state > 1:
            game_end_stance(GlobalState.game_state)


if __name__ == "__main__":
    main()
