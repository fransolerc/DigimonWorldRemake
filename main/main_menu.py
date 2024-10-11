import pygame
import sys

from constant import resources, colors, config
from main import new_game
from model.audio_manager import AudioManager

pygame.init()
audio_manager = AudioManager()

background_image = pygame.transform.scale(resources.BACKGROUND_IMAGE, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption(config.GAME_TITLE)
font = pygame.font.Font(config.FONT_TYPE, config.FONT_SIZE_LARGE)

selected_option = 0
clock = pygame.time.Clock()

running = True


def draw_menu():
    screen.blit(background_image, (0, 0))

    for i, option in enumerate(config.MENU_OPTIONS):
        text_color = colors.YELLOW if i == selected_option else colors.WHITE
        text = font.render(option, True, text_color)
        text_rect = text.get_rect(center=(config.SCREEN_WIDTH / 2, config.SCREEN_HEIGHT / 2 + 180 + i * 50))
        screen.blit(text, text_rect)


def handle_keydown(event):
    global selected_option

    if event.key == pygame.K_DOWN:
        audio_manager.play_button_hover()
        selected_option = (selected_option + 1) % len(config.MENU_OPTIONS)
    elif event.key == pygame.K_UP:
        audio_manager.play_button_hover()
        selected_option = (selected_option - 1) % len(config.MENU_OPTIONS)
    elif event.key == pygame.K_RETURN:
        select_option()


def select_option():
    global running
    if selected_option == 0:
        running = False
        audio_manager.play_button_open()
        fade_to_black(1000)
        new_game.start_new_game()
    elif selected_option == 2:
        pygame.quit()
        sys.exit()


def fade_to_black(duration=1000):
    fade_surface = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    fade_surface.fill(colors.BLACK)

    alpha_step = 5
    alpha = 0

    while alpha < 255:
        alpha += alpha_step
        fade_surface.set_alpha(alpha)
        screen.blit(background_image, (0, 0))
        draw_menu()
        screen.blit(fade_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(int(duration / (255 / alpha_step)))


def main_menu():
    global selected_option, running
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                handle_keydown(event)

        draw_menu()
        pygame.display.flip()
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main_menu()
