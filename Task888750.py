'''
Task #888750
Разворот последовательности
Кириченко Виктор
М3О-121М-20
'''

def my_input():
    try:
        ch = int(input('Введите число: '))
        if ch != 0:
            my_input()
        print(ch)
    except ValueError:
        exit(1)

my_input()
