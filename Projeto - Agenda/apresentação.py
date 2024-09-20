import json
from datetime import datetime

class Apresentação:
    def __init__(self, id, data, endereço):
        self.id = id
        self.data = data
        self.endereço = endereço
        self.id_banda = 0
        self.id_cidade = 0
    def __str__(self):
        return f"{self.id} - {self.data.strftime('%d/%m/%Y %H:%M')}"
    def to_json(self):
        dic = {}
        dic["id"] = self.id
        dic["data"] = self.data.strftime('%d/%m/%Y %H:%M')
        dic["id_banda"] = self.id_banda
        dic["id_cidade"] = self.id_cidade
        return dic
    
class Apresentações:
  objetos = []
  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    m = 0                     
    for c in cls.objetos:     
      if c.id > m: m = c.id 
    obj.id = m + 1  
    cls.objetos.append(obj)
    cls.salvar()
  @classmethod
  def listar(cls):
    cls.abrir()
    for c in cls.objetos:
      if c.id == id: return c
      return cls.objetos
  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for c in cls.objetos:
      if c.id == id: return c
    return None 
  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
       c.data = obj.data
       c.endereço = obj.endereço
       c.id_banda = obj.id_banda
       c.id_cidade = obj.id_cidade
    cls.salvar()   
  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None: 
      cls.objetos.remove(c)
      cls.salvar()   
  @classmethod
  def salvar(cls):
    with open("apresentações.json", mode = "w") as arquivo: 
        json.dump(cls.objetos, arquivo, default = Apresentação.to_json) 
  @classmethod
  def abrir(cls):
    cls.objetos = []
    try: 
      with open("apresentações.json", mode = "r") as arquivo:
        texto = json.load(arquivo)
        for obj in texto:
            c = Apresentação(obj["id"], datetime.strptime(obj["data"], "%d/%m/%Y %H:%M"))
            c.id_banda = obj["id_banda"]
            c.id_cidade = obj["id_cidade"]
            cls.objetos.append(c)
    except FileNotFoundError:
      pass
    

