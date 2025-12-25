from dataclasses import dataclass
from typing import List
from domain.product import Product

@dataclass
class ComparisonPoint:
    key: str
    label: str
    product_a: str
    product_b: str

@dataclass
class ProductBSummary:
    id: str
    name: str
    concentration: str
    ingredients: List[str]
    benefits: List[str]
    price: int

@dataclass
class ComparisonPayload:
    product_a: dict
    product_b: ProductBSummary
    points: List[ComparisonPoint]

class ComparisonAgent:
    def run(self, product_a: Product) -> ComparisonPayload:
        product_b = ProductBSummary(
            id="radiance-plus-vitamin-c-serum",
            name="Radiance Plus Vitamin C Serum",
            concentration="15% Vitamin C",
            ingredients=["Vitamin C"],
            benefits=["Brightening", "Evens skin tone"],
            price=899
        )

        points = [
            ComparisonPoint("concentration", "Vitamin C concentration",
                            product_a.concentration, product_b.concentration),
            ComparisonPoint("ingredients", "Key ingredients",
                            ", ".join(product_a.ingredients),
                            ", ".join(product_b.ingredients)),
            ComparisonPoint("benefits", "Benefits",
                            ", ".join(product_a.benefits),
                            ", ".join(product_b.benefits)),
            ComparisonPoint("price", "Price (INR)",
                            str(product_a.price), str(product_b.price)),
            ComparisonPoint("skin_types", "Suitable skin types",
                            ", ".join(product_a.skin_types),
                            "All skin types")
        ]

        return ComparisonPayload(
            product_a={"id": product_a.id, "name": product_a.name},
            product_b=product_b,
            points=points
        )
