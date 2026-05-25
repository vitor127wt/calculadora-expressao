
pilha_operadores = []

pilha_saida = []


PESOS = {
    '+': 1,
    '-': 1,
    '/': 2,
    '*': 2,
}


def conversora_npr(expressao: list) -> list:
    global pilha_saida
    for item in expressao:
        if isinstance(item, (int, float)):
            numero(item)
            continue
        if item in '+-*/^':
            operador(item)
            continue
        if item in '({[':
            abrir_escopo(item)
            continue
        if item in ')}]':
            fechar_escopo(item)
            continue
    if pilha_operadores != []:
        return despejar_operadores()

    return pilha_saida


def numero(num: int | float):
    global pilha_saida
    pilha_saida.append(num)


def operador(op: str):
    aberturas = r'([{'
    global pilha_operadores
    if not pilha_operadores:
        pilha_operadores.append(op)

        return 0
    if pilha_operadores[0] in aberturas:
        pilha_operadores.insert(0, op)

        return 0
    if PESOS[op] >= PESOS[pilha_operadores[0]]:
        pilha_saida.append(pilha_operadores.pop(0))
        pilha_operadores.insert(0, op)

        return 0
    else:
        pilha_operadores.insert(0, op)

        return 0


def abrir_escopo(escopo):
    pilha_operadores.insert(0, escopo)


def fechar_escopo(escopo):
    global pilha_operadores
    match escopo:
        case ')':
            fechar_parentese()
        case ']':
            fechar_colchete()
        case '}':
            fechar_chave()


def fechar_parentese():
    global pilha_operadores
    global pilha_saida
    for index, item in enumerate(pilha_operadores):
        if item != '(':
            pilha_saida.append(item)
            # pilha_saida.append(pilha_operadores.pop(0))
        else:
            limpar_operadores(index)
            break


def fechar_colchete():
    global pilha_operadores
    global pilha_saida
    for index, item in enumerate(pilha_operadores):
        if item != '[':
            pilha_saida.append(item)
            # pilha_saida.append(pilha_operadores.pop(0))
        else:
            limpar_operadores(index)
            break


def fechar_chave():
    global pilha_operadores
    global pilha_saida
    for index, item in enumerate(pilha_operadores):
        if item != '{':
            pilha_saida.append(item)
            # pilha_saida.append(pilha_operadores.pop(0))
        else:
            limpar_operadores(index)
            break


def limpar_operadores(index):
    for _ in range(index + 1):
        pilha_operadores.pop(index)
        index -= 1


def despejar_operadores():
    for item in pilha_operadores:
        if item in "}()[]{":
            return []
        pilha_saida.append(item)
    return pilha_saida
