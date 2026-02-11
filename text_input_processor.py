from datetime import datetime


async def create_students_review(
    professors_name: str, subjects_name: str, students_text, date: datetime
) -> None:
    from ai.text_processing import generate_json_from_text, process_raw_text

    clean_text = await process_raw_text(students_text)
    review = await generate_json_from_text(
        str(clean_text), professors_name, subjects_name, date
    )
    print(review)
