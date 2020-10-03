'''
Task #888800
Принадлежит ли точка области?
Кириченко Виктор
М3О-121М-20
'''
from math import sqrt

def isPointInArea(x, y):
    h = sqrt((x+1.)**2 + (y-1.)**2)
    inCircle = h <= 2 #Принадлежит кругу
    #print(inCircle)
    upper1line = x>=-y
    under1line = x<=-y
    upper2line = x<=float(y)/2.-1.
    under2line = x>=float(y)/2.-1.
    #print(upper1line)
    #print(under1line)
    #print(upper2line)
    #print(under2line)
    return (inCircle and upper1line and upper2line) or \
        (not inCircle and under1line and under2line and y>=-3.5)

try:
    _x = int(input('Введите x: '))
    _y = int(input('Введите y: '))
except ValueError:
    exit(1)

print('YES' if isPointInArea(_x, _y) else 'NO')
