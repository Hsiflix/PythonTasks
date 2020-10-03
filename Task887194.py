'''
Task #887194
Спички
Кириченко Виктор
М3О-121М-20
'''

x1 = [0,0,0]
x2 = [0,0,0]

inp = input()
while not inp.isnumeric():
    inp = input('Try again! ')
x1[0] = int(inp)
inp = input()
while not inp.isnumeric():
    inp = input('Try again! ')
x2[0] = int(inp)
inp = input()
while not inp.isnumeric():
    inp = input('Try again! ')
x1[1] = int(inp)
inp = input()
while not inp.isnumeric():
    inp = input('Try again! ')
x2[1] = int(inp)
inp = input()
while not inp.isnumeric():
    inp = input('Try again! ')
x1[2] = int(inp)
inp = input()
while not inp.isnumeric():
    inp = input('Try again! ')
x2[2] = int(inp)


pos = [1,2,3]

if x1[0]>x1[1]:
    pos[0], pos[1] = pos[1], pos[0]
    x1[0], x1[1] = x1[1], x1[0]
    x2[0], x2[1] = x2[1], x2[0]
if x1[1]>x1[2]:
    pos[1], pos[2] = pos[2], pos[1]
    x1[1], x1[2] = x1[2], x1[1]
    x2[1], x2[2] = x2[2], x2[1]
if x1[0]>x1[1]:
    pos[0], pos[1] = pos[1], pos[0]
    x1[0], x1[1] = x1[1], x1[0]
    x2[0], x2[1] = x2[1], x2[0]

#print('x1: {}'.format(x1))
#print('x2: {}'.format(x2))
#print('pos: {}'.format(pos))

lenghts = [x2[0]-x1[0], x2[1]-x1[1], x2[2]-x1[2]]
#print('lenghts: {}'.format(lenghts))

distants = [x1[1]-x2[0], x1[2]-x2[1]]
#print(distants)

if max(distants) <= 0:
    print(0)
elif lenghts[0]>=distants[1] and not (lenghts[2]>=distants[0] and pos[2]<pos[0]):
    print(pos[0])
elif lenghts[2]>=distants[0]:
    print(pos[2])
else: print(-1)
