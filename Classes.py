class Banco:
    def __init__(self):
        self.clientes = {}
    
    def getClientes(self):
        return self.clientes
    
    def cadastrarCliente (self, cliente):
        self.clientes[cliente.cpf] = {
            'Nome': cliente.nome, 
            'Email': cliente.email, 
            'Idade':cliente.idade, 
            'Senha': cliente.senha, 
            'Saldo': cliente.saldo,
            }

    def validarCliente(self, cpf, senha):
        if cpf in self.clientes:
            if self.clientes[cpf]["Senha"] == senha:
                return self.clientes[cpf]
            else:
                return None
        else:
            return None
        
    def validarClientecpf (self,cpf):
        if cpf in self.clientes:
            return "CLIENTE ENCONTRADO"
        else:
            return "CLIENTE NÃO ENCONTRADO"
            
    def atualizarCadastro(self, cpf, nome=None, email=None, idade=None, senha=None):
        if cpf in self.clientes:
            cliente = self.clientes[cpf]
            if nome:
                cliente['Nome'] = nome
            if email:
                cliente['Email'] = email
            if idade:
                cliente['Idade'] = idade
            if senha:
                cliente['Senha'] = senha
            print("Cadastro atualizado com sucesso.")
        else:
            print("CPF não encontrado.")

    def excluirConta(self, cpf):
        if cpf in self.clientes:
            del self.clientes[cpf]
            print("Cliente excluído com sucesso.")
        else:
            print("CPF não encontrado.")

 
class Cliente:
    def __init__(self, nome, cpf, email, idade, senha, saldo=0):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.idade = idade
        self.senha = senha
        self.saldo = saldo
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}") 
        else:
            print(f'O valor de R${valor} passou do saldo que você possui.')

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}") 

    def getSaldo(self):
        return self.saldo

    def transferencia (self, valor, destinatario):
        if self.saldo >= valor:
            self.saldo -= valor
            destinatario.depositar(valor)
            print(f"Transferência de R${valor:.2f} realizada para {destinatario.nome}. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente para a transferência.")