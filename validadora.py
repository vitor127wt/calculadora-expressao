OPERADORES = '+-/*^'
ABERTURAS = '({['
FECHAMENTOS = ')}]'


def validadora(expressao: list) -> bool:
    for index, item in enumerate(expressao):
        match item:
            case int() | float():
                if not val_num(index, expressao):
                    return False
                continue
            case str():
                if not val_operadores_aberturas_fechamentos(index, expressao):
                    return False
                continue
    return True if val_escopos(expressao) else False

# Chama as funções de validação de caracteres a esquertda e direita de numeros


def val_num(index: int, expressao: list) -> bool:
    direita = str(expressao[index + 1]
                  ) if index != len(expressao) - 1 else None
    esquerda = str(expressao[index - 1]) if index != 0 else None
    if direita is not None and direita in ABERTURAS:
        return False
    if esquerda is not None and esquerda in FECHAMENTOS:
        return False
    return True

# Chama as funções que validam caracteres a esquerda e a direita de operadores


def val_operadores_aberturas_fechamentos(index, expressao) -> bool:
    '''Chama as funções de validação de operadores, aberturas e fechamentos'''
    caracter = expressao[index]
    match caracter:
        case op if op in OPERADORES:
            if not val_operador(expressao, index):
                return False
            return True
        case ab if ab in ABERTURAS:
            if not val_aberturas(expressao, index):
                return False
            return True
        case fc if fc in FECHAMENTOS:
            if not val_fechamentos(expressao, index):
                return False
            return True
    return False


def val_operador(expressao: list, index: int) -> bool:
    '''Valida os acaraceteres adjacentes ao operador'''
    direita = str(expressao[index + 1]
                  ) if index != len(expressao) - 1 else None
    esquerda = str(expressao[index - 1]) if index != 0 else None
    if expressao[index] == 0 or index == len(expressao) - 1:
        return False
    if direita in OPERADORES or esquerda in OPERADORES:
        return False
    if direita in FECHAMENTOS or esquerda in ABERTURAS:
        return False
    return True


def val_aberturas(expressao: list, index: int) -> bool:
    direita = str(expressao[index + 1]
                  ) if index != len(expressao) - 1 else None
    esquerda = str(expressao[index - 1]) if index != 0 else None
    if index == len(expressao) - 1:
        return False
    if direita in OPERADORES or direita in FECHAMENTOS:
        return False
    if esquerda is not None and esquerda in FECHAMENTOS:
        return False
    return True


def val_fechamentos(expressao: list, index: int) -> bool:
    direita = str(expressao[index + 1]
                  ) if index != len(expressao) - 1 else None
    esquerda = str(expressao[index - 1]) if index != 0 else None
    if index == 0:
        return False
    if esquerda in ABERTURAS or esquerda in OPERADORES:
        return False
    if direita is not None and direita in ABERTURAS:
        return False
    return True


def val_escopos(expressao: list) -> bool:
    expressao = limpar_escopo(expressao)
    if len(expressao) % 2 != 0:
        return False
    while True:
        encontrei = False
        for index, item in enumerate(expressao):
            if index == len(expressao) - 1:
                if item in r'([{':
                    return False
            if item == '(' and expressao[index + 1] == ')':
                expressao.pop(index + 1)
                expressao.pop(index)
                encontrei = True
            if item == '[' and expressao[index + 1] == ']':
                expressao.pop(index + 1)
                expressao.pop(index)
                encontrei = True
            if item == r'{' and expressao[index + 1] == '}':
                expressao.pop(index + 1)
                expressao.pop(index)
                encontrei = True
        if not encontrei:
            return False
        if expressao == []:
            return True


def limpar_escopo(expressao: list) -> list:
    escopos = []
    for item in expressao:
        item = str(item)
        if item in '([{)]}':
            escopos.append(item)
    return escopos
