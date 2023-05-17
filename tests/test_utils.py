from src.utils import get_data, get_filtered_data, get_last_values, get_formatted_data


def test_get_data():
    data = get_data()
    assert isinstance(data, list)



def test_get_filtered_data(test_data):
    assert get_filtered_data(test_data) == [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}, {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}, {'id': 587085106, 'state': 'EXECUTED', 'date': '2018-03-23T10:45:06.972075', 'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Открытие вклада', 'to': 'Счет 41421565395219882431'}]
    assert get_filtered_data(test_data[:2], filter_empty=True) == [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'},
                                                {'id': 41428829, 'state': 'EXECUTED',
                                                 'date': '2019-07-03T18:35:29.512364',
                                                 'operationAmount': {'amount': '8221.37',
                                                                     'currency': {'name': 'USD', 'code': 'USD'}},
                                                 'description': 'Перевод организации',
                                                 'from': 'MasterCard 7158300734726758',
                                                 'to': 'Счет 35383033474447895560'}]
def test_get_last_values(test_data):
    data = get_last_values(test_data, 4)
    assert [x["date"] for x in data] == ['2019-08-26T10:50:58.294041', '2019-07-03T18:35:29.512364', '2018-06-30T02:08:58.425572', '2018-03-23T10:45:06.972075']
    assert data != 10


def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data)
    assert data == ['\n26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.', '\n03.07.2019 Перевод организации\nMasterCard 7158 30** **** 6758 -> Счет **5560\n8221.37 USD', '\n30.06.2018 Перевод организации\nСчет 7510 68** **** 6952 -> Счет **6702\n9824.07 USD', '\n23.03.2018 Открытие вклада\n  -> Счет **2431\n48223.05 руб.']



