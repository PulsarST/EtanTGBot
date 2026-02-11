from datetime import datetime

from database.schemes import StudentsReview

from . import base_settings


async def process_raw_text(text: str) -> str | None:
    """
    process a raw text from user:
    1. corrects spelling mistakes
    2. corrects punctuation mistakes
    3. replaces slang words

    Args:
        text(str): raw text from student

    Returns:
        processed text or None
    """
    respone = base_settings.client.models.generate_content(
        model=base_settings.model, contents=[base_settings.process_raw_text_promt, text]
    )
    return respone.text


async def generate_json_from_text(
    text: str, professors_name: str, subjects_name: str, date: datetime
) -> StudentsReview:
    """
    generate a StudentReview schema from processed text

    Args:
        text(str): processed text

    Returns:
        StudentReview schema

    Raises:
        AttributeError: if Gemini ai can't generate Json from processed text
    """
    response = base_settings.client.models.generate_content(
        model=base_settings.model,
        contents=[
            text,
            f"professor's name: {professors_name}",
            f"subjects name: {subjects_name}",
            f"datetime: {date}",
        ],
    )
    if response.text is None:
        raise AttributeError("Gemini response is None")

    print(response.text)

    return StudentsReview.model_validate_json(response.text)
