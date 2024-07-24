from typing import Any, Iterable, List, Sequence, Union, Tuple, Dict, NewType, Callable
# Primitivos
numero: int = 10
flutuante: float = 10.5
booleano: bool = True
string: str = 'Artur Pedro'

# Sequências
lista: List[int] = [1, 2, 3]
lista_str_int: List[Union[int, str]] = [1, 2, 3, 'Luiz']
tupla: Tuple[int, int, int, str] = (1, 2, 3, 'Artur')

# Dicionario e conjuntos
MeuDict = Dict[str, Union[str, int, List[int]]] # Alias
pessoa: Dict[str, Union[str, int]] = {'nome': 'Artur Pedro', 'sobrenome': 'Moreira', 'idade': 30}
pessoa2: MeuDict = {'nome': 'Artur Pedro', 'sobrenome': 'Moreira', 'idade': 30, 'l': [1, 2]}

UserId = NewType('UserId', int)
user_id = UserId(32564486)

def retorna_funcao(funcao: Callable[[int, int], int]) -> Callable:
    return funcao

def soma(x:int, y:int) -> int:
    return x + y

print(retorna_funcao(soma)(10, 20))

class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade

    def fala(self) -> None:
        print(f'{self.nome} {self.sobrenome} esta falando')

def iterar(sequecia: Sequence[int]):
    return [x*2 for x in sequecia]

def iterar2(sequecia: Iterable[int]):
    return [x*2 for x in sequecia]

print(iterar([1, 2, 3]))
print(iterar((1, 2, 3)))
print(iterar2((1, 2, 3)))
print(iterar2((1, 2, 3)))