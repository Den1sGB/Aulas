class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def exibir(self):
        print(f"Nome do Cliente: {self.nome}.\n Sobrenome do Cliente: {self.sobrenome}.\nCPF do Cliente: {self.cpf}.")
