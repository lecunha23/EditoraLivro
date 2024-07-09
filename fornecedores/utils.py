
from validate_docbr import CNPJ
import re

def validar_cnpj(cnpj):
    cnpj_validator = CNPJ()
    return cnpj_validator.validate(cnpj)

    def calcular_digito(cnpj, peso):
        soma = 0
        for i, num in enumerate(cnpj[:peso]):
            soma += int(num) * (peso + 1 - i)
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    primeiro_digito = calcular_digito(cnpj, 12)
    segundo_digito = calcular_digito(cnpj, 13)

    return cnpj[-2:] == f"{primeiro_digito}{segundo_digito}"
