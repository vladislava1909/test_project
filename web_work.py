import requests
import json  # импортируем необходимую библиотеку

print("1. чтобы получить содержание ответа, надо обратится к полю content "
      "объекта response, который возвращается, когда приходит ответ от сервера"
      " через библиотеку Requests.")

r = requests.get(
    'https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')  # делаем запрос на сервер по переданному адресу
print(r.content)

print("2. status_code, который говорит нам о том, какой вообще ответ пришёл.")

r = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')
print(r.status_code)  # Узнаем статус полученного ответа

print("3. JSON-ответ, присланный нам с того же самого ресурса")

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')  # попробуем поймать json ответ
print(r.content)

print("4. чтобы использовать полученный ответ как Python-объект, "
      "надо воспользоваться дополнительной библиотекой, "
      "которая упрощает работу с JSON-ответами и может легко "
      "переконвертировать ответ от сервера в Python-объекты,"
      " с которыми удобно работать. Давайте поменяем наш код и превратим данный текст"
      " в список, на который он так сильно похож.")

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
texts = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы
print(type(texts))  # проверяем тип сконвертированных данных

for text in texts:  # выводим полученный текст. Но для того чтобы он влез в консоль оставим только первые 50 символов.
    print(text[:50], '\n')

print("5. сделаем его настоящим словарём.")

r = requests.get('https://api.github.com')

print(r.content)

d = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы

print(type(d))
print(d['following_url'])  # обращаемся к полученному объекту как к словарю и попробуем напечатать одно из его значений

print("6. Давайте попробуем отправить post-запрос.")

r = requests.post('https://httpbin.org/post', data={'key': 'value'})  # отправляем пост запрос
print(r.content)  # содержимое ответа и его обработка происходит так же, как и с гет-запросами, разницы никакой нет

print("7. с помощью уже знакомой нам библиотеки отправить данные в нужном нам формате.")

data = {'key': 'value'}

r = requests.post('https://httpbin.org/post', json=json.dumps(
    data))  # отправляем пост запрос, но только в этот раз тип передаваемых данных будет JSON
print(r.content)

print("8. Напишите программу, которая отправляет запрос на генерацию "
      "случайных текстов (используйте этот сервис). "
      "Выведите первый из сгенерированных текстов.")

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')

r = json.loads(r.content)

print(r[0])