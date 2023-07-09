from aiogram.dispatcher.filters.state import StatesGroup, State

class comment(StatesGroup):
    reklama_edit_text = State()
    reklama_edit_image = State()
    
    