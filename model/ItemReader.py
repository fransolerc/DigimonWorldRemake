import pandas as pd
from constant import datatables
from item import Item
from utils import TextUtils


class ItemReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.items_list = []
        self.read_items()

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
                self.items_list.append(item)

        except FileNotFoundError:
            print(f"Error: {datatables.ITEM} not exists.")
        except pd.errors.EmptyDataError:
            print("Error: CSV Empty.")
        except Exception as e:
            print(f"Error al leer el archivo CSV: {e}")

    def get_item_by_index(self, index):
        if 0 <= index < len(self.items_list):
            return self.items_list[index]
        else:
            raise IndexError("Item Index Error.")

    def print_items(self):
        for item in self.items_list:
            print(f"Name: {item.name}")
            print(f"Description: {item.description}")
            print(f"Type: {item.item_type}")
            print("---------------------------------------------------------------------------")


if __name__ == "__main__":
    item_reader = ItemReader('../assets/data/datatable/Item/Info.csv')
    item_reader.print_items()
