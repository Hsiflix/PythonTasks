'''
Task #890691
Распределение фигуристов по правилам ISU
Кириченко Виктор
М3О-121М-20
'''

ch = 0
och = []

try:
    ch = int(input())
except ValueError:
    exit(1)

if ch<=0:
    print(0)
    exit(0)

for i in reversed(range(0,7)):
    if ch%i == 0 or ch%i == i-1:
        while ch>=i:
            och.append(i)
            ch-=i
        if ch > 0:
            och.append(ch)
        break
    for j in range(int(ch/i)+1):
        for k in range(int(ch/i)+1):
            if j*(i)+k*(i-1) == ch:
                stri = str(i-1)*k
                stri+= str(i)*j
                print('+'.join(stri))
                exit(0)

print('+'.join([str(i) for i in och])[::-1])
