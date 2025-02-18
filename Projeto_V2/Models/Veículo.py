# Lista de Veiculos
# C - Create - Insere um objeto na lista
# R - Read   - Listar os objetos da lista
# U - Update - Atualizar um objeto na lista
# D - Delete - Exclui um objeto da lista

import json
from Models.crud import CRUD

# Modelo
class Veiculo:
  def __init__(self, id, nome, id_fabricante):
    self.id = id
    self.nome = nome
    self.id_fabricante = id_fabricante
  def __str__(self):
    return f"{self.nome} - {self.id_fabricante}"

# Persistência
class Veiculos(CRUD):
  @classmethod
  def salvar(cls):
    with open("veiculos.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("veiculos.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Veiculo(obj["id"], obj["nome"], obj["id_fabricante"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass

#veiculo = Veiculo(id=12, nome="HB20", id_fabricante="1")
#
#Veiculos.inserir(veiculo)
#
#Veiculos = Veiculos.listar()
#
#print("Veiculos:")
#for veiculo in Veiculos:
#    print(veiculo)