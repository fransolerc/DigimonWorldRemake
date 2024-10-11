import pandas as pd

from constant import DataTables
from constant.item import ItemConstants
from item import Item
from utils import text_utils


class ItemReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.items_list = []
        self.read_items()

    def read_items(self):
        try:
            df = pd.read_csv(self.file_path)

            required_columns = [
                ItemConstants.NAME_TEXT, ItemConstants.DESCRIPTION, ItemConstants.DIGIVOLUTION,
                ItemConstants.ITEM_TYPE, ItemConstants.COLOR, ItemConstants.SORTING_VALUE,
                ItemConstants.WEIGHT, ItemConstants.ENERGY, ItemConstants.HAPPINESS,
                ItemConstants.DISCIPLINE, ItemConstants.TIREDNESS, ItemConstants.SICKNESS,
                ItemConstants.HEAL_HP, ItemConstants.HEAL_MP, ItemConstants.INCREASE_HP,
                ItemConstants.INCREASE_MP, ItemConstants.INCREASE_OFFENSE,
                ItemConstants.INCREASE_DEFENSE, ItemConstants.INCREASE_SPEED,
                ItemConstants.INCREASE_BRAINS, ItemConstants.INCREASE_LIFETIME,
                ItemConstants.PRICE_MONEY, ItemConstants.MERIT_VALUE
            ]

            for column in required_columns:
                if column not in df.columns:
                    raise ValueError(f"Missing column in CSV: {column}")

            for _, row in df.iterrows():
                name = text_utils.TextUtils.extract_text(row[ItemConstants.NAME_TEXT])
                description = text_utils.TextUtils.extract_text(row[ItemConstants.DESCRIPTION])

                item = Item(
                    name=name,
                    description=description,
                    digivolution=row[ItemConstants.DIGIVOLUTION],
                    item_type=row[ItemConstants.ITEM_TYPE],
                    color=row[ItemConstants.COLOR],
                    sorting_value=row[ItemConstants.SORTING_VALUE],
                    weight=row[ItemConstants.WEIGHT],
                    energy=row[ItemConstants.ENERGY],
                    happiness=row[ItemConstants.HAPPINESS],
                    discipline=row[ItemConstants.DISCIPLINE],
                    tiredness=row[ItemConstants.TIREDNESS],
                    sickness=row[ItemConstants.SICKNESS],
                    heal_hp=row[ItemConstants.HEAL_HP],
                    heal_mp=row[ItemConstants.HEAL_MP],
                    increase_hp=row[ItemConstants.INCREASE_HP],
                    increase_mp=row[ItemConstants.INCREASE_MP],
                    increase_offense=row[ItemConstants.INCREASE_OFFENSE],
                    increase_defense=row[ItemConstants.INCREASE_DEFENSE],
                    increase_speed=row[ItemConstants.INCREASE_SPEED],
                    increase_brains=row[ItemConstants.INCREASE_BRAINS],
                    increase_lifetime=row[ItemConstants.INCREASE_LIFETIME],
                    price_money=row[ItemConstants.PRICE_MONEY],
                    merit_value=row[ItemConstants.MERIT_VALUE]
                )
                self.items_list.append(item)

        except FileNotFoundError:
            print(f"Error: {DataTables.ITEM} not exists.")
        except pd.errors.EmptyDataError:
            print("Error: CSV Empty.")
        except Exception as e:
            print(f"Error reading CSV: {e}")

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
    item_reader = ItemReader('../../assets/data/datatable/Item/Info.csv')
    item_reader.print_items()
