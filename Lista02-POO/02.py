class Viagem:
    def __init__(self):
        self.__d = 0
        self.__t = 0
    
    def set_distancia(self, valor):
        if valor >= 0: self.__d = valor
        else: raise ValueError()
    def get_distancia(self):
        return self.__d
    
    def set_tempo(self, valor):
        if valor >= 0: self.__t = valor
        else: raise ValueError()
    def get_tempo(self):
        return self.__t
    
    def velocidade_media(self):
        return self.__d / self.__t
    
class UI:
    def main():
        x = Viagem()
        x.set_distancia(float(input("Informe a distância percorrida em km: ")))
        x.set_tempo(float(input("Ingorme o tempo gasto no percurso em horas: ")))
        print(f"A velocidade média atingida foi: {x.velocidade_media()}km/h")

UI.main()
    
