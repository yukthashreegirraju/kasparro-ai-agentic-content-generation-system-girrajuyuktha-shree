from dataclasses import dataclass
from typing import List

@dataclass
class Product:
    id: str
    name: str
    concentration: str
    skin_types: List[str]
    ingredients: List[str]
    benefits: List[str]
    how_to_use: str
    side_effects: str
    price: int
    currency: str
