from dataclasses import dataclass


@dataclass
class Baseball:
    player: str = ""
    atbats: int = 0
    hits: int = 0
