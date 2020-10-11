'''
Task #890741
Второй максимум
Кириченко Виктор
М3О-121М-20
'''

mass = []

try:
    mass.append(int(input()))
    while mass[-1] != 0:
        mass.append(int(input()))
except ValueError:
    exit(1)

mass.remove(0)
if len(mass)<2:
    exit(0)

mass.remove(max(mass))
print(max(mass))
