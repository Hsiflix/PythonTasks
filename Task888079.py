'''
Task #888079
Перестановка слов
Кириченко Виктор
М3О-121М-20
'''

string = input('Введите строку для переставовки: ')
split = string.split(' ')
if len(split) == 2:
    print('{} {}'.format(split[1], split[0]))
else: print(string)
