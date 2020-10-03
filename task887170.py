'''
Task #887170
Сложное уравнение
Кириченко Виктор
М3О-121М-20
'''
print('Решение уравнения (ax+b)/(cx+d)=0.')
try:
    a = int(input('Введите число a: '))
    b = int(input('Введите число b: '))
    c = int(input('Введите число c: '))
    d = int(input('Введите число d: '))
except ValueError:
    exit(1)
if a==0 and b==0:
    print('INF')
elif a==0 or b*c == d*a:
    print('NO')
else:
    resh = -b/a
    print(int(resh) if resh.is_integer() else 'NO')
