from dataclasses import dataclass

@dataclass
class Item:
    name: str
    priority: int
    tile: tuple
    attack: int
    defence: int
    equipped: bool = False

    