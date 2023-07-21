import typing

from aiogram.dispatcher.filters import BoundFilter


class CallbackFilter(BoundFilter):
    key = 'callback_data'

    def __init__(self, callback_data: typing.Union[str, typing.List[str]] = None):
        self.callback_data = callback_data

    async def check(self, obj):
        if self.callback_data is None:
            return False

        if isinstance(self.callback_data, str):
            return obj.data == self.callback_data

        return obj.data in self.callback_data

