##    Шифр Цезаря 🌶️🌶️🌶️🌶️_  Версия 2 _ Русский Язык и Английский язык ч/з поиск в СТРОКЕ

def shifr_tsezarya():
    alfavit_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'*20
    alfavit_ru_big = alfavit_ru.upper()
    alfavit_eng = 'abcdefghijklmnopqrstuvwxyz'*20
    alfavit_eng_big = alfavit_eng.upper()
    d = input('шифрование(1) или дешифрование(2)?  ').strip()
    while not d.isdigit() or d not in ('1', '2'):  # проверка введенного числа
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
            for i in stroka:            # строка нужно шифровать с шагом k
                if i.isupper():
                    j = alfavit_ru_big.find(i)
                    print(alfavit_ru_big[j + k], end='')
                elif i in ",.:;!? #$%&*+'-=@^_\" 0123456789":
                    print(i, end='')
                else:
                    j = alfavit_ru.find(i)
                    print(alfavit_ru[j + k], end='')

        else:
            for i in stroka:             # дешифрование, строка закодирована
                if i.isupper():
                    j = alfavit_ru_big.rfind(i)
                    print(alfavit_ru_big[j - k], end='')
                elif i in ",.:;!? #$%&*+'-=@^_\" 0123456789":
                    print(i, end='')
                else:
                    j = alfavit_ru.rfind(i)
                    print(alfavit_ru[j - k], end='')

    if yaz.lower() == 'eng':
        if d == 1:
            for i in stroka:             # строка нужно шифровать с шагом k
                if i.isupper():
                    j = alfavit_eng_big.find(i)
                    print(alfavit_eng_big[j + k], end='')
                elif i in ",.:;!? #$%&*+'-=@^_\" 0123456789":
                    print(i, end='')
                else:
                    j = alfavit_eng.find(i)
                    print(alfavit_eng[j + k], end='')

        else:
            for i in stroka:           # дешифрование, строка закодирована
                if i.isupper():
                    j = alfavit_eng_big.rfind(i)
                    print(alfavit_eng_big[j - k], end='')
                elif i in ",.:;!? #$%&*+'-=@^_\" 0123456789":
                    print(i, end='')
                else:
                    j = alfavit_eng.rfind(i)
                    print(alfavit_eng[j - k], end='')

shifr_tsezarya()