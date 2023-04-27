import pytest

from src.utils import load_json, get_filtered_data, get_last_five, get_exchanged_data


@pytest.fixture
def file():
    file = '../src/operations.json'
    return file

def test_load_json(file):
    data = load_json(file)
    assert isinstance(data, list)


def test_filtered_data(item, item1):
    assert get_filtered_data(item) == item
    assert get_filtered_data(item1) == []


def test_get_last_five(item):
    test = get_last_five(item)
    assert [elem["date"] for elem in test] == ["2019-08-26T10:50:58.294041", "2019-07-03T18:35:29.512364", "2018-06-30T02:08:58.425572"]


def test_get_exchanged_data(item):
    test = get_exchanged_data(item[:1])
    assert test[0] == '\n30.06.2018 Перевод организации\n -> Счет **1177\n9824.07 USD'