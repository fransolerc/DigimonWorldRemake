import time

from model.dialogue import Dialogue
from utils.text_utils import TextUtils
from constant import (
    CONDITION_SHOW_TEXT_BOX,
    CONDITION_DELAY,
    CONDITION_SET_SELECTION, ROW_IF_VALUE, ROW_OPERATOR, ROW_TEXT, ROW_NAME, ROW_CONDITION, ROW_IF_OUTPUT,
    ROW_JUMP_TO_LINE, ROW_SWITCH, ROW_BOOLEAN, ROW_FLOAT, ROW_GIVE_ITEMS, ROW_SELECTION, ROW_LOCATION, ROW_ROTATION,
    ROW_WIDGET_POSITION, ROW_PLAY_SOUND, ROW_DATA_TABLE
)


class DialogueProcessor:
    def __init__(self, dialogue_reader, game_data_manager):
        self.game_data_manager = game_data_manager
        self.dialogue_reader = dialogue_reader

    def process_dialogue(self, row):
        try:
            dialogue = self.create_dialogue(row)

            if dialogue.condition == CONDITION_SHOW_TEXT_BOX:
                self.process_show_text_box(dialogue.name, dialogue.text)
            elif dialogue.condition == CONDITION_DELAY:
                self.process_delay(dialogue.float_delay)
            elif dialogue.condition == CONDITION_SET_SELECTION:
                self.process_set_selection(dialogue)

        except ValueError as e:
            print(f"Error processing dialogue: {e}")

    @staticmethod
    def create_dialogue(row):
        return Dialogue(
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

    def process_show_text_box(self, name, text):
        extracted_text = TextUtils.extract_text(text)

        if extracted_text:
            processed_text = self.replace_variables(extracted_text)
            print(f"{name}: {processed_text}")

    @staticmethod
    def process_delay(delay_value):
        time.sleep(delay_value)

    def process_set_selection(self, dialogue):
        selection_text = dialogue.selection
        selection_options = TextUtils.extract_selection_options(selection_text)

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

    def replace_variables(self, text):
        player_name = self.game_data_manager.get_player_name() or "Player"
        partner_name = self.game_data_manager.get_partner_name() or "Partner"

        text = text.replace("{Player}", player_name)
        text = text.replace("{Partner}", partner_name)
        return text

    def jump_to_line(self, selected_line):
        self.dialogue_reader.current_index = selected_line - 1
        self.dialogue_reader.jump_to_line(self.dialogue_reader.current_index)
