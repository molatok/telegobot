from aiogram.utils import executor
from bot_start import dp

from Key import keys

keys.register_handlers(dp)

if __name__ == '__main__':
   executor.start_polling(dp)