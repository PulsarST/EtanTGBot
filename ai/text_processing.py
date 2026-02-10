import json


async def process_raw_text(text: str) -> str: ...


async def generate_json_from_text(text: str) -> dict[str, int | str]: ...
