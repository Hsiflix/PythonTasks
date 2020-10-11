'''
Task #889888
Гражданская оборона(*)
Кириченко Виктор
М3О-121М-20
'''

def select_l_r(list_object, position):
    l = [-1, -1]
    for j in reversed(range(position)):
        if list_object[j][0]=='B':
            l[0] = list_object[j][1]
            l[1] = list_object[j][2]
            break
    r = [-1, -1]
    for j in range(len(list_object))[position:]:
        if list_object[j][0]=='B':
            r[0] = list_object[j][1]
            r[1] = list_object[j][2]
            break
    return [l, r]

s_dist = []
b_dist = []
list_ = []
result = []

try:
    s_count = int(input())
    if s_count <=0:
        raise ValueError
    _ = input()
    s_dist = [int(i) for i in _.split()]
    if len(s_dist) != s_count:
        raise ValueError
    b_count = int(input())
    if b_count <=0:
        raise ValueError
    _ = input()
    b_dist = [int(i) for i in _.split()]
    if len(b_dist) != b_count:
        raise ValueError
except ValueError:
    exit(1)

for i in range(len(s_dist)):
    list_.append(['S', i, s_dist[i]])

for i in range(len(b_dist)):
    list_.append(['B', i, b_dist[i]])

list_.sort(key=lambda val: val[2])

for i in range(len(list_)):
    if list_[i][0]=='S':
        l_r = select_l_r(list_, i)
        if l_r[0][0]==-1:
            result.append([list_[i][1], l_r[1][0]+1])
        elif l_r[1][0]==-1:
            result.append([list_[i][1], l_r[0][0]+1])
        elif abs(list_[i][2]-l_r[0][1])>abs(list_[i][2]-l_r[1][1]):
            result.append([list_[i][1], l_r[1][0]+1])
        else:
            result.append([list_[i][1], l_r[0][0]+1])

result.sort(key=lambda val: val[0])

print(' '.join([str(i[1]) for i in result]))
