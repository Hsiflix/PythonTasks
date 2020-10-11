'''
Task #890114
Ферзи
Кириченко Виктор
М3О-121М-20
'''

list_x = []
list_y = []

try:
    for i in range(8):
        _ = input().split()
        if len(_) != 2:
            raise ValueError
        list_x.append(int(_[0]))
        list_y.append(int(_[1]))
    if max(list_x)>8:
        raise ValueError
    if max(list_y)>8:
        raise ValueError
    if min(list_x)<0:
        raise ValueError
    if min(list_y)<0:
        raise ValueError
except ValueError:
    exit(1)

for i in list_x:
    if list_x.count(i) > 1:
        print('YES')
        exit(0)

for i in list_y:
    if list_y.count(i) > 1:
        print('YES')
        exit(0)

for i in range(8):
    for j in range(8):
        if i != j:
            if abs(list_x[i]-list_x[j])==abs(list_y[i]-list_y[j]):
                print('YES')
                exit(0)

print('NO')