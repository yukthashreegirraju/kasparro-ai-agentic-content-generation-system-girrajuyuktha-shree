from dataclasses import dataclass
from typing import List
from domain.product import Product

@dataclass
class BenefitsBlock:
    heading: str
    bullets: List[str]

@dataclass
class UsageBlock:
    heading: str
    steps: List[str]
    caution: str

@dataclass
class SafetyBlock:
    heading: str
    side_effects: str
    suitable_for: List[str]

@dataclass
class PricingBlock:
    heading: str
    price_text: str

@dataclass
class ContentBlocks:
    benefits: BenefitsBlock
    usage: UsageBlock
    safety: SafetyBlock
    pricing: PricingBlock


def generate_benefits_block(p: Product) -> BenefitsBlock:
    bullets = [b if b.endswith(".") else b + "." for b in p.benefits]
    return BenefitsBlock("Key benefits", bullets)

def extract_usage_block(p: Product) -> UsageBlock:
    return UsageBlock(
        "How to use",
        [p.how_to_use],
        "Always follow with sunscreen in the morning."
    )

def generate_safety_block(p: Product) -> SafetyBlock:
    suitable = [s.capitalize() + " skin" for s in p.skin_types]
    return SafetyBlock("Safety & side effects", p.side_effects, suitable)

def generate_pricing_block(p: Product) -> PricingBlock:
    return PricingBlock("Price", f"₹{p.price}")
