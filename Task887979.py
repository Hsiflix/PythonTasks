'''
Task #887979
Удаление каждого третьего
Кириченко Виктор
М3О-121М-20
'''

string = input('Введите строку для удаления каждого третьего: ')
print(''.join([string[i] if i%3 != 0 else '' for i in range(len(string))]))
