class Aluno:
    def __init__(self): #construtor
        self.matricula= ''
        self.nome= ''
    def ano_ingresso(self): #metodo
        return int(self.matricula[0:4])
a = Aluno()
a.nome = 'Vitinho'
a.matricula = '20221011110029'
b = Aluno()
b.nome = "João garanhão"
b.matricula = "20221011110042"

print(a.nome, a.matricula, a.ano_ingresso())
print(b.nome, b.matricula, b.ano_ingresso())