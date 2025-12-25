from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class FieldMapping:
    source: str
    path: str
    key: str
    required: bool = True

@dataclass
class TemplateDefinition:
    fields: List[FieldMapping]

TEMPLATES: Dict[str, TemplateDefinition] = {
    "product_page": TemplateDefinition([
        FieldMapping("product", "name", "product_name"),
        FieldMapping("product", "description", "product_description"),
        FieldMapping("product", "price", "price"),
        FieldMapping("product", "images.0", "main_image"),
        FieldMapping("product", "*", "product"),
    ]),
    "faq_page": TemplateDefinition([
        FieldMapping("faq", "*", "faq_list", required=False),
    ])
}
