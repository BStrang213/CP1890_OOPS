from dataclasses import dataclass


@dataclass
class Movie:
    Name: str
    year: int
    minutes: int
    id: int
    category: str

