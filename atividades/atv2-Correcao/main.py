from aula2.models import Leitor, Livro, Emprestimo
from fastapi import FastAPI, HTTPException
from typing import List
from datetime import date
import uuid

app = FastAPI()

livros: List[Livro] = []
leitores: List[Leitor] = []
emprestimos: List[Emprestimo] = []

@app.post('/livro', response_model=Livro)
def cadastra_livro(livro_cadastra: Livro):
    livro_cadastra.uuid = str(uuid.uuid4())
    livros.append(livro_cadastra)
    return livro_cadastra

@app.get('/livros', response_model=List[Livro])
def lista_livros():
    return livros

@app.get('/livros/{titulo}', response_model=List[Livro])
def lista_livros_por_titulo(titulo: str):
    encontrados = [livro for livro in livros if livro.titulo == titulo]
    if not encontrados:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return encontrados

@app.post('/leitores', response_model=Leitor)
def cadastrar_leitor(leitor: Leitor):
    leitor.uuid = str(uuid.uuid4())
    leitores.append(leitor)
    return leitor

@app.get('/emprestimo', response_model=Emprestimo)
def emprestimo(leitor: str, livro: str, data_emprestimo: date, data_devolucao: date):
    user = next((u for u in leitores if u.uuid == leitor), None)
    book = next((l for l in livros if l.uuid == livro and l.disponivel), None)

    if user and book:
        book.disponivel = False
        dados = {
            "leitor": user,
            "livro": book,
            "data_emp": data_emprestimo,
            "data_dev": data_devolucao
        }
        emprestimo_obj = Emprestimo(**dados)
        emprestimos.append(emprestimo_obj)
        return emprestimo_obj

    raise HTTPException(status_code=404, detail="Empréstimo não realizado")
