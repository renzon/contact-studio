from collections import defaultdict


def zero_factory():
    return 0


histograma = defaultdict(zero_factory)

letras = 'abcajhgadsligads'

for char in letras:
    histograma[char] += 1

print(histograma)
