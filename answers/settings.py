import aiogram.utils.markdown as md
from aiogram import types

import db.notify_settings
from handlers import notify_settings
from main import bot


async def send_user_settings(user_id: int) -> types.Message:
    is_on_off_dict = db.notify_settings.get_user_notify_settings_to_dict(user_telegram_id=user_id)
    return await bot.send_message(
        user_id,
        md.text(
            md.text('раздел “Обучение”: изменения баллов в накопительно-балльной системе (НБС)'),
            md.text('раздел “Новости”: публикация общих новостей (новости по дисциплинам', md.hitalic('(coming soon))')),
            md.text('раздел “Ресурсы”: изменения и загрузка файлов по дисциплине', md.hitalic('(coming soon)')),
            md.text('раздел “Домашние задания”: изменения статусов отправленных работ'),
            md.text(
                'раздел “Заявки”: изменения статусов заявок на обходной лист, материальную помощь, социальную стипендию, копии документов, справки'),
            sep=',\n\n',
        ),
        reply_markup=notify_settings.init_notify_settings_inline_btns(is_on_off=is_on_off_dict),
    )
