# fornecedores/utils.py

import re

def validar_cnpj(cnpj):
    cnpj = re.sub(r'\D', '', cnpj)  # Remove todos os caracteres não numéricos

    if len(cnpj) != 14:
        return False

    def calcular_digito(cnpj, peso):
        soma = 0
        for i, num in enumerate(cnpj[:peso]):
            soma += int(num) * (peso + 1 - i)
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    primeiro_digito = calcular_digito(cnpj, 12)
    segundo_digito = calcular_digito(cnpj, 13)

    return cnpj[-2:] == f"{primeiro_digito}{segundo_digito}"
