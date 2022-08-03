
# Type aliases
# Isso são type aliases
ListaInteiros = list[int]
DictListaInteiros = dict[str, ListaInteiros]

um_dict_de_listas: DictListaInteiros = {
    "A": [1, 2],
    "B": [3, 4],
    "C": [5, 6],
}
# Union types
string_e_inteiros: str | int = 1  # Union
string_e_inteiros = "A"  # Sem erros
string_e_inteiros = 2  # Sem erros
