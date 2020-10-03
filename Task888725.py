'''
Task #888725
Только квадраты
Кириченко Виктор
М3О-121М-20
'''

from math import sqrt

def is_square(a):
    if a != 0:
        return sqrt(a).is_integer()
    return False

output = ''

try:
    ch = -1
    while ch != 0:
        ch = int(input('Введите число: '))
        if is_square(ch):
            output = '{} {}'.format(ch, output)
except ValueError:
    exit(1)

print(output if len(output)>0 else 0)
