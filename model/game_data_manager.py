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
        with open(self.save_file, 'w') as file:
            json.dump(self.game_data, file)
        print(f"Datos guardados en {self.save_file}")

    def load_game_data(self):
        if os.path.exists(self.save_file):
            with open(self.save_file, 'r') as file:
                self.game_data = json.load(file)
            print(f"Datos cargados desde {self.save_file}")
        else:
            print(f"No se encontró el archivo de guardado {self.save_file}")

    def set_player_name(self, name):
        self.game_data["Player"] = name

    def set_partner_name(self, name):
        self.game_data["Partner"] = name

    def get_player_name(self):
        return self.game_data.get("Player", "")

    def get_partner_name(self):
        return self.game_data.get("Partner", "")
