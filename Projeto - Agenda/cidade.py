import json

class Cidade:
  def __init__(self, id, cn, uf):
    self.id = id
    self.cn = cn
    self.uf = uf
  def get_cn(self):
    return self.__cn
  def set_cn(self, cn):
    if cn != "": self.cn = cn
    else: raise ValueError("Cidade inválida")  
  def __str__(self):
    return f"{self.id} - {self.cn} - {self.uf}"

class Cidades:
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
      c.cn = obj.cn
      c.email = obj.email
      c.fone = obj.fone
    cls.salvar()   
  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None: 
      cls.objetos.remove(c)
      cls.salvar()   
  @classmethod
  def salvar(cls):
    with open(" s.json", mode = "w") as arquivo:   
      json.dump(cls.objetos, arquivo, default = vars)
  @classmethod
  def abrir(cls):
    cls.objetos = []
    try: 
      with open("cidades.json", mode = "r") as arquivo:
        texto = json.load(arquivo)
        for obj in texto:
          c = Cidade(obj["id"], obj["cn"], obj["email"], obj["fone"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass
    
