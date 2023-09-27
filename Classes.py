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
     
    def validarCliente(self, cpf, senha):
        for cliente in self._clientes:
            if cliente["CPF"] == cpf and cliente["Senha"] == senha:
                return "ACESSO LIBERADO"
            else:
                return "ACESSO NEGADO. Digite os dados novamente ou faça seu cadastro."

    # def excluir_conta(self):
    #     del self
    #     print("Cliente excluído com sucesso.")

 
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

    # def transferencia (self,valor,cliente_a, cliente_b,cpf, senha,saldo):
    #     cliente_a.saldo = cliente_a.depositar()
    #     cliente_b.saldo = cliente_b.depositar()
            
    #     cliente_a = Banco.validar_cliente_por_cpf_e_senha()

    #     if cpf and senha in clientes:
    #         cliente_b = int (input("Informe o CPF do destinatário",cpf))
    #         for cpf, in clientes:
    #             valor = float (input("Informe a quantia que deseja transferir:"))
    #             cliente_b.saldo = cliente_b.saldo + valor
    #             cliente_a.saldo = cliente_a.saldo - valor
    #             print ("Transferencia no valor de R$",valor, "concluída")
    #         else:
    #             print ("Usuário não encontrado")
    #     else:
    #         print ("Usuário não encontrado")