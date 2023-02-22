import pygame
import sys
import time

from components.board import Board
from components.start_button import StartButton
from components.welcome_text import WelcomeText
from game_info.global_state import GlobalState

screen = pygame.display.set_mode((1500, 800))


def main_menu_stance():
    start_button = StartButton(1500, 800)
    welcome_text = WelcomeText(1500, 800)

    while True:
        screen.blit(pygame.image.load("visuals/background.png"), (0, 0))
        event_list = pygame.event.get()

        for event in event_list:
            if event.type == pygame.QUIT:
                sys.exit(0)

        if start_button.is_clicked():
            welcome_text.was_clicked = True

        welcome_text.update()
        if start_button.update() == -1:
            GlobalState.game_state = 1
            return

        screen.blit(start_button.button_img, (start_button.pos_x, start_button.pos_y))
        screen.blit(welcome_text.button_img, (welcome_text.pos_x, welcome_text.pos_y))
        pygame.display.flip()


def gameplay_stance():
    new_board = Board()
    active_cards = 0
    moves_counter = 0
    active_list_indexes = []
    while True:
        screen.blit(pygame.image.load("visuals/background.png"), (0, 0))
        event_list = pygame.event.get()

        for event in event_list:
            if event.type == pygame.QUIT:
                sys.exit(0)

        if active_cards == 2:
            if new_board.get_card(active_list_indexes[len(active_list_indexes) - 1]).get_value() == new_board.get_card(
                    active_list_indexes[len(active_list_indexes) - 2]).get_value():
                active_cards = 0
            else:
                active_cards = 0
                new_board.get_card(active_list_indexes[len(active_list_indexes) - 1]).able_to_flop = True
                new_board.get_card(active_list_indexes[len(active_list_indexes) - 1]).change_status()
                new_board.get_card(active_list_indexes[len(active_list_indexes) - 2]).able_to_flop = True
                new_board.get_card(active_list_indexes[len(active_list_indexes) - 2]).change_status()
                active_list_indexes.pop(len(active_list_indexes) - 1)
                active_list_indexes.pop(len(active_list_indexes) - 1)
                time.sleep(1)

        for i in range(4):
            for j in range(10):
                if new_board.get_card((i * 10 + j)).update(event_list) and new_board.get_card(
                        (i * 10 + j)).able_to_flop:
                    moves_counter += 1
                    active_cards += 1
                    active_list_indexes.append((i * 10 + j))
                    new_board.get_card(i * 10 + j).able_to_flop = False

        for i in range(4):
            for j in range(10):
                new_board.get_card(i * 10 + j).draw_img()
                screen.blit(new_board.get_card((i * 10 + j)).draw_card(),
                            (new_board.get_card((i * 10 + j)).pos_x, new_board.get_card((i * 10 + j)).pos_y))

        pygame.display.flip()
        if len(active_list_indexes) == 40:
            GlobalState.game_state = moves_counter
            return


def game_end_stance(score):
    end_text = pygame.font.SysFont("monospace", 45)

    while True:
        screen.blit(pygame.image.load("visuals/background.png"), (0, 0))
        event_list = pygame.event.get()

        for event in event_list:
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                GlobalState.game_state = 1
                return

        score_text = "Congratulations! You've won in " + str(score) + " moves"
        play_again = "Press any key to play again"
        text = end_text.render(score_text, True, (255, 255, 255))
        screen.blit(text, (250, 250))
        text = end_text.render(play_again, True, (255, 255, 255))
        screen.blit(text, (350, 400))
        pygame.display.flip()
