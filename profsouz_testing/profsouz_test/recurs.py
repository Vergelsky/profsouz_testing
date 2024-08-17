import json


def get_companies(data: dict) -> tuple:
    """
    Получение данных всех компаний из списка
    """
    result = ()
    # Добавляем данные текущей компании
    if data.get('id'):
        # Если они вообще есть
        result += (data['title'], data['id']),

    children = data.get('children')
    # Если потомков нет - возвращаем данные текущей компании
    if not children:
        return result
    else:
        # Если потомки есть - получаем данные компаний из потомков, и возвращаем вместе с текущей
        for company in children:
            result += get_companies(company)
        return result
