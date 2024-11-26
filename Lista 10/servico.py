class Servico:
    def __init__(self, id, descricao, valor, duracao):
        self.id = id
        self.set_descricao(descricao)
        self.set_valor(valor)
        self.set_duracao(duracao)
    
    def __str__(self):
        return f"{self.id} - {self.descricao} - R$ {self.valor:.2f} - {self.duracao} min"
    
    # Métodos de acesso (getters)
    def get_descricao(self):
        return self._descricao
    
    def get_valor(self):
        return self._valor
    
    def get_duracao(self):
        return self._duracao

    # Métodos de modificação (setters)
    def set_descricao(self, descricao):
        if not descricao:
            raise ValueError("A descrição não pode ser vazia.")
        self._descricao = descricao
    
    def set_valor(self, valor):
        if valor < 0:
            raise ValueError("O valor não pode ser negativo.")
        self._valor = valor
    
    def set_duracao(self, duracao):
        if duracao < 0:
            raise ValueError("A duração não pode ser negativa.")
        self._duracao = duracao
