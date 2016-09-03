import requests
import xmltodict


def listar():
    '''Lista os cds presentes em
    http://www.w3schools.com/xml/cd_catalog.xml
    '''
    r = requests.get('http://www.w3schools.com/xml/cd_catalog.xml')
    if r.status_code != 200:
        raise Exception('Nao funfou')
    dct = xmltodict.parse(r.content)
    catalogo = dct['CATALOG']
    cds = catalogo.get('CD', [])
    for cd in cds:
        print(cd['TITLE'], cd['PRICE'])


if __name__ == '__main__':
    listar()
