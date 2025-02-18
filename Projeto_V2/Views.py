from Models.Fabricante import Fabricante, Fabricantes
from Models.Usuario import Usuario, Usuarios
from Models.Profissional import Profissional, Profissionais
from Models.Versão import Versão, Versões
from Models.Veículo import Veiculo, Veiculos

class View:
    def usuario_admin():
        for c in View.usuario_listar():
            if c.email == "admin": return
        View.usuario_inserir("admin", "admin", "1234", "1234", 1)

    def usuario_inserir(nome, email, senha):
        c = Usuario(0, nome, email, senha)
        Usuarios.inserir(c)

    def usuario_listar():
        return Usuarios.listar()    

    def usuario_listar_id(id):
        return Usuarios.listar_id(id)    

    def usuario_atualizar(id, nome, email, senha):
        c = Usuario(id, nome, email, senha)
        Usuarios.atualizar(c)

    def usuario_excluir(id):
        c = Usuario(id, "", "", "")
        Usuarios.excluir(c)









    def usuario_autenticar(email, senha):
        for c in View.usuario_listar():
            if c.email == email and c.senha == senha:
                return {"id" : c.id, "nome" : c.nome }
        return None

    def profissional_autenticar(email, senha):
        for c in View.profissional_listar():
            if c.email == email and c.senha == senha:
                return {"id" : c.id, "nome" : c.nome }
        return None









    def profissional_inserir(nome, email, senha):
        c = Profissional(0, nome, email, senha)
        Profissionais.inserir(c)

    def profissional_listar():
        return Profissionais.listar()    

    def profissional_listar_id(id):
        return Profissionais.listar_id(id)    

    def profissional_atualizar(id, nome, email, senha):
        c = Profissional(id, nome, email, senha)
        Profissionais.atualizar(c)

    def profissional_excluir(id):
        c = Profissional(id, "", "", "")
        Profissionais.excluir(c) 









    def versao_inserir(id_veiculo, nome, ano, preco, ipva, seguro, garantia, porte, lugares):
        c = Versão(0, nome, ano, preco, ipva, seguro, garantia, porte, lugares)
        c.id_veiculo = id_veiculo
        Versões.inserir(c)

    def versao_listar():
        return Versões.listar()    

    def versao_pesquisar(id_veiculo):
        r = []
        versoes = Veiculos.listar()
        for v in versoes:
            if v.id_veiculo == id_veiculo: r.append(v)
        return r       
  
    def versao_atualizar(id_veiculo, nome, ano, preco, ipva, seguro, garantia, porte, lugares):
        c = Versão(0, nome, ano, preco, ipva, seguro, garantia, porte, lugares)
        c.id_veiculo = id_veiculo
        Versões.atualizar(c)

    def versao_excluir(id):
        c = Versão(id, None)
        Versão.excluir(c)    

    






    def veiculo_inserir(nome, id_fabricante):
        c = Veiculo(0, nome, id_fabricante)
        Veiculos.inserir(c)

    def veiculo_listar():
        return Veiculos.listar()    

    def veiculo_listar_id(id):
        return Veiculos.listar_id(id)    

    def veiculo_atualizar(id, nome, id_fabricante):
        c = Veiculo(id, nome, id_fabricante)
        Veiculos.atualizar(c)

    def veiculo_excluir(id):
        c = Veiculo(id, "", 0)
        Veiculos.excluir(c)    





    def fabricante_inserir(nome, email, fone):
        c = Fabricante(0, nome, email, fone)
        Fabricantes.inserir(c)

    def fabricante_listar():
        return Fabricantes.listar()    

    def fabricante_listar_id(id):
        return Fabricantes.listar_id(id)    

    def fabricante_atualizar(id, nome, email, fone):
        c = Fabricante(id, nome, email, fone)
        Fabricantes.atualizar(c)

    def fabricante_excluir(id):
        c = Fabricante(id, "", "", "")
        Fabricantes.excluir(c)    