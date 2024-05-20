from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from Lesson3.keyboards.career_keyboard import make_keyboard

router = Router()

available_jobs = [
    'Программист',
    'Маркетолог',
    'Менеджер',
    'Аналитик',
    'Бухгалтер']

available_grades = [
    'Низкий',
    'Средний',
    'Высокий']

class Choice(StatesGroup):
    job = State()
    grade = State()

@router.message(Command(commands=['prof']))
async def start(message: types.Message,state: FSMContext):
    await message.answer('Какая профессия Вас интересует?', reply_markup=make_keyboard(available_jobs))
    await state.set_state((Choice.job))

@router.message(Choice.job, F.text.in_(available_jobs))
async def jobs(mesage: types.Message, state: FSMContext):
    await mesage.answer('Как вы оцениваете свой уровень?', reply_markup=make_keyboard(available_grades))
    await state.set_state(Choice.grade)
@router.message(Choice.job)
async def job_incorrrect(mesage: types.Message):
    await mesage.answer('Ошибка. Попробуйте еще раз', reply_markup=make_keyboard(available_jobs))

@router.message(Choice.grade, F.text.in_(available_grades))
async def grade(mesage: types.Message, state: FSMContext):
    await mesage.answer(f'Опрос завершен. До созвончика :) {mesage.text}', reply_markup=types.ReplyKeyboardRemove())
    await state.clear()

@router.message(Choice.grade)
async def grade_incorrrect(mesage: types.Message):
    await mesage.answer('Ошибка. Попробуйте еще раз', reply_markup=make_keyboard(available_grades))



