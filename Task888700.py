'''
Task #888700
Сумма факториалов
Кириченко Виктор
М3О-121М-20
'''

try:
    ch = int(input('Введите число: '))
except ValueError:
    exit(1)

res = 0
znach = 1
for i in range(1, ch+1):
    znach *= i
    res += znach

print(1 if res == 0 else res)
