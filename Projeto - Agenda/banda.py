import json

class Banda:
  def __init__(self, id, nome, insta, fone):
    self.id = id
    self.nome = nome
    self.insta = insta
    self.fone = fone
  def get_nome(self):
    return self.__nome
  def set_nome(self, nome):
    if nome != "": self.nome = nome
    else: raise ValueError("Nome inválido")  
  def __str__(self):
    return f"{self.id} - {self.nome} - {self.insta} - {self.fone}"

class Bandas:
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
      c.nome = obj.nome
      c.insta = obj.insta
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
    with open("bandas.json", mode = "w") as arquivo:   
      json.dump(cls.objetos, arquivo, default = vars)
  @classmethod
  def abrir(cls):
    cls.objetos = []
    try: 
      with open("bandas.json", mode = "r") as arquivo:
        texto = json.load(arquivo)
        for obj in texto:
          c = Banda(obj["id"], obj["nome"], obj["insta"], obj["fone"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass
    
