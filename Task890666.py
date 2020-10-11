'''
Task #890666
Номер числа Фибоначчи
Кириченко Виктор
М3О-121М-20
'''

ch = 0
a = 0
b = 1
count = 0

try:
    ch = int(input())
except ValueError:
    exit(1)

if ch<0:
    print(-1)
    exit(0)
elif ch == 0:
    print(0)
    exit(0)
elif ch == 1:
    print(1)
    exit(0)

while a<ch:
    a, b = b, a+b
    count+=1

if a == ch:
    print(count)
else:
    print(-1)
