from typing import Any, Dict
from templates.definitions import TEMPLATES, TemplateDefinition

class TemplateEngine:
    def __init__(self) -> None:
        self._defs: Dict[str, TemplateDefinition] = TEMPLATES

    def fill(self, template_id: str, context: Dict[str, Any]) -> Dict[str, Any]:
        definition = self._defs[template_id]
        out: Dict[str, Any] = {}

        for field in definition.fields:
            source_obj = context.get(field.source)
            if source_obj is None and field.required:
                raise ValueError(f"Missing source {field.source}")

            if field.path == "*":
                out[field.key] = source_obj
            else:
                value = source_obj
                for part in field.path.split("."):
                    if hasattr(value, part):
                        value = getattr(value, part)
                    elif isinstance(value, dict) and part in value:
                        value = value[part]
                    else:
                        value = None
                        break
                if hasattr(value, '__dict__'):
                    value = vars(value)
                out[field.key] = value

        return out
