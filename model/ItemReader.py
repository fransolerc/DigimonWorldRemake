import pandas as pd
from constant import datatables
from item import Item
from utils import TextUtils


class ItemReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.items = []

    def read_items(self):
        try:
            df = pd.read_csv(self.file_path)

            required_columns = [
                'Name Text', 'Description', 'Digivolution', 'Type',
                'Color', 'Sorting Value', 'Weight', 'Energy',
                'Happiness', 'Discipline', 'Tiredness', 'Sickness',
                'Heal HP', 'Heal MP', 'Increase HP', 'Increase MP',
                'Increase Offense', 'Increase Defense', 'Increase Speed',
                'Increase Brains', 'Increase Lifetime', 'Price Money',
                'Merit Value'
            ]

            for column in required_columns:
                if column not in df.columns:
                    raise ValueError(f"Missing column in CSV: {column}")

            for _, row in df.iterrows():
                name = TextUtils.TextUtils.extract_text(row['Name Text'])
                description = TextUtils.TextUtils.extract_text(row['Description'])

                item = Item(
                    name=name,
                    description=description,
                    digivolution=row['Digivolution'],
                    item_type=row['Type'],
                    color=row['Color'],
                    sorting_value=row['Sorting Value'],
                    weight=row['Weight'],
                    energy=row['Energy'],
                    happiness=row['Happiness'],
                    discipline=row['Discipline'],
                    tiredness=row['Tiredness'],
                    sickness=row['Sickness'],
                    heal_hp=row['Heal HP'],
                    heal_mp=row['Heal MP'],
                    increase_hp=row['Increase HP'],
                    increase_mp=row['Increase MP'],
                    increase_offense=row['Increase Offense'],
                    increase_defense=row['Increase Defense'],
                    increase_speed=row['Increase Speed'],
                    increase_brains=row['Increase Brains'],
                    increase_lifetime=row['Increase Lifetime'],
                    price_money=row['Price Money'],
                    merit_value=row['Merit Value']
                )
                self.items.append(item)

        except FileNotFoundError:
            print(f"Error: El archivo {datatables.ITEM} no se encontró.")
        except pd.errors.EmptyDataError:
            print("Error: El archivo CSV está vacío.")
        except Exception as e:
            print(f"Error al leer el archivo CSV: {e}")

    def get_items(self):
        return self.items

    def get_item_by_index(self, index):
        if 0 <= index < len(self.items):
            return self.items[index]
        else:
            raise IndexError("Item Index Error.")

    def print_items(self):
        for item in self.items:
            print(f"Name: {item.name}")
            print(f"Description: {item.description}")
            print(f"Digivolution: {item.digivolution}")
            print(f"Type: {item.item_type}")
            print(f"Color: {item.color}")
            print(f"Sorting Value: {item.sorting_value}")
            print(f"Weight: {item.weight}")
            print(f"Energy: {item.energy}")
            print(f"Happiness: {item.happiness}")
            print(f"Discipline: {item.discipline}")
            print(f"Tiredness: {item.tiredness}")
            print(f"Sickness: {item.sickness}")
            print(f"Heal HP: {item.heal_hp}")
            print(f"Heal MP: {item.heal_mp}")
            print(f"Increase HP: {item.increase_hp}")
            print(f"Increase MP: {item.increase_mp}")
            print(f"Increase Offense: {item.increase_offense}")
            print(f"Increase Defense: {item.increase_defense}")
            print(f"Increase Speed: {item.increase_speed}")
            print(f"Increase Brains: {item.increase_brains}")
            print(f"Increase Lifetime: {item.increase_lifetime}")
            print(f"Price Money: {item.price_money}")
            print(f"Merit Value: {item.merit_value}")
            print("----------")


if __name__ == "__main__":
    item_reader = ItemReader('../assets/data/datatable/Item/Info.csv')
    item_reader.read_items()
    new_item = item_reader.get_item_by_index(3)
    print(new_item)
