import typing

from aiogram.dispatcher.filters import BoundFilter


class CallbackFilter(BoundFilter):
    key = 'callback_data'

    def __init__(self, callback_data: typing.Optional[str] = None):
        self.callback_data = callback_data

    async def check(self, obj):
        if self.callback_data is None:
            return False

        return obj.data == self.callback_data

