from typing import List

from stage.history.history_context import HistoryContext


class History:
    def __init__(self):
        self.history: List[HistoryContext] = []

    def __repr__(self):
        return self.history.__repr__()

    def add(self, context: HistoryContext):
        self.history.append(context)

    def said_by(self, author: str):
        quotes = [context.prompt for context in self.history if context.author == author]
        return quotes
