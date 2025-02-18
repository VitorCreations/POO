# Lista de fabricantes
# C - Create - Insere um objeto na lista
# R - Read   - Listar os objetos da lista
# U - Update - Atualizar um objeto na lista
# D - Delete - Exclui um objeto da lista

import json
from crud import CRUD

# Modelo
class Fabricante:
  def __init__(self, id, nome, email, fone):
    self.id = id
    self.nome = nome
    self.email = email
    self.fone = fone
  def __str__(self):
    return f"{self.nome} - {self.email} - {self.fone}"

# Persistência
class Fabricantes(CRUD):
  @classmethod
  def salvar(cls):
    with open("fabricantes.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("fabricantes.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Fabricante(obj["id"], obj["nome"], obj["email"], obj["fone"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass

#a = Fabricante(id=2, nome="Fabricante AS", email="Fabricante_AS@gmail.com", fone="(84)9 XXXX-0021")
#
#Fabricantes.excluir(a)
#
#fabricantes = Fabricantes.listar()
#
#print("Fabricantes:")
#for a in fabricantes:
#    print(a)