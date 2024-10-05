import csv
import os
import re
import time
from model.GameDataManager import GameDataManager


class DialogueReader:
    def __init__(self, file_path, game_data_manager_object):
        self.file_path = file_path
        self.dialogues = []
        self.current_index = 0
        self.delay_value = 0.0
        self.game_data_manager = game_data_manager_object

    def read_dialogue_csv(self):
        if not os.path.exists(self.file_path):
            print(f"El archivo '{self.file_path}' no existe.")
            return

        try:
            with open(self.file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    condition = row.get('Condition', '').strip()
                    self.delays = 0.0

                    if condition == 'ShowTextBox':
                        if 'Text' in row and row['Text'].strip():
                            npc_name = row.get('Name', '').strip()
                            text = row['Text']
                            match = re.search(r'NSLOCTEXT\(\s*"[^"]*"\s*,\s*"[^"]*"\s*,\s*"([^"]*)"\s*\)', text)
                            if match:
                                extracted_text = match.group(1)
                                extracted_text = extracted_text.replace("\\'", "'")
                                processed_text = self.replace_variables(extracted_text)

                                print(f"{npc_name}: {processed_text}")

                                self.dialogues.append((npc_name, processed_text.strip()))

                    if condition == 'Delay':
                        self.delay_value = float(row['Float'])
                        time.sleep(self.delay_value)

        except Exception as e:
            print(f"Error al leer el archivo: {e}")

    def replace_variables(self, text):
        player_name = self.game_data_manager.get_player_name() or "Player"
        partner_name = self.game_data_manager.get_partner_name() or "Partner"

        text = text.replace("{Player}", player_name)
        text = text.replace("{Partner}", partner_name)
        return text

    def get_next_dialogue(self):
        if self.current_index < len(self.dialogues):
            dialogue_line = self.dialogues[self.current_index]
            self.current_index += 1
            return dialogue_line
        else:
            return None

    def advance_line(self):
        if self.current_index < len(self.dialogues):
            self.current_index += 1
        else:
            self.current_index = None

    def get_current_line(self):
        if self.current_index is not None and self.current_index < len(self.dialogues):
            return self.dialogues[self.current_index]
        return None


if __name__ == "__main__":
    game_data_manager = GameDataManager()

    dialogue_reader = DialogueReader("../assets/data/datatable/Dialogue/Intro2.csv", game_data_manager)
    dialogue_reader.read_dialogue_csv()

    while True:
        input("Presiona Enter para continuar...")
        dialogue = dialogue_reader.get_next_dialogue()
        if dialogue is not None:
            print(dialogue)
        else:
            print("No hay más diálogos.")
            break
