import pygame
import csv  # Asegúrate de importar csv
from model import colors, config
from model.dialogueReader import DialogueReader

pygame.init()

screen = pygame.display.set_mode((config.screen_width, config.screen_height))
pygame.display.set_caption(config.game_title)

font = pygame.font.Font(config.font_type, config.font_size)

selected_option = 0
clock = pygame.time.Clock()

dialogue_reader = DialogueReader("assets/data/datatable/Dialogue/Intro.csv")
dialogue_lines = []  # Almacena las líneas del diálogo


# Leer el diálogo y almacenar las líneas en una lista
def load_dialogue():
    with open(dialogue_reader.file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if 'Text' in row:
                dialogue_lines.append(row['Text'])
                print("Texto cargado:", row['Text'])


def start_new_game():
    load_dialogue()
    running = True
    index = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    index += 1
                    if index >= len(dialogue_lines):
                        index = 0

        screen.fill(colors.BLACK)

        if index < len(dialogue_lines):
            text = font.render(dialogue_lines[index], True, colors.WHITE)
            text_rect = text.get_rect(center=(config.screen_width / 2, config.screen_height / 2))
            screen.blit(text, text_rect)
        else:
            print("Índice fuera de rango, no se puede mostrar texto.")

        pygame.display.flip()
        clock.tick(config.FPS)


if __name__ == "__main__":
    start_new_game()
