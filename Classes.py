import os

class Usuário:
    def __init__(self):
        self.cliente = {}

    def cadastrarCliente (self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cliente[email] = {'Nome': nome, 'Senha': senha}

    def loginCliente (self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def verificar_usuario(self, email, senha):
        if email in self.cliente and self.cliente[email]['Senha'] == senha:
            return "ACESSO LIBERADO"
        else:
            return "ACESSO NEGADO. Digite os dados novamente ou faça seu cadastro."



class Produtos:
    def __init__(self, nome2, valor):
        self.nome2 = nome2
        self.valor = valor

    def getNome (self):
        return self.nome2
    
    def getValor (self):
        return self.valor
    
class Produtos_Loja:
    lista_loja = []

    def cadastrar_produto(self, nome2, valor):
        produto = Produtos(nome2, valor)
        self.lista_loja.append (produto)
        return "PRODUTO ADICIONADO"

    def listar_produtos(self):
        self.cont = 0
        for x in self.lista_loja:
            self.cont += 1
            print (f"{self.cont} - Nome: {x.getNome()} - Valor: {x.getValor()}")
        
class Carrinho(Produtos_Loja):
    lista_carrinho = []

    def adicionar_produto(self):
        produto_carrinho = self.cont
        self.lista_carrinho.append (produto_carrinho)
        return "PRODUTO ADICIONADO AO CARRINHO"

    def visualizar_carrinho(self):
        pass

    def excluir_produto(self):
        pass