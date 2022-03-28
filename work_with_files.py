print("1. Для работы с файлами в языке Python предусмотрена функция open()")

myFile = open('filename.txt', 'rt', encoding="utf8")


print("2. Метод read() — сохраняет всё содержимое файла как строку."
      "Если в метод read() передать число, то вернётся указанное число символов.")

print(myFile.read())  # read()


print("3. Метод readline() читает файл построчно. В него можно передавать число, "
      "и из строки будет прочитано указанное число символов. "
      "Важно! Как только мы применили этот метод, "
      "то повторное его применение выдаст вторую строку, ещё одно — третью строку и так далее.")

print(myFile.readline())  # readline()
print(myFile.readline())
print(myFile.readline())
print(myFile.readline())


print("4. Метод readlines() вернёт список, в котором элементами будут строки из файла. "
      "В примере видно (смотрите на стрелочку), что в файле есть одна строка с текстом, "
      "затем пустая строка, а затем ещё одна строка с текстом.")

print(myFile.readlines())  # readlines()


print("5. чтение файла построчно в цикле for."
      "Как видим, результат соответствует предыдущему примеру: "
      "сначала идёт первая строка с текстом, затем пустая, "
      "затем третья строка опять же с текстом.")

myFile = open('filename.txt')

for line in myFile:
    print(line)
myFile.close()

print("6. Выполните код c демонстрацией записи в файл. Откройте только что созданный файл.")

myFile = open('namefile.txt', 'w')
myFile.write('tttt')
print('zzzz', file=myFile)

myFile.close()


print("7. пользователь вводит произвольное целое число, "
      "а программа читает некий русский текст из файла и зашифровывает его в другой файл со сдвигом,"
      " соответствующим этому числу.")

alpha = 'абвгдеёжзиклмнщпрстуфхцчшщъыьэюя'
alphaUp = 'АБВГДЕЁЖЗИКЛМНОПРОСТУФЦЧЪЫЬЭЮЯ'
number = int(input(' Введите число, на которое нужно сдвинуть текст: '))

summary = ' '


def changeChar(char):
    if char in alpha:
        return alpha[(alpha.index(char) + number) % len(alpha)]
    elif char in alphaUp:
        return alphaUp[(alphaUp.index(char) + number) % len(alphaUp)]
    else:
        return char


with open("filename.txt", encoding="utf8") as myFile:
    for line in myFile:
        for char in line:
            summary += changeChar(char)


with open("output.txt", 'w', encoding="utf8") as myFile:
    myFile.write(summary)


