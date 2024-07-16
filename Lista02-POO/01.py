class Circulo:
    def __init__(self):
        self.__r = 0
    
    def set_raio(self, valor):
        if valor >= 0: self.__r = valor
        else: raise ValueError()
    def get_raio(self):
        return self.__r
    

    def calc_area(self):
        return (self.__r ** 2) * 3.14
    def calc_circunferencia(self):
        return self.__r * 2 * 3.14


class UI:
    @staticmethod
    def main():
        x = Circulo()
        x.set_raio(float(input("informe o valor do raio: ")))
        print(f"A área do Círculo é: {x.calc_area()}")
        print(f"A Circunferência do Círculo é: {x.calc_circunferencia()}")

UI.main()