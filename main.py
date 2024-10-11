import main_menu
from model.audio_manager import AudioManager
from model.game_data_manager import GameDataManager

if __name__ == "__main__":
    audio_manager = AudioManager()
    game_data_manager = GameDataManager()
    mainMenu.main_menu()
