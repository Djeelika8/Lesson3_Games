# ДЕШЕФРОВКА, МЫ НЕ ЗНАЕМ СДВИГ
# Hawnj pk swhg xabkna ukq nqj.
# Learn to walk before you run.
# Считайте, что n ∈[0;25].


def shifr_tsezarya(k, stroka, yaz):
    alfavit_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'*20
    alfavit_ru_big = alfavit_ru.upper()
    alfavit_eng = 'abcdefghijklmnopqrstuvwxyz'*20
    alfavit_eng_big = alfavit_eng.upper()

    if yaz.lower() == 'ru':
        for i in stroka:                       # дешифрование, строка закодирована
            if i.isupper():
                j = alfavit_ru_big.rfind(i)
                print(alfavit_ru_big[j - k], end='')
            elif i in ",.:;!? #$%&*+'-=@^_\" 0123456789":
                print(i, end='')
            else:
                j = alfavit_ru.rfind(i)
                print(alfavit_ru[j - k], end='')

    if yaz.lower() == 'eng':
        for i in stroka:                       # дешифрование, строка закодирована
            if i.isupper():
                j = alfavit_eng_big.rfind(i)
                print(alfavit_eng_big[j - k], end='')
            elif i in ",.:;!? #$%&*+'-=@^_\" 0123456789":
                print(i, end='')
            else:
                j = alfavit_eng.rfind(i)
                print(alfavit_eng[j - k], end='')

yaz = input('язык алфавита русский или английский? (ru/eng)  ').strip()
while yaz.lower() not in ('ru','eng'):
    yaz = input('Так какой язык алфавита (ru/eng)?  ').strip()
stroka = input('Введите строку: ')
for i in range (1, 26):
    shifr_tsezarya(i, stroka, yaz)
    print()