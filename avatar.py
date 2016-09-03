import requests


def avatar(usuario):
    url = 'https://api.github.com/users/' + usuario
    r = requests.get(url)
    if r.status_code == 200:
        dct = r.json()
        return dct['avatar_url']

print(avatar('trfiladelfo'))
