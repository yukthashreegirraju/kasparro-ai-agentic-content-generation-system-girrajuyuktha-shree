from dataclasses import dataclass
from typing import List
from domain.product import Product
from domain.questions import Question
from content.blocks import ContentBlocks

@dataclass
class FAQEntry:
    question_id: str
    category: str
    question: str
    answer: str

def generate_faq_entries(
    product: Product,
    blocks: ContentBlocks,
    questions: List[Question]
) -> List[FAQEntry]:
    p = product
    answers = {
        "q1": f"{p.name} is a serum with {p.concentration} that helps brighten skin and fade dark spots.",
        "q2": f"{p.name} contains {', '.join(p.ingredients)} as key ingredients.",
        "q3": f"{p.name} is suitable for {', '.join(p.skin_types)} skin types.",
        "q5": blocks.usage.steps[0],
        "q8": p.side_effects,
        "q11": f"{blocks.pricing.price_text} for {p.name}."
    }

    faqs: List[FAQEntry] = []
    for q in questions:
        if q.id in answers:
            faqs.append(
                FAQEntry(
                    question_id=q.id,
                    category=q.category,
                    question=q.text,
                    answer=answers[q.id],
                )
            )
    return faqs
