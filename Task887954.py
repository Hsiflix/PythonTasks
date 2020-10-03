'''
Task #887954
Количество палиндромов
Кириченко Виктор
М3О-121М-20
'''

try:
    string = int(input('Введите строку для нахождения кол-ва палиндромов: '))
    if string < 1 or string > 100000:
        raise ValueError
except ValueError:
    exit(1)

palindroms = []

for x in range(1,10):
    palindroms.append(x)
    palindroms.append(int(str(x)+str(x)))
    for y in range(0,10):
        palindroms.append(int(str(x)+str(y)+str(x)))
        palindroms.append(int(str(x)+str(y)+str(y)+str(x)))
        for z in range(0,10):
            palindroms.append(int(str(x)+str(y)+str(z)+str(y)+str(x)))

palindroms.sort()

count = 0
for i in palindroms:
    if i <= string:
        count+=1
    else:
        break

print(count)
