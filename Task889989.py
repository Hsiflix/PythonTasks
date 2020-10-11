'''
Task #889989
Сортировка подсчетом
Кириченко Виктор
М3О-121М-20
'''

mass = []
res_string = ''

def Counter(list_object):
    result = {}
    for i in list_object:
        result.setdefault(i, 0)
        result[i]+=1
    return result

try:
    _ = input()
    mass = [int(i) for i in _.split()]
except ValueError:
    exit(1)

if len(mass) == 0:
    print()
    exit(0)

max_ = max(mass)
min_ = min(mass)
dictonary = Counter(mass)

for i in range(min_, max_+1):
    if dictonary.get(i,False):
        res_string+=str(i)*dictonary[i]

print(' '.join(res_string))
