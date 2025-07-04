import requests

URL = 'http://127.0.0.1:8000'

def listar_livros():
   r = requests.get(f"{URL}/livros")
   if r.status_code == 200:
       print(r.text)

def cadastrar_livros():
    titulo = input("Digite o titulo: ")
    ano = int(input("Digite o ano: "))
    edicao = int(input("Digite a edicao : "))
    livro = {
        "titulo" : titulo,
        "ano" : ano,
        "edicao" : edicao
    }
    r = requests.post(f"{URL}/livros",json=livro)

def listar_livro(titulo):
    r = requests.get(f"{URL}/livros/{titulo}")
    if r.status_code == 200:
       print(r.text)
    if r.status_code == 404:
       print(r.text)

def excluir_livro(titulo):
    r = requests.delete(f"{URL}/livros/{titulo}")
    if r.status_code == 200:
       print("Concluido com sucesso")
    else:
        print(r.text)


def menu():
    print("1 = Listar livros")
    print("2 = Listar livros pelo título")
    print("3 = Cadastrar livros")
    print("4 = Deletar livros")
    print("5 = Sair")
    return int(input("Digite sua opção: "))

opcao = menu()
while opcao !=5:
    if opcao == 1:
        listar_livros()
    elif opcao ==2 :
        Titulo = input("Digite seu titulo: ")
        listar_livros(Titulo)
    elif opcao==3:
        cadastrar_livros()
    elif opcao == 4:
        titulo = input("DIgite seu livro: ")
        excluir_livro(titulo)
    opcao=menu()
