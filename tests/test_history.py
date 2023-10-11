import datetime

from stage.history.history import History
from stage.history.history_context import HistoryContext, DatetimeHistory


def test_repr():
    history = History()
    context = HistoryContext("Author", "Hello, world!")
    history.add(context)
    assert repr(history) == "[HistoryContext(author='Author', prompt='Hello, world!')]"


def test_add():
    history = History()
    context = HistoryContext("Author", "Hello, world!")
    history.add(context)
    assert len(history.history) == 1
    assert history.history[0] == context


def test_said_by():
    history = History()
    context1 = HistoryContext("Author1", "Hello, world!")
    context2 = HistoryContext("Author2", "Goodbye, world!")
    history.add(context1)
    history.add(context2)
    assert history.said_by("Author1") == ["Hello, world!"]
    assert history.said_by("Author2") == ["Goodbye, world!"]
    assert history.said_by("Author3") == []


# DatetimeHistory

def test_dt_history_repr():
    dt_history = DatetimeHistory("Author", "Hello, world!", datetime.datetime.now())
    # this is just a simple check, adapt to your DatetimeHistory's __repr__ implementation
    assert "DatetimeHistory" in repr(dt_history)


def test_dt_datetime_prop():
    now = datetime.datetime.now()
    dt_history = DatetimeHistory("Author", "Hello, world!", now)
    assert dt_history.datetime == now
