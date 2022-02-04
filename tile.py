from dataclasses import dataclass, field


@dataclass
class Tile:
    """
    This class holds the properties and methods for Tile object in Arena
    """
    row: int
    col: int
    knight  = None
    items: list = field(default_factory=list)