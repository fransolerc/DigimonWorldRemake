import pygame

import constant
from constant import colors, config
from model.dialogue.dialogue_reader import DialogueReader
from main import AudioManager, GameDataManager

pygame.init()

audio_manager = AudioManager()
game_data_manager = GameDataManager()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption(config.GAME_TITLE)

font = pygame.font.Font(config.FONT_TYPE, config.FONT_SIZE_SMALL)
clock = pygame.time.Clock()


def start_new_game():
    intro_dialogue = DialogueReader(constant.datatables.DataTables.INTRO, game_data_manager)
    intro_dialogue.read_dialogue_csv()
    render_screen(intro_dialogue)

    running = True
    while running:
        handle_events(intro_dialogue)
        render_screen(intro_dialogue)

        pygame.display.flip()
        clock.tick(config.FPS)


def handle_events(intro_dialogue):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            handle_keydown_event(event, intro_dialogue)


def handle_keydown_event(event, intro_dialogue):
    if event.key == pygame.K_SPACE:
        audio_manager.play_button_open()
        if intro_dialogue.get_current_line() is not None:
            intro_dialogue.advance_line()


def render_screen(intro_dialogue):
    screen.fill(colors.BLACK)

    current_line = intro_dialogue.get_current_line()
    text_surface = font.render(current_line[1] if current_line and len(current_line) > 1 else "", True, colors.WHITE)

    screen.blit(text_surface, (50, 50))


if __name__ == "__main__":
    start_new_game()
