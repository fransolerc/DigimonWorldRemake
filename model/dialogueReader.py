import os
import time
import pandas as pd

from model.GameDataManager import GameDataManager
from utils import TextUtils


class DialogueReader:
    def __init__(self, file_path, game_data_manager_object):
        self.file_path = file_path
        self.dialogues = []
        self.current_index = 0
        self.delay_value = 0.0
        self.game_data_manager = game_data_manager_object

    def read_dialogue_csv(self):
        if not os.path.exists(self.file_path):
            print(f"{self.file_path}' not exists.")
            return

        try:
            df = pd.read_csv(self.file_path)

            required_columns = ['Condition', 'Name', 'Text', 'Float']
            for column in required_columns:
                if column not in df.columns:
                    raise ValueError(f"Missing column in CSV: {column}")

            for _, row in df.iterrows():
                self.process_dialogue(row)

        except Exception as e:
            print(f"Error reading file: {e}")

    def process_dialogue(self, row):
        condition = row['Condition'].strip()
        if condition == 'ShowTextBox':
            self.process_show_text_box(row)
        elif condition == 'Delay':
            self.process_delay(row)

    def process_show_text_box(self, row):
        if 'Text' in row and row['Text'].strip():
            npc_name = row.get('Name', '').strip()
            text = row['Text']

            extracted_text = TextUtils.TextUtils.extract_text(text)
            if extracted_text:
                processed_text = self.replace_variables(extracted_text)
                print(f"{npc_name}: {processed_text}")
                self.dialogues.append((npc_name, processed_text.strip()))

    @staticmethod
    def process_delay(row):
        delay_value = float(row['Float'])
        time.sleep(delay_value)

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
        input("Press Enter:")
        dialogue = dialogue_reader.get_next_dialogue()
        if dialogue is not None:
            print(dialogue)
        else:
            print("No more dialogs.")
            break
