# Игра: угадай число.
import random
num = random.randint(1, 100)
while True:
    print("Угадай чило от 1 до 100!")
    guess = int(input("Введите число:"))
    if guess == num:
        print("Правильно!")
        break
    elif guess < num:
        print("Загаданное число больше!")
    elif guess > num:
        print("Загаданное число меньше!")