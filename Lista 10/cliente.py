class Cliente:
    def __init__(self, id, nome, email, fone, senha):
        self.id = id
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)
    
    def __str__(self):
        return f"{self.nome} - {self.email} - {self.fone}"

    # Métodos de acesso (getters)
    def get_nome(self):
        return self._nome
    
    def get_email(self):
        return self._email
    
    def get_fone(self):
        return self._fone
    
    def get_senha(self):
        return self._senha

    # Métodos de modificação (setters)
    def set_nome(self, nome):
        if not nome:
            raise ValueError("O nome não pode ser vazio.")
        self._nome = nome
    
    def set_email(self, email):
        if not email:
            raise ValueError("O e-mail não pode ser vazio.")
        self._email = email
    
    def set_fone(self, fone):
        if not fone:
            raise ValueError("O telefone não pode ser vazio.")
        self._fone = fone
    
    def set_senha(self, senha):
        if not senha:
            raise ValueError("A senha não pode ser vazia.")
        self._senha = senha
