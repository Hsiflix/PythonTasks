'''
Task #890641
Парты
Кириченко Виктор
М3О-121М-20
'''

ch_1 = 0
ch_2 = 0
ch_3 = 0

try:
    ch_1 = int(input())
    ch_2 = int(input())
    ch_3 = int(input())
except ValueError:
    exit(1)

if ch_1<0:
    ch_1 = 0
if ch_2<0:
    ch_2 = 0
if ch_3<0:
    ch_3 = 0

print(int((ch_1+1)/2)+int((ch_2+1)/2)+int((ch_3+1)/2))
