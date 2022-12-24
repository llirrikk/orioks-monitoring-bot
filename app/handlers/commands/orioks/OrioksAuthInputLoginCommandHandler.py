from aiogram import types
from aiogram.utils import markdown

from app.forms import OrioksAuthForm
from app.handlers import AbstractCommandHandler


class OrioksAuthInputLoginCommandHandler(AbstractCommandHandler):
    @staticmethod
    async def process(message: types.Message, *args, **kwargs):
        if not message.text.isdigit():
            return await message.reply(
                markdown.text(
                    markdown.text('Логин должен состоять только из цифр.'),
                    markdown.text('Введи логин (только цифры):'),
                    sep='\n',
                ),
            )

        state = kwargs.get('state', None)
        async with state.proxy() as data:
            data['login'] = int(message.text)

        await OrioksAuthForm.next()
        await message.reply(
            markdown.text(
                markdown.hbold('Введи пароль ОРИОКС:'),
                markdown.text(),
                markdown.text(
                    markdown.hitalic(
                        '🔒 Пароль используется только для однократной авторизации'
                    ),
                    markdown.hitalic(
                        'Он не хранится на сервере и будет удалён из истории сообщений'
                    ),
                    markdown.text(
                        'Узнать подробнее можно <a href="https://orioks-monitoring.github.io/bot/faq.html#%D0%BF%D0%BE%D1%87%D0%B5%D0%BC%D1%83-%D1%8D%D1%82%D0%BE%D1%82-%D0%B1%D0%BE%D1%82-%D0%B1%D0%B5%D0%B7%D0%BE%D0%BF%D0%B0%D1%81%D0%B5%D0%BD">здесь</a>'
                    ),
                    sep='. ',
                ),
                sep='\n',
            ),
            disable_web_page_preview=True,
        )
