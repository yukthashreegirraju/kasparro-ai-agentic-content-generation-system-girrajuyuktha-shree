from domain.product import Product
from content.blocks import (
    ContentBlocks,
    generate_benefits_block,
    extract_usage_block,
    generate_safety_block,
    generate_pricing_block,
)

class ContentBlockAgent:
    def run(self, product: Product) -> ContentBlocks:
        return ContentBlocks(
            benefits=generate_benefits_block(product),
            usage=extract_usage_block(product),
            safety=generate_safety_block(product),
            pricing=generate_pricing_block(product),
        )
