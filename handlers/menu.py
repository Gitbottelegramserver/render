from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext

from app import get_module_content

router = Router()

# Главное меню
@router.message(F.text.lower() in ["обучение", "модули", "🎓 обучение"])
async def show_modules_menu(message: Message, state: FSMContext):
    await message.answer(
        "Выберите номер модуля, чтобы получить полную информацию:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="1️⃣"), KeyboardButton(text="2️⃣"), KeyboardButton(text="3️⃣")],
                [KeyboardButton(text="4️⃣"), KeyboardButton(text="5️⃣"), KeyboardButton(text="6️⃣")],
                [KeyboardButton(text="7️⃣")],
            ],
            resize_keyboard=True,
            input_field_placeholder="Напишите номер модуля (1–7)"
        )
    )

# Ответ на выбор модуля
@router.message(F.text.in_(["1", "2", "3", "4", "5", "6", "7", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣"]))
async def handle_module_choice(message: Message, state: FSMContext):
    module_number = message.text.strip()[0]  # 1️⃣ → 1
    module = get_module_content(module_number)
    
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=btn)] for btn in module["buttons"]],
        resize_keyboard=True,
        input_field_placeholder="Выберите действие по модулю"
    )
    
    await message.answer(module["description"], reply_markup=keyboard)
