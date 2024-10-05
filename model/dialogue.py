class Dialogue:
    def __init__(self,
                 condition,
                 name,
                 text,
                 operator,
                 if_value,
                 if_output,
                 jump_to_line,
                 switch,
                 boolean,
                 float_delay,
                 give_items,
                 selection,
                 location,
                 rotation, 
                 widget_position,
                 play_sound,
                 data_table):
        self.condition = condition
        self.name = name
        self.text = text
        self.operator = operator
        self.if_value = if_value
        self.if_output = if_output
        self.jump_to_line = jump_to_line
        self.switch = switch
        self.boolean = boolean
        self.float_delay = float_delay
        self.give_items = give_items
        self.selection = selection
        self.location = location
        self.rotation = rotation
        self.widget_position = widget_position
        self.play_sound = play_sound
        self.data_table = data_table

    def display(self):
        print(f"{self.name}: {self.text}")
