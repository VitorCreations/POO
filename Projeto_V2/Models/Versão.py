# Lista de Versões
# C - Create - Insere um objeto na lista
# R - Read   - Listar os objetos da lista
# U - Update - Atualizar um objeto na lista
# D - Delete - Exclui um objeto da lista

import json
from Models.crud import CRUD

# Modelo
class Versão:
  def __init__(self, id, id_veiculo, nome, ano, preco, ipva, seguro, garantia, porte, lugares):
    self.id = id
    self.id_veiculo = id_veiculo
    self.nome = nome
    self.ano = ano
    self.preco = preco
    self.ipva = ipva
    self.seguro = seguro
    self.garantia = garantia
    self.porte = porte
    self.lugares = lugares
  def __str__(self):
    return f"Id do Veículo{self.id_veiculo} - Nome da Versão{self.nome} - Ano:{self.ano} - Preço:{self.preco} - IPVA:{self.ipva} - Seguro:{self.seguro} - Garantia:{self.garantia} - Porte:{self.porte} - Lugares:{self.lugares}"

# Persistência
class Versões(CRUD):
  @classmethod
  def salvar(cls):
    with open("versões.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("versões.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Versão(obj["id"], obj["id_veiculo"], obj["nome"], obj["ano"], obj["preço"], obj["IPVA"], obj["seguro"], obj["garantia"], obj["porte"], obj["lugares"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass

#versão = Versão(id=1, nome="HB20-TSI", id_veiculo="25", descricão="carro massa")
#
#Versões.inserir(versão)
#
#Versões = Versões.listar()#
#
#print("Versões:")
#for versão in Versões:
#    print(versão)