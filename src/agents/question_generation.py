from typing import List
from domain.product import Product
from domain.questions import Question

class QuestionGenerationAgent:
    def run(self, product: Product) -> List[Question]:
        p = product
        q: List[Question] = []

        # informational
        q.append(Question("q1", "informational", f"What is {p.name}?"))
        q.append(Question("q2", "informational", f"What are the key ingredients in {p.name}?"))
        q.append(Question("q3", "informational", f"What skin types is {p.name} suitable for?"))
        q.append(Question("q4", "informational", f"What is the Vitamin C concentration in {p.name}?"))

        # usage
        q.append(Question("q5", "usage", f"How should {p.name} be used in a morning routine?"))
        q.append(Question("q6", "usage", f"How many drops of {p.name} should be applied each time?"))
        q.append(Question("q7", "usage", f"Should {p.name} be applied before or after sunscreen?"))

        # safety
        q.append(Question("q8", "safety", f"Are there any side effects when using {p.name}?"))
        q.append(Question("q9", "safety", f"Is {p.name} suitable for sensitive skin?"))
        q.append(Question("q10", "safety", f"What should I do if I feel strong tingling after using {p.name}?"))

        # purchase
        q.append(Question("q11", "purchase", f"What is the price of {p.name}?"))
        q.append(Question("q12", "purchase", f"Is {p.name} affordable for daily use?"))

        # comparison
        q.append(Question("q13", "comparison", f"How does {p.name} compare to another Vitamin C serum in ingredients?"))
        q.append(Question("q14", "comparison", f"How does the price of {p.name} compare to a similar serum?"))
        q.append(Question("q15", "comparison", f"Which product is better for oily skin: {p.name} or another Vitamin C serum?"))

        return q
