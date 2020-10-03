'''
Task #888775
Алгоритм Евклида
Кириченко Виктор
М3О-121М-20
'''

def gcd(a, b):
    if a == 0 or b == 0:
        print(max(a,b))
        return max(a,b)
    elif a > b:
        gcd(b, a%b)
    elif a < b:
        gcd(a, b%a)
    else:
        print(a)
        return a

try:
    _a = int(input('Введите x: '))
    _b = int(input('Введите y: '))
except ValueError:
    exit(1)

gcd(_a, _b)
