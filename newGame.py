import pygame
from constant import colors, config, dialogue
from model.dialogueReader import DialogueReader
from main import AudioManager, GameDataManager

pygame.init()

audio_manager = AudioManager()
game_data_manager = GameDataManager()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption(config.GAME_TITLE)

font = pygame.font.Font(config.FONT_TYPE, config.FONT_SIZE_SMALL)

clock = pygame.time.Clock()


def start_new_game():
    intro_dialogue = DialogueReader(dialogue.INTRO, game_data_manager)
    intro_dialogue.read_dialogue_csv()

    screen.fill(colors.BLACK)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    audio_manager.play_button_open()
                    if intro_dialogue.get_current_line() is not None:
                        intro_dialogue.advance_line()
                    else:
                        running = False

        screen.fill(colors.BLACK)

        current_line = intro_dialogue.get_current_line()

        if current_line is not None and len(current_line) > 1:
            text_surface = font.render(current_line[1] or "", True, colors.WHITE)
        else:
            text_surface = font.render("", True, colors.WHITE)

        screen.blit(text_surface, (50, 50))

        pygame.display.flip()
        clock.tick(config.FPS)


if __name__ == "__main__":
    start_new_game()
