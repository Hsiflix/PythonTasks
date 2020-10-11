'''
Task #890616
Обращение фрагмента
Кириченко Виктор
М3О-121М-20
'''

inp = input()
result = ''

first = inp.find('h')
last = inp.rfind('h')

if first == -1 or last == -1:
    result = inp
else:
    result+=inp[0:first+1]
    result+=inp[first+1:last][::-1]
    result+=inp[last:]

print(result)
