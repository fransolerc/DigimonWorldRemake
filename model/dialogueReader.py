import csv
import os


class DialogueReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_dialogue_csv(self):
        if not os.path.exists(self.file_path):
            print(f"El archivo '{self.file_path}' no existe.")
            return

        with open(self.file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if 'Text' in row:
                    print(row['Text'])
                else:
                    print("La columna 'Text' no se encuentra en la fila:", row)
