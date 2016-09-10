from collections import UserDict


def f(p:g):
    print('Executando f')
    g()


print(dir())


# g() da pau pq nao esta definido

def g():
    print('Executando g')


print(dir())

f()


class A(UserDict):
    def update(*args, **kwds):
        return super().update(**kwds)