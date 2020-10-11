'''
Task #890089
"Сжатие" списка
Кириченко Виктор
М3О-121М-20
'''

spisok = input().split()

for i in spisok:
    if i == '0':
        spisok.remove('0')
        spisok.append('0')

print(' '.join(spisok))