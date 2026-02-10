import json

import base_settings


async def process_raw_text(text: str) -> str | None:
    respone = base_settings.client.models.generate_content(
        model=base_settings.model, contents=[base_settings.process_raw_text_promt, text]
    )
    return respone.text


async def generate_json_from_text(text: str) -> dict[str, int | str]:
    response = base_settings.client.models.generate_content(
        model=base_settings.model, contents=[]
    )
    return json.loads(response.text or "")
