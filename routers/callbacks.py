from aiogram.dispatcher.router import Router
from aiogram.filters import CommandStart
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

router = Router()


class ReviewTeacherState(StatesGroup):
    professors_name = State()
    subject_name = State()
    students_text = State()


@router.message(CommandStart())
async def start_command(meesage: Message) -> None:
    """function to procces start command and send hello to user"""

    if meesage.from_user is None:
        return

    user_first_name = meesage.from_user.first_name
    await meesage.answer(f"Hi, {user_first_name} !")


@router.message(Command("review"))
async def send_review(message: Message, state: FSMContext) -> None:
    await state.set_state(ReviewTeacherState.professors_name)
    await message.answer("Введите имя преподавателя: ")


@router.message(ReviewTeacherState.professors_name)
async def process_professors_name(message: Message, state: FSMContext) -> None:
    await state.update_data(professors_name=message.text)
    await state.set_state(ReviewTeacherState.subject_name)
    await message.answer("Введите названия дицсиплины: ")


@router.message(ReviewTeacherState.subject_name)
async def process_subjects_name(message: Message, state: FSMContext) -> None:
    await state.update_data(subject_name=message.text)
    await state.set_state(ReviewTeacherState.students_text)
    await message.answer("Введите свой отзыв о преподавателе")


@router.message(ReviewTeacherState.students_text)
async def process_student_text(message: Message, state: FSMContext) -> None:
    user_data = await state.get_data()
    professors_name = user_data.get("professors_name")
    subjects_name = user_data.get("subject_name")
    students_text = message.text
    datetime = message.date

    from text_input_processor import create_students_review

    await create_students_review(
        str(professors_name), str(subjects_name), students_text, datetime
    )

    await message.answer("Благодарим за ваш отзыв !")
    await state.clear()
