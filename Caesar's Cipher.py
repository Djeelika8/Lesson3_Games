##    Шифр Цезаря 🌶️🌶️🌶️🌶️_  Версия 1 _ Русский Язык и Английский язык по КОЛЬЦУ

def shifr_tsezarya():
    d = input('шифрование(1) или дешифрование(2)?  ').strip()
    while not d.isdigit() or  d not in ('1', '2'):  # проверка введенного числа
        d = input('Нужно ввести целое число 1 или 2 ')
    d = int(d)
    k = input('Каков шаг сдвига вправо? ').strip()
    while not k.isdigit():  # проверка введенного числа
        k = input('Нужно ввести целое число ')
    k = int(k)
    yaz = input('язык алфавита русский или английский? (ru/eng)  ').strip()
    while yaz.lower() not in ('ru','eng'):
        yaz = input('Так какой язык алфавита (ru/eng)?  ').strip()
    stroka = input('Введите строку: ')

    if yaz.lower() == 'ru':
        if d == 1:
            for i in stroka:                                  # строка нужно шифровать с шагом k
                if i.isupper():
                    if ord(i.lower()) + k > 1103:
                        print((chr(ord(i.lower()) + k - 32)).upper(),end='')
                    else:
                        print((chr(ord(i.lower()) + k)).upper(), end='')
                elif i in ",.:;!? #$%&*+'-=@^_\" 0123456789":
                    print(i, end='')
                else:
                    if ord(i) + k > 1103:
                        print(chr(ord(i) + k - 32), end='')     # 32-это диапазон Алфавита, от а(1072) до я(1103) вкл.
                    else:
                        print(chr(ord(i) + k), end='')
        else:
            for i in stroka:  # дешифрование, строка закодирована
                if i.isupper():
                    if ord(i.lower()) - k < 1072:
                        print((chr(ord(i.lower()) - k + 32)).upper(), end='')
                    else:
                        print((chr(ord(i.lower()) - k)).upper(), end='')
                elif i in ",.:;!? #$%&*+'-=@^_\" 0123456789":
                    print(i, end='')
                else:
                    if ord(i) - k < 1072:
                        print(chr(ord(i) - k + 32), end='')
                    else:
                        print(chr(ord(i) - k), end='')
    if yaz.lower() == 'eng':
        if d == 1:
            for i in stroka:                                    # строка нужно шифровать с шагом k
                if i.isupper():
                    if ord(i.lower()) + k > 122:                # больше z
                        print((chr(ord(i.lower()) + k - 26)).upper(),end='')
                    else:
                        print((chr(ord(i.lower()) + k)).upper(), end='')
                elif i in ",.:;!? #$%&*+'-=@^_\" 0123456789":
                    print(i, end='')
                else:
                    if ord(i) + k > 122:
                        print(chr(ord(i) + k - 26), end='')    # 32-это диапазон Алфавита, от а(1072) до я(1103) вкл.
                    else:
                        print(chr(ord(i) + k), end='')
        else:
            for i in stroka:  # дешифрование, строка закодирована
                if i.isupper():
                    if ord(i.lower()) - k < 97:                 # меньше 'a'
                        print((chr(ord(i.lower()) - k + 26)).upper(), end='')
                    else:
                        print((chr(ord(i.lower()) - k)).upper(), end='')
                elif i in ",.:;!? #$%&*+'-=@^_\" 0123456789":
                    print(i, end='')
                else:
                    if ord(i) - k < 97:
                        print(chr(ord(i) - k + 26), end='')
                    else:
                        print(chr(ord(i) - k), end='')

shifr_tsezarya()