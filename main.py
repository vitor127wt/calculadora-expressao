from montadora import montadora
from validadora import validadora
from conversora import conversora_npr
from calculadora import calculadora

TESTE = '10 + [4 * (6 - {8 / 2})] - {9 / (3 * 2)} + [12 / (4 * 3)]'  # 17.5


def entrada_formatada():
    print('-->', sep='', end='')
    # entrada = input()
    entrada = TESTE
    return entrada


while True:
    entrada = entrada_formatada()
    entrada = montadora(entrada)
    if not validadora(entrada):
        print('Expressão invalida')
        break
    npr = conversora_npr(entrada)
    resultado = calculadora(npr)
    print(resultado)
    break
