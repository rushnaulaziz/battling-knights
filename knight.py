from dataclasses import dataclass

from item import Item
from tile import Tile


@dataclass
class Knight:
    """ 
    This class hold the properties and methods of Knight
    """
    id: str
    name: str
    tile: Tile
    defence_power: int = 1
    attack_power: int = 1
    item: Item = None
    status: str = "ALIVE"