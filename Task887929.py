'''
Task #887929
Идеальный исполнитель
Кириченко Виктор
М3О-121М-20
'''

try:
    ch1 = int(input('Введите число A: '))
    ch2 = int(input('Введите число B: '))
    if ch2>=ch1:
        raise ValueError
except ValueError:
    exit(1)

while ch1 > ch2:
    if ch1%2==1:
        print('-1')
        ch1 = ch1 - 1
    elif ch1/2 >= ch2:
        print(':2')
        ch1 = ch1/2
    elif ch1 > ch2:
        print('-1')
        ch1 = ch1 - 1
