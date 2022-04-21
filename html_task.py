import lxml.html
import requests # импортируем наш знакомый модуль
from lxml import etree
print("1. Напишите программу, которая будет с помощью парсера lxml доставать текст из тега tag2 следующего HTML:"
      "<html>"
      "<head> <title> Some title </title> </head>"
      "<body>"
        "<tag1> some text"
            "<tag2> MY TEXT </tag2>"
        "</tag1>"
      "</body"
      "</html>")


html = ''' <html>
 <head> <title> Some title </title> </head>
 <body>
  <tag1> some text
     <tag2> MY TEXT </tag2>
   </tag1>
 </body>
</html>
'''

tree = lxml.html.document_fromstring(html)

text = tree.xpath('/html/body/tag1/tag2/text()')  # xpath для нахождения текста элемента tag2

print(text)

print("2. Используя полученные знания, допишите сделанный в начале юнита скрипт "
      "(где мы доставали заголовки новостей о Python с Python.org) так, "
      "чтобы он показывал ещё и дату добавления новости."
      "Примечание: Для получения атрибутов тега (т. е. его дополнительных параметров)"
      " используется метод .get(<имя атрибута>).")

html = requests.get('https://www.python.org/').content  # получим html главной странички официального сайта python

# создадим объект ElementTree. Он возвращается функцией parse()
tree = etree.parse('Welcome to Python.org.html',
                   lxml.html.HTMLParser())  # попытаемся спарсить наш файл с помощью html парсера

ul = tree.findall(
    'body/div/div[3]/div/section/div[3]/div[1]/div/ul/li')  # помещаем в аргумент методу findall скопированный xpath

# создаём цикл в котором мы будем выводить название каждого элемента из списка
for li in ul:
    a = li.find('a')  # в каждом элементе находим где хранится название. У нас это тег <a>
    time = li.find('time')
    print(time.get('datetime'), a.text)  # из этого тега забираем текст - это и будет нашим названием

