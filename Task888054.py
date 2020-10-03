'''
Task #888054
Замена фрагмента
Кириченко Виктор
М3О-121М-20
'''

string = input('Введите строку для замены фрагмента: ')

symHl = string.find('h')
symHr = string.rfind('h')

if symHl != -1 and symHr != -1 and symHl != symHr:
    part1 = string[0:symHl+1]
    part2 = string[symHl+1:symHr]
    part3 = string[symHr:]
    part2 = part2.replace('h','H')
    print(''+part1+part2+part3)
else:
    print(string)
