import base_settings

from database import schemes


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


async def generate_json_from_text(text: str) -> schemes.StudentsReview:
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
        model=base_settings.model, contents=[]
    )
    if response.text is None:
        raise AttributeError("Gemini response is None")

    return schemes.StudentsReview.model_validate_json(response.text)
