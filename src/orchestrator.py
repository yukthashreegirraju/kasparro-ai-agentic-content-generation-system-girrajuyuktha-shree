from agents.product_parser import ProductParser
from agents.faq_generator import FAQGeneratorAgent
from pathlib import Path
import json
from typing import List
from dataclasses import dataclass

@dataclass
class FAQItem:
    category: str
    question: str
    answer: str

class FAQGeneratorAgent:
    def run(self, product) -> List[FAQItem]:
        return [
            FAQItem("Usage", "How to use?", product.usage),
            FAQItem("Usage", "When to apply?", "Morning before sunscreen"),
            FAQItem("Safety", "Side effects?", product.side_effects),
            FAQItem("Info", "Concentration?", product.concentration),
            FAQItem("Info", "Skin types?", product.skin_type)
        ]

def run_pipeline():
    # Parse
    parser = ProductParser()
    product = parser.run("data/glowboost.json")
    
    # FAQ
    faq_gen = FAQGeneratorAgent()
    faq = faq_gen.run(product)
    
    # Generate 3 JSON pages
    Path("output").mkdir(exist_ok=True)
    
    # FAQ Page
    with open("output/faq_page.json", "w") as f:
        json.dump([{"category": f.category, "question": f.question, "answer": f.answer} for f in faq], f, indent=2)
    
    # Product Page  
    with open("output/product_page.json", "w") as f:
        json.dump({
            "name": product.product_name,
            "price": f"₹{product.price}",
            "benefits": product.benefits,
            "ingredients": product.ingredients
        }, f, indent=2)
    
    # Comparison Page
    with open("output/comparison_page.json", "w") as f:
        json.dump({
            "glowboost": {"price": product.price, "concentration": product.concentration},
            "competitor": {"price": 999, "concentration": "15% Vitamin C"}
        }, f, indent=2)
    
    print("🎉 SUCCESS! Check output/*.json")

if __name__ == "__main__":
    run_pipeline()

