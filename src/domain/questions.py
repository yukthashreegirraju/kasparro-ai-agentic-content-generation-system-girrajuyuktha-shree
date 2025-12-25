from dataclasses import dataclass
from typing import Literal

Category = Literal["informational", "usage", "safety", "purchase", "comparison"]

@dataclass
class Question:
    id: str
    category: Category
    text: str

