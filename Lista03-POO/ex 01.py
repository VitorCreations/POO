class Retangulo:
    def __init__(self,b,h):
        self.__b = 0
        self.__h = 0
        self.set_base(b)
        self.set_altura(h)
    
    def set_base(self,x):
        if x >= 0: self.__b = x
        else:
            raise ValueError()
    def set_altura(self,x):
        if x >= 0: self.__h = x
        else:
            raise ValueError()
    
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h
    
    def calc_area(self):
        return self.__b * self.__h
    def calc_diagonal(self):
        return (self.__b ** 2 + self.__h ** 2) ** (1/2)
    
    def __str__(self):
        return f"Base = {self.__b} - Altura = {self.__h}"