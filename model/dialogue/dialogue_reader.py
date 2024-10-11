import os
import pandas as pd
from constant import (
    ROW_CONDITION, ROW_NAME, ROW_TEXT, ROW_FLOAT, ROW_OPERATOR,
    ROW_IF_VALUE, ROW_IF_OUTPUT, ROW_JUMP_TO_LINE, ROW_SWITCH,
    ROW_BOOLEAN, ROW_GIVE_ITEMS, ROW_SELECTION, ROW_LOCATION,
    ROW_ROTATION, ROW_WIDGET_POSITION, ROW_PLAY_SOUND,
    ROW_DATA_TABLE
)
from model.game_data_manager import GameDataManager
from dialogue_processor import DialogueProcessor


class DialogueReader:
    def __init__(self, file_path, game_data_manager_object):
        self.file_path = file_path
        self.current_index = 0
        self.game_data_manager = game_data_manager_object
        self.processor = DialogueProcessor(self, self.game_data_manager)

    def read_dialogue_csv(self):
        if not os.path.exists(self.file_path):
            print(f"{self.file_path} does not exist.")
            return

        try:
            df = pd.read_csv(self.file_path)
            required_columns = self.get_required_columns()

            for column in required_columns:
                if column not in df.columns:
                    raise ValueError(f"Missing column in CSV: {column}")

            for _, row in df.iterrows():
                self.processor.process_dialogue(row)

        except (FileNotFoundError, ValueError) as e:
            print(f"Error reading file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    @staticmethod
    def get_required_columns():
        return [
            ROW_CONDITION, ROW_NAME, ROW_TEXT, ROW_FLOAT, ROW_OPERATOR,
            ROW_IF_VALUE, ROW_IF_OUTPUT, ROW_JUMP_TO_LINE, ROW_SWITCH,
            ROW_BOOLEAN, ROW_GIVE_ITEMS, ROW_SELECTION, ROW_LOCATION,
            ROW_ROTATION, ROW_WIDGET_POSITION, ROW_PLAY_SOUND, ROW_DATA_TABLE
        ]

    def get_next_dialogue(self):
        if self.current_index < self.read_dialogue_csv_length():
            try:
                df = pd.read_csv(self.file_path)
                dialogue_line = df.iloc[self.current_index]
                self.current_index += 1
                return dialogue_line
            except Exception as e:
                print(f"Error reading next dialogue: {e}")
                return None
        else:
            return None

    def jump_to_line(self, selected_line):
        if selected_line < self.read_dialogue_csv_length():
            try:
                df = pd.read_csv(self.file_path)
                dialogue_line = df.iloc[selected_line]
                return dialogue_line
            except Exception as e:
                print(f"Error reading next dialogue: {e}")
                return None
        else:
            return None

    def read_dialogue_csv_length(self):
        try:
            df = pd.read_csv(self.file_path)
            return len(df)
        except Exception as e:
            print(f"Error reading file: {e}")
            return 0


if __name__ == "__main__":
    game_data_manager = GameDataManager()
    dialogue_reader = DialogueReader("../../assets/data/datatable/Dialogue/Intro.csv", game_data_manager)
    dialogue_reader.read_dialogue_csv()
