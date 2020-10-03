'''
Task #887146
МКАД
Кириченко Виктор
М3О-121М-20
'''

import time
from typing import Final

MRR: Final = 109

inp = input('Введите скорость (км./ч.): ')
while(not (inp.isdecimal() or (inp[0] == '-' and inp[1:].isdecimal()))):
    inp = input('Введите скорость (км./ч.): ')
v = int(inp)
inp = input('Введите время (ч.): ')
while(not (inp.isdecimal())):
    inp = input('Введите время (ч.): ')
t = int(inp)

#print('Скорость: {}, Время: {}.'.format(v,t))
#--------------------------------------------------------------------------
start_time = time.time()
#--------------------------------------------------------------------------

stoppingPoint = v*t % MRR
print(stoppingPoint)
#print('Байкер остановится на {}-м километре'.format(stoppingPoint))

#--------------------------------------------------------------------------
#print("Время выполнения: {} сек.".format(time.time() - start_time))

