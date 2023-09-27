clientes = []
class Banco:
    def __init__(self):
        self.clientes = {}
    
    def getClientes (self):
        return self.clientes
    
    def cadastrarCliente (self, nome, cpf, email, idade, senha, senhaMovimentacoes):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.idade = idade
        self.senha = senha
        self.senhaMovimentacoes = senhaMovimentacoes
        self.clientes[cpf] = {'Nome': nome, 'Email:': email, 'Idade:':idade, 'Senha': senha, 'Senha para movimentações': senhaMovimentacoes}
     
    def validarCliente(self, cpf, senha):
        for cliente in self.clientes:
            if cliente["CPF"] == cpf and cliente["Senha"] == senha:
                return "ACESSO LIBERADO"
            else:
                return "ACESSO NEGADO"
    
    def validarClientecpf (self,cpf):
        for cliente in self.clientes:
            if cliente["CPF"] == cpf:
                return "CLIENTE ENCONTRADO"
            else:
                return "CLIENTE NÃO ENCONTRADO"
    
    def validarSenha (self, senhaMovimentacoes):
        for cliente in self._clientes:
            if cliente["Senha para movimentações"] == senhaMovimentacoes:
                return "ACESSO LIBERADO"
            else:
                return "ACESSO NEGADO"
            
    def atualizarCadastro(self, nome=None, cpf=None, email=None, idade=None, senha=None, senhaMovimentacoes=None):
        if nome:
            self.nome = nome
        if cpf:
            self.cpf = cpf
        if email:
            self.email = email
        if idade:
            self.idade = idade
        if senha:
            self.senha = senha
        if senhaMovimentacoes:
            self.senhaMovimentacoes = senhaMovimentacoes
        print("Cadastro atualizado com sucesso.")

    def excluirConta(self):
        del self
        print("Cliente excluído com sucesso.")

 
class Cliente:
    def __init__(self):
        self.saldo = 0
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}") 
        else:
            print(f'O valor de R${valor} passou do saldo que você possui.')

    def depositar (self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}") 

    def getSaldo(self):
        return self.saldo

    def transferencia (self, valor, cpfDestinatario):
        if self.saldo >= valor:
            self.saldo -= valor
            cpfDestinatario.depositar(valor)
            print(f"Transferência de R${valor:.2f} realizada para {cpfDestinatario.nome}. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente para a transferência.")