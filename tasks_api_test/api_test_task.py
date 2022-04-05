# Написать простой тест, который проверяет JSON на правильность полей.
# То есть проверяет, что каждый объект в JSON:

# Содержит все перечисленные в требованиях поля.
# Не имеет других полей.
# Все поля имеют именно тот тип, который указан в требованиях:
# int — целое число;
# string — произвольная строка;
# string (url) — это строка с url. В рамках этого задания проверяем,
# что url начинается c http:\\ или https:\\;
# string (itemBuyEvent или itemViewEvent) — строка,
# в которой могут быть только эти конкретные два значения и никакие другие;
# bool — булево значение, то есть True или False.
# Тест должен вернуть Pass или список значений, которые тест посчитал ошибочными,
# и причину, почему они ошибочные.

import json

original_response_dict = {
"timestamp":0,
"referer": "",
"location":"",
"remoteHost":"",
"partyId":"",
"sessionId":"",
"pageViewId":"",
"eventType":"",
"item_id":"",
"item_price":0,
"item_url":"",
"basket_price":"",
"detectedDuplicate":True,
"detectedCorruption":True,
"firstInSession":True,
"userAgentName":""
}

def is_url(text):
    original_str = str(text)
    return len(original_str) > 0 \
           and (original_str.startswith("http://")
                or original_str.startswith("https://"))

def is_eventType(text):
    original_str = str(text)
    return original_str == 'itemBuyEvent' or 'itemViewEvent'

def test_api(data_json):
    error_dict = {}

    if type(data_json) is not list:
        error_dict["Формат ответа"] = "Тело ответа не является списком."
        return error_dict
    elif len(data_json) == 0:
        error_dict["Формат ответа"] = "В теле ответа не данных(пустое)."
        return error_dict

    for item in data_json:
        if len(dict(item).keys()) != len(original_response_dict.keys()):
            error_dict["Формат ответа"] = " Количество полей в ответе не соответствует требованиям."
        for name, value in original_response_dict.items():
            if item.get(name) is None:
                error_dict[name] = "Поле не найдено в теле объекта."
            elif type(item.get(name)) is not type(value):
                error_dict[name] = "Тип поля не соответствует требованиям."
            elif name == 'referer' and is_url(item.get(name)) is not True:
                error_dict[name] = "Поле не содержит URL."
            elif name == 'location' and is_url(item.get(name)) is not True:
                error_dict[name] = "Поле не содержит URL."
            elif name == 'item_url' and is_url(item.get(name)) is not True:
                error_dict[name] = "Поле не содержит URL."
            elif name == 'eventType' and is_eventType(item.get(name)) is not True:
                error_dict[name] = "Поле не соответствует требованиям."



    return error_dict

try:
    with open('example_api.json') as json_file:
        data = json.load(json_file)
except Exception as ex:
    print("Неверный формат json ответа.")
else:
    error_dictionary = test_api(data)
    if len(error_dictionary) > 0:
        print(error_dictionary)
    else:
        print("Pass")







