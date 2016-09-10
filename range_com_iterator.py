class Range:
    def __init__(self, inicio, fim=None, passo=1):
        self.passo = passo
        self.fim = fim
        self.inicio = inicio

    def __iter__(self):
        return RangeIterator(self.inicio, self.fim, self.passo)


class RangeIterator:
    def __init__(self, inicio, fim=None, passo=1):
        self.passo = passo
        if fim is None:
            fim = inicio
            inicio = 0
        self.fim = fim
        self.inicio = inicio
        self.atual = inicio

    def __next__(self):
        if self.atual >= self.fim:
            raise StopIteration()
        valor = self.atual
        self.atual += self.passo
        return valor


if __name__ == '__main__':
    r = Range(10)

    for i in r:
        print(i)
