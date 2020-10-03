'''
Task #889099
Алфавит
Кириченко Виктор
М3О-121М-20
'''

import time
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    try:
        yield start
    finally:
        print('Время выполнения: {}'.format(time.time() - start))

class timer2:
    def __init__(self):
        self.start = 0
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Время выполнения: {} sec.'.format(time.time() - self.start))

inp = input('Введите первую последовательсть: ')
target = input('Введите целевую последовательность: ')
if len(inp)!=len(target):
    exit(1)

inp_ord = [ord(i) for i in inp]
tarb_ord = [ord(i) for i in target]

def step(string):
    i = len(string)
    if i == 1:
        while ord(string)<122:
            string = chr(ord(string)+1)
            inp_ord[len(inp_ord)-i] = ord(string)
            print(''.join([chr(k) for k in inp_ord]))
            assert ''.join([chr(k) for k in inp_ord]) != target
        return
    else:
        step(string[1:])
        while ord(string[0])<122:
            string = chr(ord(string[0])+1)+'a'*len(string[1:])
            inp_ord[len(inp_ord)-i] = ord(string[0])
            for l in range(len(inp_ord)-i+1, len(inp_ord)):
                inp_ord[l] = 97
            print(''.join([chr(k) for k in inp_ord]))
            if(''.join([chr(k) for k in inp_ord]) == target):
                return
            step(string[1:])

try:
    print(inp)
    with timer2() as t:
        step(inp)
except AssertionError:
    exit(0)
