import pygame
from constant.audio import UI_BUTTON_HOVER, UI_BUTTON_OPEN


class AudioManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AudioManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        pygame.mixer.init()
        self._initialized = True

    @staticmethod
    def play_button_hover():
        UI_BUTTON_HOVER.play()

    @staticmethod
    def play_button_open():
        UI_BUTTON_OPEN.play()
