from collections import ChainMap

dct_perfeito = {'arquivo': 'nome.txt', 'aux': 'xyx'}
dct_defeituoso = {'aux': 'xyx', 'foo': 'bar'}


def parse(dct):
    padrao = {'arquivo': 'default.txt', 'aux': 'default.aux', 'foo': 'default.foo'}
    return ChainMap(dct, padrao)


print(parse(dct_perfeito)['foo'])
print(parse(dct_defeituoso))


