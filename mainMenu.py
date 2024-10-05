import pygame
import sys

from constant import resources, colors, config
from main import AudioManager
import newGame

pygame.init()

audio_manager = AudioManager()

background_image = pygame.transform.scale(resources.BACKGROUND_IMAGE, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption(config.GAME_TITLE)

font = pygame.font.Font(config.FONT_TYPE, config.FONT_SIZE_LARGE)

selected_option = 0

clock = pygame.time.Clock()


def draw_menu():
    screen.blit(background_image, (0, 0))

    for i, option in enumerate(config.MENU_OPTIONS):
        if i == selected_option:
            text_color = colors.YELLOW
        else:
            text_color = colors.WHITE

        text = font.render(option, True, text_color)
        text_rect = text.get_rect(center=(config.SCREEN_WIDTH / 2, config.SCREEN_HEIGHT / 2 + 200 + i * 100))
        screen.blit(text, text_rect)


def main_menu():
    global selected_option
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    audio_manager.play_button_hover()
                    selected_option = (selected_option + 1) % len(config.MENU_OPTIONS)
                if event.key == pygame.K_UP:
                    audio_manager.play_button_hover()
                    selected_option = (selected_option - 1) % len(config.MENU_OPTIONS)
                if event.key == pygame.K_RETURN:
                    if selected_option == 0:
                        audio_manager.play_button_open()
                        newGame.start_new_game()
                        print("New Game")
                    elif selected_option == 1:
                        audio_manager.play_button_open()
                        print("Continue Game")

        draw_menu()

        pygame.display.flip()

        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()
