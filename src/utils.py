import json
from datetime import datetime

def load_json(file):
    """Загружаем данные из файла"""
    with open(file, 'r', encoding='utf8') as json_file:
        data = json.load(json_file)
        return data


def get_filtered_data(data):
    """Фильтруем файл по выполненым переводам(EXECUTED)"""
    data = [x for x in data if 'state' in x and 'from' in x and x['state'] == 'EXECUTED']
    return data


def get_last_five(data):
    """Берём последние 5 значений"""
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:5]


def get_exchanged_data(data):
    '''Собираем информацию и выводим в необходимом формате'''
    new_data = []
    for i in data:
        time = datetime.strptime(i['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = i['description']
        sender = i['from'].split()
        if len(sender) == 2:
            from_ = f'{sender[0]} {sender[1][:4]} {sender[1][4:6]}** **** {sender[1][:4]}'
        else:
            from_ = f'{" ".join(sender[:-1])} {sender[-1][:4]} {sender[-1][4:6]}** **** {sender[-1][:4]}'
        receiver = i['to'].split()
        amount = i['operationAmount']['amount']
        currency = i['operationAmount']['currency']['name']

        new_data.append(f'{time} {description}\n'
                        f'{from_} -> {receiver[0]} **{receiver[1][:4]}\n'
                        f'{amount} {currency}')
    return new_data
