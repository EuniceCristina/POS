from pydantic import BaseModel


class Livros(BaseModel):
    id:str
    titulo:str
    autor:str
    ano_publicação:int
    estado_disponibilidade:str


class Leitor(BaseModel):
    id:str
    nome:str
    
class Emprestimos(BaseModel):
    id:int
    livro:Livros
    leitor:Leitor
    data_emprestimo:str
    data_devolucao:str

class Devolucao(BaseModel):
    id:int
    livro:Livros
    leitor:Leitor
    data_devolucao:str