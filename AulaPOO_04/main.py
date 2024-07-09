class Triangulo:                                #entidade
    def __init__(self):                         #construtor
        self.__b = 0                            #atributos encapsulados
        self.__h = 0

    def set_base(self, valor):
        if valor >= 0: self.__b = valor
        else: raise ValueError()
    def get_base(self):
        return self.__b
    
    def set_altura(self, valor):                #armazenar um valor, 
        if valor >= 0: self.__h = valor
        else: raise ValueError()
    def get_altura(self):                       #recupera o valor
        return self.__h

    
    def calc_area(self):                        #métodos = operação - método de instância
        return self.__b * self.__h / 2

class UI:                                       #Interface com o usuário
    @staticmethod                               #prints e inputs nessa classe
    def main():                                 #operação principal da UI - método de classe
        x = Triangulo()
        #x.b = float(input("Informe o Valor da base: "))
        #x.h = float(input("Informe o Valor da altura: "))
        x.set_base(float(input("Informe o Valor da base: ")))
        x.set_altura(float(input("Informe o Valor da altura: ")))
        print(f"A área do triangulo é {x.calc_area()}")

UI.main()                                         #rodar o programa