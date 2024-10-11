class DataTables:
    # Rutas de los archivos CSV
    INTRO = 'assets/data/datatable/dialogue/Intro.csv'
    ITEM = 'assets/data/datatable/Item/Info.csv'
    DIGIMON_INFO = 'assets/data/datatable/Digimon/Info.csv'

    # Nombres de las columnas
    ROW_CONDITION = 'Condition'
    ROW_NAME = 'Name'
    ROW_TEXT = 'Text'
    ROW_FLOAT = 'Float'
    ROW_OPERATOR = 'Operator'
    ROW_IF_VALUE = 'If Value'
    ROW_IF_OUTPUT = 'If Output'
    ROW_JUMP_TO_LINE = 'Jump To Line'
    ROW_SWITCH = 'Switch'
    ROW_BOOLEAN = 'Boolean'
    ROW_GIVE_ITEMS = 'Give Items'
    ROW_SELECTION = 'Selection'
    ROW_LOCATION = 'Location'
    ROW_ROTATION = 'Rotation'
    ROW_WIDGET_POSITION = 'Widget Position'
    ROW_PLAY_SOUND = 'Play Sound'
    ROW_DATA_TABLE = 'DataTable'

    # Condiciones
    CONDITION_SHOW_TEXT_BOX = 'ShowTextBox'
    CONDITION_DELAY = 'Delay'
    CONDITION_SET_SELECTION = 'set Selection'

    def get_required_columns(self):
        return [
            self.ROW_CONDITION, self.ROW_NAME, self.ROW_TEXT, self.ROW_FLOAT, self.ROW_OPERATOR,
            self.ROW_IF_VALUE, self.ROW_IF_OUTPUT, self.ROW_JUMP_TO_LINE, self.ROW_SWITCH,
            self.ROW_BOOLEAN, self.ROW_GIVE_ITEMS, self.ROW_SELECTION, self.ROW_LOCATION,
            self.ROW_ROTATION, self.ROW_WIDGET_POSITION, self.ROW_PLAY_SOUND, self.ROW_DATA_TABLE
        ]
