from datetime import datetime


class HistoryContext:
    def __init__(self, author, prompt):
        """
        Create a new instance of HistoryContext.

        :param author: The author of the context
        :param prompt: The prompt of the context
        """
        self._author = author
        self._prompt = prompt

    def __repr__(self):
        return f"HistoryContext(author='{self.author}', prompt='{self.prompt}')"

    @property
    def author(self):
        return self._author

    @property
    def prompt(self):
        return self._prompt


class DatetimeHistory(HistoryContext):
    def __init__(self, author, prompt, dt: datetime):
        """
        Create a new instance of DatetimeContext.

        :param author: The author of the context
        :param prompt: The prompt of the context
        :param datetime: The datetime of the context
        """
        super().__init__(author, prompt)
        self._datetime = dt

    def __repr__(self):
        return f"DatetimeHistory(author='{self.author}', prompt='{self.prompt}', datetime='{self._datetime}')"

    @property
    def datetime(self):
        return self._datetime
