"""
Type annotations em Python
Observação: estou usando o Python 3.10.

O que é Type Annotation? São partes do código usadas para indicar tipos de
dados em locais como: variáveis, parâmetros e retornos de funções e métodos.
Em Python isso é usado para documentação e ajuda com auto completar dos
editores, visto que a linguagem não impede a execução do código mesmo se as
anotações estiverem incorretas."""

# Anotações básicas em variáveis
uma_string: str = 'Um valor'
um_inteiro: int = 123456
um_float: float = 1.23
um_boolean: bool = True
um_set: set = {1, 2, 3}  # mais sobre a seguir
uma_lista: list = []  # mais sobre a seguir
um_dicionário: dict = {}  # mais sobre a seguir
# Parâmetros de funções e métodos
# x e y devem ser inteiros
# z deve ser um número de ponto flutuante
# obs.: float aceita tanto int como float,
# int aceita apenas int.
# Para informar o retorno da função, use:
# `-> tipo` antes dos dois pontos, como em
# def () -> None: para funções sem retorno


def soma(x: int, y: int, z: float) -> float:
    return x + y + z
