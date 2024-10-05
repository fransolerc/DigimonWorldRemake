from dataclasses import dataclass
from typing import List


@dataclass
class DigimonInfo:
    text_normal: str
    text_romanized: str
    favorite_food: str
    level: int
    type: str
    speciality_1: str
    speciality_2: str
    speciality_3: str
    sleep_time: str
    training_preference: str
    sprite: str
    preferred_map_id: int
    default_weight: int
    energy_capacity: int
    energy_threshold: int
    energy_usage: int
    poop_size: int
    poop_timer: float
    height: float
    ai_partner_distance: float
    footstep_sound: str
    eat_sound: str
    attack_sound: str
    glad_sound: str
    down_sound: str
    feeding_time: List[int]
    enabled_techniques: List[int]
    default_technique: int
    finisher_index: int
    stats_gain_hp: int
    stats_gain_mp: int
    stats_gain_offense: int
    stats_gain_defense: int
    stats_gain_speed: int
    stats_gain_brains: int
    digivolution_requirement_bonus: str
    digivolution_requirement_hp: int
    digivolution_requirement_mp: int
    digivolution_requirement_offense: int
    digivolution_requirement_defense: int
    digivolution_requirement_speed: int
    digivolution_requirement_brains: int
    digivolution_requirement_care_mistakes: int
    digivolution_requirement_weight: int
    digivolution_requirement_happiness: int
    digivolution_requirement_discipline: int
    digivolution_requirement_battles_won: int
    digivolution_requirement_techniques: int
    digivolution_requirement_max_battles: int
    digivolution_requirement_max_care_mistakes: int
    digivolution_from: List[str]
    digivolution_to: List[str]

    def display_info(self):
        print(f"Text Normal: {self.text_normal}")
        print(f"Text Romanized: {self.text_romanized}")
        print(f"Favorite Food: {self.favorite_food}")
        print(f"Level: {self.level}")
        print(f"Type: {self.type}")
        print(f"Speciality #1: {self.speciality_1}")
        print(f"Speciality #2: {self.speciality_2}")
        print(f"Speciality #3: {self.speciality_3}")
        print(f"Sleep Time: {self.sleep_time}")
        print(f"Training Preference: {self.training_preference}")
        print(f"Sprite: {self.sprite}")
        print(f"Preferred Map ID: {self.preferred_map_id}")
        print(f"Default Weight: {self.default_weight}")
        print(f"Energy Capacity: {self.energy_capacity}")
        print(f"Energy Threshold: {self.energy_threshold}")
        print(f"Energy Usage: {self.energy_usage}")
        print(f"Poop Size: {self.poop_size}")
        print(f"Poop Timer: {self.poop_timer}")
        print(f"Height: {self.height}")
        print(f"AI Partner Distance: {self.ai_partner_distance}")
        print(f"Footstep Sound: {self.footstep_sound}")
        print(f"Eat Sound: {self.eat_sound}")
        print(f"Attack Sound: {self.attack_sound}")
        print(f"Glad Sound: {self.glad_sound}")
        print(f"Down Sound: {self.down_sound}")
        print(f"Feeding Time: {', '.join(map(str, self.feeding_time))}")
        print(f"Enabled Techniques: {', '.join(map(str, self.enabled_techniques))}")
        print(f"Default Technique: {self.default_technique}")
        print(f"Finisher Index: {self.finisher_index}")
        print(f"Stats Gain - HP: {self.stats_gain_hp}")
        print(f"Stats Gain - MP: {self.stats_gain_mp}")
        print(f"Stats Gain - Offense: {self.stats_gain_offense}")
        print(f"Stats Gain - Defense: {self.stats_gain_defense}")
        print(f"Stats Gain - Speed: {self.stats_gain_speed}")
        print(f"Stats Gain - Brains: {self.stats_gain_brains}")
        print(f"Digivolution Requirement - Bonus: {self.digivolution_requirement_bonus}")
        print(f"Digivolution Requirement - HP: {self.digivolution_requirement_hp}")
        print(f"Digivolution Requirement - MP: {self.digivolution_requirement_mp}")
        print(f"Digivolution Requirement - Offense: {self.digivolution_requirement_offense}")
        print(f"Digivolution Requirement - Defense: {self.digivolution_requirement_defense}")
        print(f"Digivolution Requirement - Speed: {self.digivolution_requirement_speed}")
        print(f"Digivolution Requirement - Brains: {self.digivolution_requirement_brains}")
        print(f"Digivolution Requirement - Care Mistakes: {self.digivolution_requirement_care_mistakes}")
        print(f"Digivolution Requirement - Weight: {self.digivolution_requirement_weight}")
        print(f"Digivolution Requirement - Happiness: {self.digivolution_requirement_happiness}")
        print(f"Digivolution Requirement - Discipline: {self.digivolution_requirement_discipline}")
        print(f"Digivolution Requirement - Battles Won: {self.digivolution_requirement_battles_won}")
        print(f"Digivolution Requirement - Techniques: {self.digivolution_requirement_techniques}")
        print(f"Digivolution Requirement - Max Battles: {self.digivolution_requirement_max_battles}")
        print(f"Digivolution Requirement - Max Care Mistakes: {self.digivolution_requirement_max_care_mistakes}")
        print(f"Digivolution From: {', '.join(map(str, self.digivolution_from))}")
        print(f"Digivolution To: {', '.join(map(str, self.digivolution_to))}")
        print("---------------------------------------------------------------------------")
