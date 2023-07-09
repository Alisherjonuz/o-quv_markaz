from aiogram.dispatcher.filters.state import StatesGroup, State

class register(StatesGroup):
    name = State()
    phone = State()
    address = State()
    subject = State()