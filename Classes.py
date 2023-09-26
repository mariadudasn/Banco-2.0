clientes = []
class Banco:
    def __init__(self):
            self._clientes = {}
    
    def cadastrarCliente (self, nome, cpf, email, idade, senha):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.idade = idade
        self.senha = senha
        self._clientes[nome] = {'CPF': cpf, 'Email:': email, 'Idade:':idade, 'Senha': senha}
     
    def validar_cliente_por_cpf_e_senha(self, cpf, senha):
        for cliente in self._clientes:
            if cliente["CPF"] == cpf and cliente["Senha"] == senha:
                return cliente
        return None
        
    def excluir_conta(self):
        del self
        print("Cliente excluído com sucesso.")

 
class Cliente:
    def __init__(self):
        self._valor = 0
        self._cpf = 0
        self._senha = ""
        self._saldo = 0
        self._cliente_b = ""
        self._cliente_a = ""

    def sacar(self, valor):
        if(self.__if_saque(valor)):
            self.__saldo -= valor

        else:
            print(f'o valor de {valor} passou o limite para saque')


    def depositar (self, valor, nome, cpf, saldo):
        if valor > 0:
            self.saldo += valor
            self.nome = nome
            self.cpf = cpf
            print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}") 

    def transferencia (self,valor,cliente_a, cliente_b,cpf, senha,saldo):
        cliente_a.saldo = cliente_a.depositar()
        cliente_b.saldo = cliente_b.depositar()
            
        cliente_a = Banco.validar_cliente_por_cpf_e_senha()

        if cpf and senha in clientes:
            cliente_b = int (input("Informe o CPF do destinatário",cpf))
            for cpf, in clientes:
                valor = float (input("Informe a quantia que deseja transferir:"))
                cliente_b.saldo = cliente_b.saldo + valor
                cliente_a.saldo = cliente_a.saldo - valor
                print ("Transferencia no valor de R$",valor, "concluída")
            else:
                print ("Usuário não encontrado")
        else:
            print ("Usuário não encontrado")