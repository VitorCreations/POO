class Frete:
    def __init__(self,d,p):
        self.__d = 0
        self.__p = 0
        self.set_distancia(d)
        self.set_peso(p)
    
    def set_distancia(self,x):
        if x >= 0: self.__d = x
        else:
            raise ValueError()
    def set_peso(self,x):
        if x >= 0: self.__p = x
        else:
            raise ValueError()
    
    def get_distancia(self):
        return self.__d
    def get_peso(self):
        return self.__p
    
    def calc_frete(self):
        return self.__d * self.__p
    
    def __str__(self):
        return f"distancia = {self.__d} - peso = {self.__p}"