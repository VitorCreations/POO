# Lista de Usuarios
# C - Create - Insere um objeto na lista
# R - Read   - Listar os objetos da lista
# U - Update - Atualizar um objeto na lista
# D - Delete - Exclui um objeto da lista

import json
from Models.crud import CRUD

# Modelo
class  Profissional:
  def __init__(self, id, nome, email, senha):
    self.id = id
    self.nome = nome
    self.email = email
    self.senha = senha
  def __str__(self):
    return f"{self.nome} - {self.email}"

# Persistência
class Profissionais(CRUD):
  @classmethod
  def salvar(cls):
    with open("profissionais.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("profissionais.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Profissional(obj["id"], obj["nome"], obj["email"], obj["senha"],)
          cls.objetos.append(c)
    except FileNotFoundError:
      pass
