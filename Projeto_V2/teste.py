from Models.Fabricante import Fabricante, Fabricantes

a = Fabricante(id=1, nome="Fabricante A", email="Fabricante_A@gmail.com", fone="(84)9 9624-0021")
Fabricantes.inserir(a)

for c in Fabricantes.listar():
    print(c)