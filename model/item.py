from dataclasses import dataclass


@dataclass
class Item:
    name: str
    description: str
    digivolution: str
    item_type: str
    color: str
    sorting_value: str
    weight: str
    energy: str
    happiness: str
    discipline: str
    tiredness: str
    sickness: str
    heal_hp: str
    heal_mp: str
    increase_hp: str
    increase_mp: str
    increase_offense: str
    increase_defense: str
    increase_speed: str
    increase_brains: str
    increase_lifetime: str
    price_money: str
    merit_value: str
