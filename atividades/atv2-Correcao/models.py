from pydantic import BaseModel
from datetime import date
from typing import List, Optional

class Livro(BaseModel):
    uuid: Optional[str] = None
    titulo: str
    ano: str
    disponivel: bool = True  # Valor padrão

class Leitor(BaseModel):
    uuid: Optional[str] = None
    nome: str
    livros: List[Livro] = []  # Lista vazia por padrão

class Emprestimo(BaseModel):
    data_emp: date
    data_dev: date
    livro: Livro
    leitor: Leitor