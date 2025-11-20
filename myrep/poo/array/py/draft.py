import random

class Foo:
    def __init__(self, x: int):
        self.x = x
    def __repr__(self) -> str:
        return f"Foo({self.x})"

    def __str__(self):
        return f"Foo({self.x})"

listaNumero: list[int] = []
listaObjeto: list[Foo] = []

listaNumeroPreenchida: list[int] = [2,4,6,8,10]

print(len(listaNumeroPreenchida))

listaNumeroPreenchida.append(2)
print(listaNumeroPreenchida)
listaNumeroPreenchida.pop()
print(listaNumeroPreenchida)

listaNumeroPreenchida.insert(0, 12)
print(listaNumeroPreenchida)
listaNumeroPreenchida.pop(0)
print(listaNumeroPreenchida)

listaNumeroPreenchida.insert(3, 45)
print(listaNumeroPreenchida)
listaNumeroPreenchida.pop(3)
print(listaNumeroPreenchida)

print('-'.join(str(listaNumeroPreenchida)))

n = 20
listaSequencia = [i for i in range(0, n)]

print(listaSequencia)

listaAleatoria = [random.randint(0, 100000) for i in range(0, 10)]

print(listaAleatoria)

print(listaSequencia[2])

for i in range(len(listaSequencia)):
    print(listaSequencia[i])

for i in listaSequencia:
    print(i)

x = 3
for i in listaSequencia:
    if i == x:
        print('valor encontrado laço')

if x in listaSequencia:
    print('valor encontrado')

print(listaSequencia.index(8))

listaParesFiltrada = [i for i in listaSequencia if i % 2 == 0]

print(listaParesFiltrada)

listaTransformada = [(i ** 2) for i in listaSequencia]

print(listaTransformada)

x = 6
for i in listaSequencia:
    if x == i:
        indice = listaSequencia.index(x)
        listaSequencia.pop(indice)

x = 1
listaRepetida = [1,4,2,5,1,7,8,3,1]

novaListaRepetida = [i for i in listaRepetida if i != x]

print(novaListaRepetida)

print(listaObjeto)

listaObjeto.append(Foo(322))
listaObjeto.append(Foo(656))
listaObjeto.append(Foo(878))

print(listaObjeto)

listaObjeto.pop(1)

print(listaObjeto)

listaObjeto.insert(0, Foo(111))
listaObjeto.pop()

print(listaObjeto)

x = Foo(322)

for i, o in enumerate(listaObjeto):
    if x.x == o.x:
        print(f'valor {x} encontrado na posicao {i}')

listaObjeto = [i for i in listaObjeto if i.x > 300]

print(listaObjeto)

for i in range(10):
    listaObjeto.append(Foo(random.randint(0, 200)))

print(listaObjeto)