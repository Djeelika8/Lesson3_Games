'''Генератор безопасных паролей'''
from random import sample
import string

# print(string.punctuation)              # пунктуация  !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# print(string.digits)                   # числа  0123456789
# print(string.ascii_uppercase)          # заглавные  ABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.ascii_lowercase)          # строчные  abcdefghijklmnopqrstuvwxyz
# print(string.ascii_letters)            # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.hexdigits)                # 0123456789abcdefABCDEF
# print(string.octdigits)                # 01234567
# print(string.printable)                # цифры+строчные+заглавные+пунктуация  0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
#
# print('Строка string.whitespace')
# print(string.whitespace)               # все символы ASCII, которые считаются пробелами.

digits = string.digits                     # '0123456789'
lowercase_letters = string.ascii_lowercase # 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = string.ascii_uppercase # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # или lowercase_letters.upper()
punctuation = '!#$%&*+-=?@^_'

def generate_password(n):
    d = input('Какова длина одного пароля?  ')
    while not d.isdigit():                               # проверка введенного числа
        d = input('Нужно ввести целое число ')
    dig = input('Включать ли цифры 0123456789? да/нет (1/0) ').strip()
    upp = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? да/нет (1/0) ').strip()
    low = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? да/нет (1/0) ').strip()
    simb = input('Включать ли символы !#$%&*+-=?@^_? да/нет (1/0) ').strip()
    simb2 = input('Исключать ли неоднозначные символы il1Lo0O? да/нет (1/0) ').strip()
    chars = ''                   # все символы, которые могут быть в пароле
    if (dig.lower() == 'да') or (dig.lower() == '1'):
        chars = chars + digits
    if (upp.lower() == 'да') or (upp.lower() == '1'):
        chars = chars + uppercase_letters
    if (low.lower() == 'да') or (low.lower() == '1'):
        chars = chars + lowercase_letters
    if (simb.lower() == 'да') or (simb.lower() == '1'):
        chars = chars + punctuation
    if (simb2.lower() == 'да') or (simb2.lower() == '1'):
        for i in 'il1Lo0O':
            if i in chars:
                chars = chars.replace(i, '')

    while n > 0:
        password = sample(chars, int(d))
        print(*password, sep='')
        n = n - 1

n = input('Количество паролей для генерации?  ')
while not n.isdigit():                               # проверка введенного числа
    n = input('Нужно ввести целое число ')
generate_password(int(n))