'''
Task #890716
Пробежка по утрам
Кириченко Виктор
М3О-121М-20
'''

ch_1 = 0
ch_2 = 0
count = 0

try:
    ch_1 = int(input())
    ch_2 = int(input())
except ValueError:
    exit(1)

while ch_1<ch_2:
    ch_1*=1.1
    count+=1

print(count+1)
