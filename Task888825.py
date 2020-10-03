'''
Task #888825
Принадлежит ли точка квадрату?
Кириченко Виктор
М3О-121М-20
'''

def isPointInSquare(x, y):
    return abs(x)+abs(y)<=1.

try:
    _x = float(input('Введите x: '))
    _y = float(input('Введите y: '))
except ValueError:
    exit(1)

print('YES' if isPointInSquare(_x, _y) else 'NO')
