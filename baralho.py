from collections import namedtuple
from itertools import product, chain
from random import shuffle

Carta = namedtuple('Carta', 'naipe numero')


class Baralho:
    def __init__(self):
        self.cartas = [
            Carta(naipe, numero)
            for naipe, numero in product(
                'paus copas ouros espadas'.split(),
                chain(range(2, 11), 'QJKA')
            )
            ]

    def __str__(self):
        return str(self.cartas)

    def __getitem__(self, idx):
        return self.cartas[idx]

    def __len__(self):
        return len(self.cartas)

    def __setitem__(self, idx, value):
        self.cartas[idx] = value


baralho = Baralho()

print(baralho[0])
print(baralho[:5])
for i, carta in zip(range(1, len(baralho) * 10 + 1, 10), baralho):
    print(i, carta)

shuffle(baralho)
print(baralho)

all()




# Solucao com for
# [
# Carta(naipe, numero)
# for naipe in 'paus copas ouros espadas'.split()
# for numero in chain(range(2, 11), 'QJKA')
# ]
