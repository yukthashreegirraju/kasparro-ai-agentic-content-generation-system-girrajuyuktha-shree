from dataclasses import dataclass
from typing import List, Dict, Any
from agents.product_parser import Product

@dataclass
class FAQItem:
    question: str
    answer: str

class FAQGeneratorAgent:
    def run(self, product: Product) -> List[FAQItem]:
        # Generate FAQ based on product data
        faq = [
            FAQItem(
                question="How to use this product?",
                answer=f"Apply {product.name} to clean skin morning and night. Follow with moisturizer."
            ),
            FAQItem(
                question="When will I see results?",
                answer="Visible results in 7-14 days with consistent use."
            ),
            FAQItem(
                question="Is this suitable for my skin type?",
                answer="Yes, {product.name} works for all skin types including sensitive skin."
            )
        ]
        return faq
