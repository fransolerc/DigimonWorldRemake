import mainMenu
from model.audioManager import AudioManager
from model.GameDataManager import GameDataManager

if __name__ == "__main__":
    audio_manager = AudioManager()
    game_data_manager = GameDataManager()
    mainMenu.main_menu()
