pilha_resultado = []


def calculadora(npr: list) -> int | float:
    global pilha_resultado
    for item in npr:
        match item:
            case int() | float():
                empilhar(item)
            case '+':
                empilhar(somar())
            case '-':
                empilhar(subtrair())
            case '*':
                empilhar(multiplicar())
            case '/':
                empilhar(dividir())
    if len(pilha_resultado) != 1:
        raise ValueError
    return pilha_resultado[0]


def somar(a: int | float = None, b: int | float = None) -> int | float:
    operandos = desempilhar()
    return operandos[0] + operandos[1]


def multiplicar(a: int | float = None, b: int | float = None) -> int | float:
    operandos = desempilhar()
    return operandos[0] * operandos[1]


def dividir(a: int | float = None, b: int | float = None) -> int | float:
    operandos = desempilhar()
    if operandos[1] != 0:
        return operandos[0] / operandos[1]
    raise ZeroDivisionError


def subtrair(a: int | float = None, b: int | float = None) -> int | float:
    operandos = desempilhar()
    return operandos[0] - operandos[1]


def empilhar(numero: int | float):
    global pilha_resultado
    pilha_resultado.append(numero)


def desempilhar() -> list:
    global pilha_resultado
    b = pilha_resultado.pop()
    a = pilha_resultado.pop()
    operandos = [a, b]
    return operandos
