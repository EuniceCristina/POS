
from fastapi import FastAPI, HTTPException
from models import Livros, Leitor, Emprestimos, Devolucao 
from typing import List
from secrets import token_hex

app = FastAPI()


livros_db: List[Livros] = []
leitores_db: List[Leitor] = []
emprestimos_db: List[Emprestimos] = []
devolucoes_db: List[Devolucao] = []

@app.get("/livros/", response_model=List[Livros])
def listar_livros():
    return livros_db

@app.get("/livros/{id}", response_model=Livros)
def listar_livros_id(id: int):
    for livro in livros_db:
        if livro.id == id:
            return livro
    raise HTTPException(status_code=404, detail="Livro não encontrado")

@app.post("/livros/", response_model=Livros)
def criar_livro(livro: Livros): 
    livro.id = int(token_hex(4), 16)  
    livros_db.append(livro) 
    return livro

@app.post("/leitor/", response_model=Leitor)
def criar_leitor(leitor: Leitor):
    leitor.id = int(token_hex(4), 16)  
    leitores_db.append(leitor)
    return leitor

@app.post("/emprestimos/", response_model=Emprestimos)
def criar_emprestimo(emprestimo: Emprestimos):
    emprestimos_db.append(emprestimo)
    return emprestimo

@app.post("/devolucao/", response_model=Devolucao) 
def criar_devolucao(devolucao: Devolucao):
    devolucoes_db.append(devolucao)
    return devolucao

@app.get("/livros_emprestados", response_model=List[Livros])
def listar_livros_emprestados():
    emprestados = [livro for livro in livros_db if livro.estado_disponibilidade.lower() == "emprestado"]
    if not emprestados:
        raise HTTPException(status_code=404, detail="Nenhum livro emprestado encontrado")
    return emprestados