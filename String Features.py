
import string

print(string.punctuation)              # пунктуация  !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(string.digits)                   # числа  0123456789
print(string.ascii_uppercase)          # заглавные  ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)          # строчные  abcdefghijklmnopqrstuvwxyz
print(string.ascii_letters)            # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.hexdigits)                # 0123456789abcdefABCDEF
print(string.octdigits)                # 01234567
print(string.printable)                # цифры+строчные+заглавные+пунктуация  0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

print('Строка string.whitespace')
print(string.whitespace)               # все символы ASCII, которые считаются пробелами.