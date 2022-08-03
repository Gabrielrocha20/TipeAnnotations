# Callable
from collections.abc import Callable

SomaInteiros = Callable[[int, int], int]


def executa(func: SomaInteiros, a: int, b: int) -> int:
    return func(a, b)


def soma(a: int, b: int) -> int:
    return a + b


executa(soma, 1, 2)

# Tipos opcionais


def soma1(x: float, y: float | None = None) -> float:
    if isinstance(y, int | float):
        return x + y
    return x + x
