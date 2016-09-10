tpl = (2, 3)
print(type(tpl))
for e in tpl:
    print(e)


def f(p, *parametros):
    print(p)
    print(type(parametros))
    print(parametros)
    return p, parametros


f(1)
f(2)
f(2, 4)
f(2, 4, 5)

lista = [4, 5, 6]
f(lista)
f(*lista)
print(f(2, 3))
primeiro, segundo = f(2, 4)
print(primeiro, segundo)

primeiro, *resto = lista

print(primeiro, resto)
print(lista)


def g(**kwargs):
    return kwargs


# print(g(a=7, g=8))

dct = {'a': 7, 'g': 8}

print(g(**dct))


def j(a, b, *args, k=8, **kwargs):
    print(a, b, k, args, kwargs)


j(1, 2, 3, 6, m=12)
