'''
Task #890064
Количество совпадающих пар
Кириченко Виктор
М3О-121М-20
'''

def sum_(count):
    return sum(range(count))

def Counter(list_object):
    result = {}
    for i in list_object:
        result.setdefault(i, 0)
        result[i]+=1
    return result

spisok = []

try:
    _ = input()
    spisok = [int(i) for i in _.split()]
except ValueError:
    exit(1)

slovar = Counter(spisok)

summa = 0
for j in slovar.values():
    summa+=sum_(j)

print(summa)
