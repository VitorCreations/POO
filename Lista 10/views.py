from models.cliente import Cliente, Clientes
from models.horario import Horario, Horarios
from models.servico import Servico, Servicos
from datetime import datetime, timedelta

class View:
    def cliente_admin():
        for c in View.cliente_listar():
            if c.email == "admin": return
        View.cliente_inserir("admin", "admin", "1234", "1234")

    def cliente_inserir(nome, email, fone, senha):
        for cliente in View.cliente_listar():
            if cliente.email == email:
                raise ValueError("O e-mail já está em uso.")
        c = Cliente(0, nome, email, fone, senha)
        Clientes.inserir(c)

    def cliente_listar():
        return Clientes.listar()    

    def cliente_listar_id(id):
        return Clientes.listar_id(id)    

    def cliente_atualizar(id, nome, email, fone, senha):
        for cliente in View.cliente_listar():
            if cliente.email == email and cliente.id != id:
                raise ValueError("O e-mail já está em uso por outro cliente.")
        c = Cliente(id, nome, email, fone, senha)
        Clientes.atualizar(c)

    def cliente_excluir(id):
        for horario in View.horario_listar():
            if horario.id_cliente == id:
                raise ValueError("Não é possível excluir o cliente porque ele possui horários agendados.")
        c = Cliente(id, "", "", "", "")
        Clientes.excluir(c)

    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.email == email and c.senha == senha:
                return {"id" : c.id, "nome" : c.nome }
        return None

    def horario_inserir(data, confirmado, id_cliente, id_servico):
        if id_cliente and not View.cliente_listar_id(id_cliente):
            raise ValueError("ID do cliente inválido.")
        if id_servico and not View.servico_listar_id(id_servico):
            raise ValueError("ID do serviço inválido.")
        c = Horario(0, data)
        c.confirmado = confirmado
        c.id_cliente = id_cliente
        c.id_servico = id_servico
        Horarios.inserir(c)

    def horario_listar():
        return Horarios.listar()    

    def horario_listar_disponiveis():
        horarios = View.horario_listar()
        disponiveis = []
        for h in horarios:
            if h.data >= datetime.now() and h.id_cliente == None: disponiveis.append(h)
        return disponiveis   

    def horario_atualizar(id, data, confirmado, id_cliente, id_servico):
        if id_cliente and not View.cliente_listar_id(id_cliente):
            raise ValueError("ID do cliente inválido.")
        if id_servico and not View.servico_listar_id(id_servico):
            raise ValueError("ID do serviço inválido.")
        c = Horario(id, data)
        c.confirmado = confirmado
        c.id_cliente = id_cliente
        c.id_servico = id_servico
        Horarios.atualizar(c)

    def horario_excluir(id):
        horario = Horarios.listar_id(id)
        if horario and horario.id_cliente:
            raise ValueError("Não é possível excluir um horário que está agendado para um cliente.")
        Horarios.excluir(horario)

    def horario_abrir_agenda(data, hora_inicio, hora_fim, intervalo):
        dt = datetime.strptime(data, "%d/%m/%Y")
        if dt.date() < datetime.now().date():
            raise ValueError("Data não pode estar no passado.")
        if intervalo <= 0 or intervalo > 120:
            raise ValueError("Intervalo deve estar entre 1 e 120 minutos.")
        hora_inicio_dt = datetime.strptime(f"{data} {hora_inicio}", "%d/%m/%Y %H:%M")
        hora_fim_dt = datetime.strptime(f"{data} {hora_fim}", "%d/%m/%Y %H:%M")
        if hora_fim_dt <= hora_inicio_dt:
            raise ValueError("Hora final deve ser maior que a hora inicial.")
        i = data + " " + hora_inicio
        f = data + " " + hora_fim
        d = timedelta(minutes=intervalo)
        di = datetime.strptime(i, "%d/%m/%Y %H:%M")
        df = datetime.strptime(f, "%d/%m/%Y %H:%M")
        x = di
        while x <= df:
            View.horario_inserir(x, False, None, None)
            x = x + d

    def servico_inserir(descricao, valor, duracao):
        c = Servico(0, descricao, valor, duracao)
        Servicos.inserir(c)

    def servico_listar():
        return Servicos.listar()    

    def servico_listar_id(id):
        return Servicos.listar_id(id)    

    def servico_atualizar(id, descricao, valor, duracao):
        c = Servico(id, descricao, valor, duracao)
        Servicos.atualizar(c)

    def servico_excluir(id):
        for horario in View.horario_listar():
            if horario.id_servico == id:
                raise ValueError("Não é possível excluir o serviço porque ele está vinculado a horários agendados.")
        c = Servico(id, "", 0, 0)
        Servicos.excluir(c)
