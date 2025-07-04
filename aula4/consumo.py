#pip install requests

import requests

if __name__ == "__main__":
    url = "http://127.0.0.1:8000"
    r = requests.get(f"{url}/livros")
    print(r.text)
    livro = {
        "titulo": "Python como Programar",
        "ano": 2024,
        "edicao": 1
    }
    r = requests.post(f"{url}/livros",json=livro)
    print(r.status_code)
    print(r.text)
    pesquisa = "Python como Programar"
    r = requests.get(f"{url}/livros/{pesquisa}")
    print(r.status_code)
    print(r.text)
    r = requests.delete(f"{url}/livros/{pesquisa}")
    print(r.status_code)
    


from main import *
from models import Livro
def menu():
    print("""
Menu -> 
1 - Listar todos os livros
2 -  Pesquisa livro por título
3 - Cadastrar um livro
4 - Deletar um livro
5 - Editar um livro
6 - Sair
""")
    return int(input('Digite sua opção: '))

opcao = menu()

while opcao !=6:
    if opcao==1:
        livros = listar_livros()
        print(livros)
    elif opcao==2:
        titulo = input('Digite o título  : ')
        print(listar_livro(titulo))
    elif opcao == 3:
        titulo = input('Digite seu titulo: ')
        ano = int(input('Digite o ano do sue livro : '))
        edicao = int(input('Digite a edição do seu livro: '))
        livro = {
            'titulo' : titulo,
            'ano' : ano,
            'edicao' : edicao
        }
        dict_livro = Livro(**livro)
        criar_livro(dict_livro)
    elif opcao == 4:
        titulo = input('Digite seu titulo: ')
        deletar_livro(titulo)
    elif opcao == 5:
        titulo = input('Digite o titulo de quem deseja editar: ')
        nov_titulo = input('Digite seu novo titulo: ')
        ano = int(input('Digite o novo ano do sue livro : '))
        edicao = int(input('Digite a nova edição do seu livro: '))
        livro = {
            'titulo' : nov_titulo,
            'ano' : ano,
            'edicao' : edicao
        }
        dict_livro = Livro(**livro)
        editar_livro(titulo,dict_livro)

   


    opcao = menu()


