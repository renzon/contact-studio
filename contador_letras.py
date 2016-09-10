histograma = {}

letras = 'abcajhgadsligads'

for char in letras:
    histograma[char] = histograma.get(char, 0) + 1

print(histograma)
