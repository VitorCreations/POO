from banda import Banda, Bandas
from apresentação import Apresentação, Apresentações
from datetime import datetime


class UI:
  @staticmethod
  def menu():
    print("Cadastro de Bandas")
    print("  1 - Inserir, 2 - listar, 3 - atualizar, 4 - excluir")
    print("Cadastro de Cidades")
    print("  5 - Inserir, 6 - listar, 7 - atualizar, 8 - excluir")
    print("Cadastro de Apresentações")
    print("  1 - Inserir, 2 - listar, 3 - atualizar, 4 - excluir")
    print("Outras opções")
    print("  9 - Fim")
    return int(input("Informe uma opção: "))

  @staticmethod
  def main():
    op = 0
    while op != 13: 
      op = UI.menu()
      if op == 1: UI.banda_inserir()
      if op == 2: UI.banda_listar()
      if op == 3: UI.banda_atualizar()
      if op == 4: UI.banda_excluir()
      if op == 5: UI.apresentação_inserir()
      if op == 6: UI.apresentação_listar()
      if op == 7: UI.apresentação_atualizar()
      if op == 8: UI.apresentação_excluir()
      if op == 9: UI.apresentação_inserir()
      if op == 10: UI.apresentação_listar()
      if op == 11: UI.apresentação_atualizar()
      if op == 12: UI.apresentação_excluir()

  @staticmethod
  def banda_inserir():
    nome = input("Informe o nome: ")
    insta = input("Informe o instagram da banda: ")
    fone = input("Informe o fone: ")
    b = Banda(0, nome, insta, fone)
    Bandas.inserir(b)

  @staticmethod
  def apresentação_inserir():
    datastr = input("Informe a data e o horário no formato dd/mm/aaaa hh:mm: ")
    data = datetime.strptime(datastr, "%d/%m/%Y %H:%M")
    endereço = input("Informe o endereço da apresentação")
    a = Apresentação(0, data, endereço)
    Apresentações.inserir(a)

  @staticmethod
  def banda_listar():
    for b in Bandas.listar():
      print(b)

  @staticmethod
  def apresentação_listar():
    for a in Apresentações.listar():
      print(a)

  @staticmethod
  def banda_atualizar():
    UI.banda_listar()
    id = int(input("Informe o id da banda a ser atualizado: "))
    nome = input("Informe o novo nome: ")
    insta = input("Informe o novo instagram: ")
    fone = input("Informe o novo fone: ")
    b = Banda(id, nome, insta, fone)
    Bandas.atualizar(b)

  @staticmethod
  def apresentação_atualizar():
    UI.apresentação_listar()
    datastr = input("Informe a nova data e o horário no formato dd/mm/aaaa hh:mm: ")
    data = datetime.strptime(datastr, "%d/%m/%Y %H:%M")
    endereço = input("Informe o novo endereço da apresentação")
    a = Apresentação(0, data, endereço)
    Apresentações.atualizar(a)

  @staticmethod
  def banda_excluir():
    UI.banda_listar()
    id = int(input("Informe o id do banda a ser excluído: "))
    b = Banda(id, "", "", "")
    Bandas.excluir(b)

  @staticmethod
  def apresentação_excluir():
    UI.apresentação_listar()
    id = int(input("Informe o id da apresentação a ser excluida: "))
    a = Apresentação(id, "", "")
    Apresentações.excluir(a)
  
UI.main()    





  
