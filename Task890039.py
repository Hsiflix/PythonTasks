'''
Task #890039
Больше соседей
Кириченко Виктор
М3О-121М-20
'''

mass = []
count = 0

try:
    _ = input()
    mass = [int(i) for i in _.split()]
except ValueError:
    exit(1)

if len(mass)<=2:
    print(count)
    exit(0)

for i in range(len(mass)-2):
    if mass[i+1]>mass[i] and mass[i+1]>mass[i+2]:
        count+=1

print(count)
