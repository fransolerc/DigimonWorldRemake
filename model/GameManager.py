import json
import os


class GameDataManager:
    def __init__(self, save_file="savefile.json"):
        self.save_file = save_file
        self.game_data = {
            "Player": "",
            "Companion": ""
        }

    def save_game_data(self):
        """Guarda los datos del juego en un archivo JSON."""
        with open(self.save_file, 'w') as file:
            json.dump(self.game_data, file)
        print(f"Datos guardados en {self.save_file}")

    def load_game_data(self):
        """Carga los datos del juego desde un archivo JSON."""
        if os.path.exists(self.save_file):
            with open(self.save_file, 'r') as file:
                self.game_data = json.load(file)
            print(f"Datos cargados desde {self.save_file}")
        else:
            print(f"No se encontró el archivo de guardado {self.save_file}")

    def set_player_name(self, name):
        """Establece el nombre del jugador."""
        self.game_data["Player"] = name

    def set_companion_name(self, name):
        """Establece el nombre del compañero Digimon."""
        self.game_data["Companion"] = name

    def get_player_name(self):
        """Obtiene el nombre del jugador."""
        return self.game_data.get("Player", "")

    def get_companion_name(self):
        """Obtiene el nombre del compañero Digimon."""
        return self.game_data.get("Companion", "")
