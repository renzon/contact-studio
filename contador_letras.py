histograma = {}

letras = 'abcajhgadsligads'

for char in letras:
    if char in histograma:
        histograma[char] += 1
    else:
        histograma[char] = 1

print(histograma)
