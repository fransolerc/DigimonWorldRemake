import pygame
import sys

from model import colors, config

pygame.init()

screen = pygame.display.set_mode((config.screen_width, config.screen_height))
pygame.display.set_caption(config.game_title)

font = pygame.font.Font(config.font_type, config.font_size)

selected_option = 0

clock = pygame.time.Clock()


def start_new_game():
    print("Iniciando una nueva partida...")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(colors.BLACK)
        text = font.render("Nueva Partida Iniciada", True, colors.WHITE)
        text_rect = text.get_rect(center=(config.screen_width / 2, config.screen_height / 2))
        screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(config.FPS)
