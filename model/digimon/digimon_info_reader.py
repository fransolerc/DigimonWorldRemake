import pandas as pd

from constant.digimon import DigimonConstants
from model.digimon.digimon_info import DigimonInfo


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
                    text_normal=row[DigimonConstants.DIGIMON_NAME_TEXT_NORMAL],
                    text_romanized=row[DigimonConstants.DIGIMON_NAME_TEXT_ROMANIZED],
                    favorite_food=row[DigimonConstants.DIGIMON_FAVORITE_FOOD],
                    level=row[DigimonConstants.DIGIMON_LEVEL],
                    type=row[DigimonConstants.DIGIMON_TYPE],
                    speciality_1=row[DigimonConstants.DIGIMON_SPECIALITY_1],
                    speciality_2=row[DigimonConstants.DIGIMON_SPECIALITY_2],
                    speciality_3=row[DigimonConstants.DIGIMON_SPECIALITY_3],
                    sleep_time=row[DigimonConstants.DIGIMON_SLEEP_TIME],
                    training_preference=row[DigimonConstants.DIGIMON_TRAINING_PREFERENCE],
                    sprite=row[DigimonConstants.DIGIMON_SPRITE],
                    preferred_map_id=row[DigimonConstants.DIGIMON_PREFERED_MAP_ID],
                    default_weight=row[DigimonConstants.DIGIMON_DEFAULT_WEIGHT],
                    energy_capacity=row[DigimonConstants.DIGIMON_ENERGY_CAPACITY],
                    energy_threshold=row[DigimonConstants.DIGIMON_ENERGY_THRESHOLD],
                    energy_usage=row[DigimonConstants.DIGIMON_ENERGY_USAGE],
                    poop_size=row[DigimonConstants.DIGIMON_POOP_SIZE],
                    poop_timer=row[DigimonConstants.DIGIMON_POOP_TIMER],
                    height=row[DigimonConstants.DIGIMON_HEIGHT],
                    ai_partner_distance=row[DigimonConstants.DIGIMON_AI_PARTNER_DISTANCE],
                    footstep_sound=row[DigimonConstants.DIGIMON_FOOTSTEP_SOUND],
                    eat_sound=row[DigimonConstants.DIGIMON_EAT_SOUND],
                    attack_sound=row[DigimonConstants.DIGIMON_ATTACK_SOUND],
                    glad_sound=row[DigimonConstants.DIGIMON_GLAD_SOUND],
                    down_sound=row[DigimonConstants.DIGIMON_DOWN_SOUND],
                    feeding_time=[row[f"{DigimonConstants.DIGIMON_FEEDING_TIME} #{i + 1}"] for i in range(8)],
                    enabled_techniques=[int(row[f"{DigimonConstants.DIGIMON_ENABLED_TECHNIQUES} #{i + 1}"]) for i in
                                        range(16)],
                    default_technique=int(row[DigimonConstants.DIGIMON_DEFAULT_TECHNIQUE]),
                    finisher_index=int(row[DigimonConstants.DIGIMON_FINISHER_INDEX]),
                    stats_gain_hp=row[DigimonConstants.DIGIMON_STATS_GAIN_HP],
                    stats_gain_mp=row[DigimonConstants.DIGIMON_STATS_GAIN_MP],
                    stats_gain_offense=row[DigimonConstants.DIGIMON_STATS_GAIN_OFFENSE],
                    stats_gain_defense=row[DigimonConstants.DIGIMON_STATS_GAIN_DEFENSE],
                    stats_gain_speed=row[DigimonConstants.DIGIMON_STATS_GAIN_SPEED],
                    stats_gain_brains=row[DigimonConstants.DIGIMON_STATS_GAIN_BRAINS],
                    digivolution_requirement_bonus=row[DigimonConstants.DIGIMON_DIGIVOLUTION_REQUIREMENT_BONUS],
                    digivolution_requirement_hp=int(row[DigimonConstants.DIGIMON_DIGIVOLUTION_REQUIREMENT_HP]),
                    digivolution_requirement_mp=int(row[DigimonConstants.DIGIMON_DIGIVOLUTION_REQUIREMENT_MP]),
                    digivolution_requirement_offense=int(
                        row[DigimonConstants.DIGIMON_DIGIVOLUTION_REQUIREMENT_OFFENSE]),
                    digivolution_requirement_defense=int(
                        row[DigimonConstants.DIGIMON_DIGIVOLUTION_REQUIREMENT_DEFENSE]),
                    digivolution_requirement_speed=int(row[DigimonConstants.DIGIMON_DIGIVOLUTION_REQUIREMENT_SPEED]),
                    digivolution_requirement_brains=int(row[DigimonConstants.DIGIMON_DIGIVOLUTION_REQUIREMENT_BRAINS]),
                    digivolution_requirement_care_mistakes=int(
                        row[DigimonConstants.DIGIMON_DIGIVOLUTION_REQUIREMENT_CARE_MISTAKES]),
                    digivolution_requirement_weight=int(row[DigimonConstants.DIGIMON_DIGIVOLUTION_REQUIREMENT_WEIGHT]),
                    digivolution_requirement_happiness=int(
                        row[DigimonConstants.DIGIMON_DIGIVOLUTION_REQUIREMENT_HAPPINESS]),
                    digivolution_requirement_discipline=int(
                        row[DigimonConstants.DIGIMON_DIGIVOLUTION_REQUIREMENT_DISCIPLINE]),
                    digivolution_requirement_battles_won=int(
                        row[DigimonConstants.DIGIMON_DIGIVOLUTION_REQUIREMENT_BATTLES_WON]),
                    digivolution_requirement_techniques=int(
                        row[DigimonConstants.DIGIMON_DIGIVOLUTION_REQUIREMENT_TECHNIQUES]),
                    digivolution_requirement_max_battles=int(
                        row[DigimonConstants.DIGIMON_DIGIVOLUTION_REQUIREMENT_MAX_BATTLES]),
                    digivolution_requirement_max_care_mistakes=int(
                        row[DigimonConstants.DIGIMON_DIGIVOLUTION_REQUIREMENT_MAX_CARE_MISTAKES]),
                    digivolution_from=[row[f"{DigimonConstants.DIGIMON_DIGIVOLUTION_FROM} #{i + 1}"] for i in range(5)],
                    digivolution_to=[row[f"{DigimonConstants.DIGIMON_DIGIVOLUTION_TO} #{i + 1}"] for i in range(6)],
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
    digimon_reader = DigimonInfoReader('../../assets/data/datatable/Digimon/Info.csv')
    try:
        digimon = digimon_reader.get_digimon_by_index(16)
        print(f"Digimon: {digimon.text_normal}")
    except IndexError as e:
        print(e)
