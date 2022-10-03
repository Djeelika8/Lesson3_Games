'''  Игра - "Угадайка чисел" '''
from random import randint

def is_valid(n, dip):                                      # проверка ЦЕЛОЕ ли число
    return n.isdigit() and 1 <= int(n) <= dip**3


def Guess_the_numbers():                            # Игра - "Угадайка чисел"
    dip = int(input('С цифры 1 до какой границы загадать число?: '))
    r = randint(1, dip)                             # число из диапазона от 1 до введеного вкл/
    cont = 1
    while True:                                    # Бесконечный цикл
        n = input(f'{name}, введите число: ')
        while not is_valid(n, dip):                     # проверка введенного числа ч/з Функцию
            n = input('А может быть все-таки введем целое число? ')
        n = int(n)
        if n > r:
            print('Ваше число больше загаданного, попробуйте еще разок')
            cont += 1
        elif n < r:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            cont += 1
        else:
            print('Вы угадали, поздравляем!')
            print('число попыток: ', cont)
            break

name = input('Привет, как Вас зовут? ')
print(f'{name} Добро пожаловать в числовую угадайку')
Guess_the_numbers()

print('A может желаете еще сыграть?...')
new_game = int(input('Если ДА, наберите цифру 1: '))
if new_game == 1:
    Guess_the_numbers()
else:
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
