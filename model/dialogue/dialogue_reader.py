import os
import time
import pandas as pd

from constant import ROW_CONDITION, ROW_NAME, ROW_TEXT, ROW_FLOAT, ROW_OPERATOR, ROW_IF_VALUE, ROW_IF_OUTPUT, \
    ROW_JUMP_TO_LINE, ROW_SWITCH, ROW_BOOLEAN, ROW_GIVE_ITEMS, ROW_SELECTION, ROW_LOCATION, ROW_ROTATION, \
    ROW_WIDGET_POSITION, ROW_PLAY_SOUND, ROW_DATA_TABLE, CONDITION_SHOW_TEXT_BOX, CONDITION_DELAY, \
    CONDITION_SET_SELECTION
from model.game_data_manager import GameDataManager
from model.dialogue import Dialogue
from utils import text_utils


class DialogueReader:
    def __init__(self, file_path, game_data_manager_object):
        self.file_path = file_path
        self.current_index = 0
        self.game_data_manager = game_data_manager_object

    def read_dialogue_csv(self):
        if not os.path.exists(self.file_path):
            print(f"{self.file_path} does not exist.")
            return

        try:
            df = pd.read_csv(self.file_path)

            required_columns = [
                ROW_CONDITION,
                ROW_NAME,
                ROW_TEXT,
                ROW_FLOAT,
                ROW_OPERATOR,
                ROW_IF_VALUE,
                ROW_IF_OUTPUT,
                ROW_JUMP_TO_LINE,
                ROW_SWITCH,
                ROW_BOOLEAN,
                ROW_GIVE_ITEMS,
                ROW_SELECTION,
                ROW_LOCATION,
                ROW_ROTATION,
                ROW_WIDGET_POSITION,
                ROW_PLAY_SOUND,
                ROW_DATA_TABLE
            ]

            for column in required_columns:
                if column not in df.columns:
                    raise ValueError(f"Missing column in CSV: {column}")

            for _, row in df.iterrows():
                self.process_dialogue(row)

        except (FileNotFoundError, ValueError) as e:
            print(f"Error reading file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def process_dialogue(self, row):
        try:
            dialogue = Dialogue(
                condition=row[ROW_CONDITION].strip(),
                name=row.get(ROW_NAME, ''),
                text=row.get(ROW_TEXT, ''),
                operator=row.get(ROW_OPERATOR, ''),
                if_value=row.get(ROW_IF_VALUE, ''),
                if_output=row.get(ROW_IF_OUTPUT, ''),
                jump_to_line=int(row.get(ROW_JUMP_TO_LINE, 0)),
                switch=row.get(ROW_SWITCH, ''),
                boolean=bool(row.get(ROW_BOOLEAN, False)),
                float_delay=float(row.get(ROW_FLOAT, 0.0)),
                give_items=row.get(ROW_GIVE_ITEMS, ''),
                selection=row.get(ROW_SELECTION, ''),
                location=row.get(ROW_LOCATION, ''),
                rotation=row.get(ROW_ROTATION, ''),
                widget_position=row.get(ROW_WIDGET_POSITION, ''),
                play_sound=row.get(ROW_PLAY_SOUND, ''),
                data_table=row.get(ROW_DATA_TABLE, '')
            )

            if dialogue.condition == CONDITION_SHOW_TEXT_BOX:
                self.process_show_text_box(dialogue.name, dialogue.text)
            elif dialogue.condition == CONDITION_DELAY:
                self.process_delay(dialogue.float_delay)
            elif dialogue.condition == CONDITION_SET_SELECTION:
                self.process_set_selection(dialogue)

        except ValueError as e:
            print(f"Error processing dialogue: {e}")

    def process_show_text_box(self, name, text):
        extracted_text = text_utils.TextUtils.extract_text(text)

        if extracted_text:
            processed_text = self.replace_variables(extracted_text)
            print(f"{name}: {processed_text}")

    @staticmethod
    def process_delay(delay_value):
        time.sleep(delay_value)

    def process_set_selection(self, dialogue):

        selection_text = dialogue.selection

        selection_options = text_utils.TextUtils.extract_selection_options(selection_text)

        print("Please make a selection:")
        for i, (line, option_text) in enumerate(selection_options, start=1):
            print(f"{i}. {option_text}")

        while True:
            try:
                user_choice = int(input("Enter your choice (number): ")) - 1
                if 0 <= user_choice < len(selection_options):
                    selected_line = selection_options[user_choice][0]
                    break
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a valid number.")

        print(f"Jumping to line {selected_line}")
        self.jump_to_line(selected_line)

    def jump_to_line(self, line_number):
        if 0 <= line_number < self.read_dialogue_csv_length():
            self.current_index = line_number - 1
        else:
            print(f"Line number {line_number} is out of range.")

    def replace_variables(self, text):
        player_name = self.game_data_manager.get_player_name() or "Player"
        partner_name = self.game_data_manager.get_partner_name() or "Partner"

        text = text.replace("{Player}", player_name)
        text = text.replace("{Partner}", partner_name)
        return text

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

    def advance_line(self):
        if self.current_index < self.read_dialogue_csv_length():
            self.current_index += 1
        else:
            self.current_index = None

    def get_current_line(self):
        if self.current_index is not None and self.current_index < self.read_dialogue_csv_length():
            try:
                df = pd.read_csv(self.file_path)
                current_row = df.iloc[self.current_index]
                return current_row
            except Exception as e:
                print(f"Error reading current line: {e}")
                return None
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
