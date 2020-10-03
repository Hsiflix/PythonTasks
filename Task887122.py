'''
Task #887122
Наименьшее расстояние между локальными максимумами
Кириченко Виктор
М3О-121М-20
'''

def data_input():
    data = []
    while True:
        inp = input('Введите очередное число, 0 - конец ввода: ')
        if inp.isdecimal() or (inp[0] == '-' and inp[1:].isdecimal()):
            data.append(int(inp))
        else:
            print('Вы ввели неверное число, повторите попытку или введите 0, чтобы закончить ввод.')
            continue
        if int(inp) == 0:
            break
    return data

def min_dist_between_loc_max(data):
    #print(data)
    if len(data) < 5:
        return 0
    listLocMax = []
    for i in range(len(data)-2):
        if data[i+1] > data[i] and data[i+1] > data[i+2]:
            listLocMax.append(i+1)
    #print(listLocMax)
    if len(listLocMax) < 2:
        return 0
    listDist = [listLocMax[i+1]-listLocMax[i] for i in range(len(listLocMax)-1)]
    return min(listDist)


print(min_dist_between_loc_max(data_input()))
#print(min_dist_between_loc_max([1,2,1,1,2,1,2,1,0]))
#print(min_dist_between_loc_max([1,2,1,1,1,1,2,1,0]))
#print(min_dist_between_loc_max([1,2,0]))
#print(min_dist_between_loc_max([1,1,1,1,1,1,1,0]))
#print(min_dist_between_loc_max([1,1,1,2,1,1,1,0]))