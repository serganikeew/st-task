""" 
С клавиатуры вводятся строка S, число N и символ C. Требуется создать строку, 
которая есть замена в введенной строке S символа с индексом N на символ C. 
Вывести новую строку на экран. Напечатать, отличается ли новая строка от исходной.
"""

s = input()
n = int(input())
c = input()
string = ''

string = s[:(n)] + c + s[(n + 1):]

print(string)

if string == s:
    print('Не отличается.')
else:
    print('Отличается.')
