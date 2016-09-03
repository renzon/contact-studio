import requests


def avatar(usuario):
    'funcao que retornar o avatar de um usuário do github'
    url = 'https://api.github.com/users/' + usuario
    r = requests.get(url)
    if r.status_code == 200:
        dct = r.json()
        return dct['avatar_url']


if __name__ == '__main__':
    print(avatar('trfiladelfo'))
