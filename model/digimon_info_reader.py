import pandas as pd
from model.digimon_info import DigimonInfo


class DigimonInfoReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.digimon_list = []
        self.read_digimons()

    def read_digimons(self):
        try:
            df = pd.read_csv(self.file_path)

            for _, row in df.iterrows():
                digimon_info = DigimonInfo(
                    text_normal=row["Name Text Normal"],
                    text_romanized=row["Name Text Romanized"],
                    favorite_food=row["Favorite Food"],
                    level=row["Level"],
                    type=row["Type"],
                    speciality_1=row["Speciality #1"],
                    speciality_2=row["Speciality #2"],
                    speciality_3=row["Speciality #3"],
                    sleep_time=row["Sleep Time"],
                    training_preference=row["Training Preference"],
                    sprite=row["Sprite"],
                    preferred_map_id=row["Prefered Map ID"],
                    default_weight=row["Default Weight"],
                    energy_capacity=row["Energy Capacity"],
                    energy_threshold=row["Energy Threshold"],
                    energy_usage=row["Energy Usage"],
                    poop_size=row["Poop Size"],
                    poop_timer=row["Poop Timer"],
                    height=row["Height"],
                    ai_partner_distance=row["AI Partner Distance"],
                    footstep_sound=row["Footstep Sound"],
                    eat_sound=row["Eat Sound"],
                    attack_sound=row["Attack Sound"],
                    glad_sound=row["Glad Sound"],
                    down_sound=row["Down Sound"],
                    feeding_time=[row[f"Feeding Time #{i + 1}"] for i in range(8)],
                    enabled_techniques=[int(row[f"Enabled Technique #{i + 1}"]) for i in range(16)],
                    default_technique=int(row["Default Technique"]),
                    finisher_index=int(row["Finisher Index"]),
                    stats_gain_hp=row["Statsgain - HP"],
                    stats_gain_mp=row["Statsgain - MP"],
                    stats_gain_offense=row["Statsgain - Offense"],
                    stats_gain_defense=row["Statsgain - Defense"],
                    stats_gain_speed=row["Statsgain - Speed"],
                    stats_gain_brains=row["Statsgain - Brains"],
                    digivolution_requirement_bonus=row["Digivolution Requirement - Bonus"],
                    digivolution_requirement_hp=int(row["Digivolution Requirement - HP"]),
                    digivolution_requirement_mp=int(row["Digivolution Requirement - MP"]),
                    digivolution_requirement_offense=int(row["Digivolution Requirement - Offense"]),
                    digivolution_requirement_defense=int(row["Digivolution Requirement - Defense"]),
                    digivolution_requirement_speed=int(row["Digivolution Requirement - Speed"]),
                    digivolution_requirement_brains=int(row["Digivolution Requirement - Brains"]),
                    digivolution_requirement_care_mistakes=int(row["Digivolution Requirement - Care Mistakes"]),
                    digivolution_requirement_weight=int(row["Digivolution Requirement - Weight"]),
                    digivolution_requirement_happiness=int(row["Digivolution Requirement - Happiness"]),
                    digivolution_requirement_discipline=int(row["Digivolution Requirement - Discipline"]),
                    digivolution_requirement_battles_won=int(row["Digivolution Requirement - Battles Won"]),
                    digivolution_requirement_techniques=int(row["Digivolution Requirement - Techniques"]),
                    digivolution_requirement_max_battles=int(row["Digivolution Requirement - Max Battles"]),
                    digivolution_requirement_max_care_mistakes=int(row["Digivolution Requirement - Max Care Mistakes"]),
                    digivolution_from=[row[f"Digivoluton - From #{i + 1}"] for i in range(5)],
                    digivolution_to=[row[f"Digivoluton - To #{i + 1}"] for i in range(6)],
                )
                self.digimon_list.append(digimon_info)

        except FileNotFoundError:
            print(f"Error: {self.file_path} not found.")
        except pd.errors.EmptyDataError:
            print(f"Error: CSV {self.file_path} is empty.")
        except Exception as exception:
            print(f"Error reading CSV file: {exception}")

    def get_digimon_by_index(self, index):
        if 0 <= index < len(self.digimon_list):
            return self.digimon_list[index]
        else:
            raise IndexError("Item Index Error.")

    def print_digimons(self):
        for digimon_element in self.digimon_list:
            print(f"Name: {digimon_element.text_normal}")
            print("---------------------------------------------------------------------------")


if __name__ == "__main__":
    digimon_reader = DigimonInfoReader('../assets/data/datatable/Digimon/Info.csv')
    try:
        digimon = digimon_reader.get_digimon_by_index(2)
        print(f"Digimon: {digimon.text_normal}")
    except IndexError as e:
        print(e)
