import math

def t_eficaz():
    tpc = input('Digite a tensão de pico: ')
    tpc = float(tpc)
    result = round((tpc / math.sqrt(2)), 3)
    result = str(result)
    if '.' in result:
        size = len(result)
        result = list(result)
        for i in range (size):
            if '.' in result [i]:
                result[i] = ','
                break
    result = ''.join(result)
    print ('A tensão eficaz é ' + result + 'V\n')

def t_pico():
    tez = input('Digite a tensão eficaz: ')
    tez = float(tez)
    result = round((tez * math.sqrt(2)), 3)
    result = str(result)
    if '.' in result:
        size = len(result)
        result = list(result)
        for i in range (size):
            if '.' in result [i]:
                result[i] = ','
                break
    result = ''.join(result)
    print('A tensão de pico é ' + result + 'V\n')

while True:
    slct = input('Selecione o cálculo desejado:\n1. Tensão eficaz \n2. Tensão de pico\n')
    if slct == '1':
        t_eficaz()
    if slct == '2':
        t_pico()