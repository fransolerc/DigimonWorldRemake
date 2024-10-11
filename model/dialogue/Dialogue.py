from dataclasses import dataclass


@dataclass
class Dialogue:
    condition: str
    name: str
    text: str
    operator: str = ""
    if_value: any = None
    if_output: any = None
    jump_to_line: any = None
    switch: any = None
    boolean: any = None
    float_delay: float = 0.0
    give_items: any = None
    selection: any = None
    location: any = None
    rotation: any = None
    widget_position: any = None
    play_sound: any = None
    data_table: any = None

    def display(self):
        print(f"{self.name}: {self.text}")
