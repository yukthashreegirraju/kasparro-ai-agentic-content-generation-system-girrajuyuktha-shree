from pathlib import Path
import json
from dataclasses import dataclass
from typing import List

@dataclass
class Product:
    product_name: str
    concentration: str
    skin_type: str
    ingredients: List[str]
    benefits: List[str]
    usage: str
    side_effects: str
    price: int

class ProductParser:
    def run(self, path: str) -> Product:
        raw = json.loads(Path(path).read_text(encoding="utf-8"))
        return Product(**raw)

