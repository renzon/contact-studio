class Vetor:
    def __init__(this, x=0, y=0):
        this.y = y
        this.x = x

    def __repr__(self):
        return 'Vetor({}, {})'.format(self.x, self.y)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def somar(self, vetor):
        return Vetor(self.x + vetor.x, self.y + vetor.y)

    def __add__(self, other):
        return self.somar(other)

    @staticmethod
    def m():
        return 1


vetor = Vetor(1, 2)
vetor2 = Vetor(2, 2)
print(vetor + vetor2)
print(vetor.__repr__())
print(vetor)


perm
