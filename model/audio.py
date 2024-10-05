import pygame


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
        self.ui_button_hover = pygame.mixer.Sound('assets/audio/UI_Button_Hover.WAV')
        self.ui_button_open = pygame.mixer.Sound('assets/audio/UI_Button_Open.WAV')
        self._initialized = True

    def play_button_hover(self):
        self.ui_button_hover.play()

    def play_button_open(self):
        self.ui_button_open.play()
