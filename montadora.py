

def montadora(expressao: str) -> list:
    expressao = expressao.replace(' ', '')
    expressao = list(expressao)
    saida = []
    numero_atual = ''
    for index, char in enumerate(expressao):
        if char.isdigit() or char == '.':
            numero_atual += char
            if index == (len(expressao) - 1):
                saida.append(
                    int(numero_atual) if '.' not in numero_atual else float(numero_atual))

        else:
            if numero_atual:
                saida.append(
                    int(numero_atual) if '.' not in numero_atual else float(numero_atual))
            saida.append(char)
            numero_atual = ''
    return saida
