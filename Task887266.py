
'''
Task #887266
Ход короля
Кириченко Виктор
М3О-121М-20
'''

try:
    x1_1 = int(input('Введите число координату х1 начала: '))
    if not 1<=x1_1<=8:
        raise ValueError
    x2_1 = int(input('Введите число координату х2 начала: '))
    if not 1<=x2_1<=8:
        raise ValueError
    x1_2 = int(input('Введите число координату х1 цели: '))
    if not 1<=x1_2<=8:
        raise ValueError
    x2_2 = int(input('Введите число координату х2 цели: '))
    if not 1<=x2_2<=8:
        raise ValueError
except ValueError:
    exit(1)

if abs(x1_2-x2_1) < 2 and abs(x2_2-x2_1) < 2:
    print('YES')
else: print('NO')
