class Horario:
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self._confirmado = False
        self._id_cliente = 0
        self._id_servico = 0
    
    def __str__(self):
        return f"{self.id} - {self.data}"

    # Métodos de acesso (getters)
    def get_confirmado(self):
        return self._confirmado
    
    def get_id_cliente(self):
        return self._id_cliente
    
    def get_id_servico(self):
        return self._id_servico

    # Métodos de modificação (setters)
    def set_confirmado(self, confirmado):
        if not isinstance(confirmado, bool):
            raise ValueError("O status de confirmação deve ser um valor booleano.")
        self._confirmado = confirmado
    
    def set_id_cliente(self, id_cliente):
        if id_cliente < 0:
            raise ValueError("O ID do cliente não pode ser negativo.")
        self._id_cliente = id_cliente
    
    def set_id_servico(self, id_servico):
        if id_servico < 0:
            raise ValueError("O ID do serviço não pode ser negativo.")
        self._id_servico = id_servico
