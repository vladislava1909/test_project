import json

# вида файлов :
# -текстовые(txt. html.);
# - бинарные(аудио, видео, изображения)
# Последовательность взаимодействия:
# открыть файл - open()
# чтение файла - read() или запись в файл - write()
# закрытие файла - close()

# открытие и закрытие файла
# open(file, mode)
# file: путь файла
# - абсолютный(относительно памяти компьютера)
# - относительный(непосредственно имя файла, расположенного в одной папке с файлом кода)

# mode: Режимы чтения файла
# r (read) - файл открывается для чтения
# w (write) - файл открывается для записи
# a (append) - файл открывается для дозаписи
# b (binary) - для работы бинарного файла; комбинируется с другими режимами: br(чтение), bw(запись)

# создание файла
#myfile = open('hello.txt', 'w')
#myfile.close()

# чтение файла
#myfile = open('hello.txt', 'r')
#file = myfile.read()
#print(file)
#myfile.close()

# работа с файлами исключения
#try:
    #somefile = open('hello.txt1', 'w')
    #try:
        #somefile.write('hello world')
    #except Exception as e:
        #print(e)
    #finally:
        #somefile.close()
#except Exception as ex:
    #print(ex)


#конструкция, которая автоматически открывает и закрывает файл - with
# with open(file, mode) as file_object:
#      инструкции

# with open('hello2.txt', 'w') as somefile:
#    somefile.write('good!')

# дозапись

# with open('hello2.txt', 'a') as file:
#     file.write('\nBad!')


# чтение файла 'r' readline() - считывает одну строку из файла
# read() - считывает всё содержимое из файла в одну строку
# readlines() - считывает все строки из файла в список

#readline
#with open('17-4.txt') as f:
#    a = f.readline()
#    print(a)

#readlines
#with open('17-4.txt') as f:
#    a = f.readlines()
#    print(a)

#map
#with open('17-4.txt') as f:
#    a = f.readlines()
#    b = list(map(int, a))
#    print(b)

# без map
#with open('17-4.txt') as f:
#    a = f.readlines()
#    b = [ int(x) for x in a]
#    print(b)


#Задачи:

#1
# В файле 17-4.txt содержится последовательность целых чисел.
# Элементы последовательности могут принимать целые значения
# от 0 до 10000 включительно.
# Рассматривается множество элементов последовательности,
# которые удовлетворяют следующим условиям:
# - в числе есть хотя бы два нуля
# - число кратно 7
# Найдите наибольшее из таких чисел и их количество.

#with open('17-4.txt') as f:
#    s = f.readlines()
#    a = list(map(int, s))
#    res = []
#    for i in a:
#        if str(i).count('0') >= 2 and i % 7 == 0:
#            res.append(i)
#print(max(res),len(res))

#2
# В файле 17-4.txt содержится последовательность целых чисел.
# Элементы последовательности могут принимать целые значения
# от 0 до 10000 включительно.
# Определите количество пар,
# в которых хотя бы один из двух элементов заканчивается на 7,
# а их сумма делится на 12. В ответе запишите два числа:
# сначала количество найденных пар,
# а затем максимальную сумму элементов таких пар.
# В данной задаче под парой подразумевается
# два идущих подряд элемента последовательности.

#with open('17-205.txt') as f:
#    s = [int(x) for x in f]
#    res = []
#    for i in range(1, len(s)):  #print(s[i], ' ', s[i-1]) # комбинация попарно
#        if (abs(s[i]) % 10 == 7 or abs(s[i-1]) % 10 == 7) and (s[i] + s[i-1]) % 12 == 0:
#            res.append(s[i] + s[i-1])
#    print(len(res), max(res))

# 3
# Текстовый файл состоит не более чем из 10**6 последовательности символов X, Y, и Z.
# Определите максимальное количество идущих подряд символов,
# среди которых каждые два соседних различны.

#with open('24_demo.txt') as f:
#    s = f.readline()
#    m = 1
#    k = 1
#   for i in range(1, len(s)):
#       if s[i] != s[i-1]:
#           k += 1
#            m = max(k, m)
#        else:
#            k = 1
#print(m)


# 4
# подсчитать количество слов

# file = open('textpython.txt')
# data = file.read()
# words = data.split()
# print(len(words))
# file.close()


# JSON

#data = {
#    "name": "Ivan",
#    "age": 26,
#    "city": "Saratov"
#}

#with open('data_file.json', 'w') as f:
#    json.dump(data, f)







