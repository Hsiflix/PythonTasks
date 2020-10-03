'''
Task #889099
Алфавит
Кириченко Виктор
М3О-121М-20
'''

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
            assert ''.join([chr(k) for k in inp_ord]) != target
            step(string[1:])
try:
    print(inp)
    step(inp)
except AssertionError:
    exit(0)
