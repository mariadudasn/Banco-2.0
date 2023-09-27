from Classes import*
import os


def main():

    def op_invalida():
        print("\n Opção inválida. \n")
        os.system("pause")
        os.system("cls")
    
    banco = Banco()
    
    y = 0
    while y == 0:
        try:
            os.system("cls")
            print ("BEM-VINDO AO BANCO MMALT-PAY!")
            print ("O que você deseja fazer?")
            print ("[1] CADASTRO")
            print ("[2] LOGIN")
            print ("[3] SAIR")
            menu = int(input(">> "))

            match menu:
                case 1:
                        os.system("cls")
                        print("Preencha as informações abaixo para se cadastrar: \n")
                        nome = input("Nome: ")
                        cpf = int(input("CPF: "))
                        email = input("Email: ")
                        idade = int(input("Idade: "))
                        senha = input("Digite sua senha: ")
                        senhaMovimentacoes = input("Digite uma senha para realizar transferências: ")

                        cliente = Cliente(nome, cpf, email, idade, senha, senhaMovimentacoes)
                        banco.cadastrarCliente(cliente)

                        if idade < 18:
                            print("\nDesculpe, você não pode ter uma conta se sua idade for menor de 18 anos.")     
                        else:
                            print("\n Usuário cadastrado com sucesso!")

                        op = int(input("\n [1] Voltar \n [2] Sair \n \nDigite a opção desejada: "))

                        if op == 1: 
                            y = 0
                            os.system("cls")

                        elif op == 2:
                            y = 1
                    
                        else: 
                            op_invalida()

                case 2:
                        os.system("cls")
                        print("Preencha as informações para acessar sua conta: \n")
                        cpf = int(input("CPF: "))
                        senhaa = input("Digite sua senha: ")
                        validacao = banco.validarCliente(cpf, senhaa)

                        if validacao == 'ACESSO LIBERADO':
                            print("ACESSO LIBERADO")
                            cliente = banco.clientes[cpf]

                            while True:
                                print ("O QUE DESEJA FAZER?")
                                print (" ")
                                op2 = int(input(" [1] DEPÓSITO \n [2] SAQUE \n [3] TRANSFERÊNCIA \n [4] ALTERAR DADOS \n [5] EXCLUIR CONTA \n [6] LISTAR CLIENTES \n [7] VOLTAR AO MENU INICIAL \n [8] SAIR \n \n Digite a opção desejada: "))
                                
                                if op2 == 1:
                                    print("DEPÓSITO")
                                    print("Digite seu cpf para realizar o depósito: ")
                                    cpf1 = input(">> ")
                                    print("Digite sua senha para realizar o depósito: ")
                                    senham1 = input(">> ")

                                    validacao2 = banco.validarSenha(cpf1, senham1)
                                    if validacao2 == 'ACESSO LIBERADO':
                                        cliente.depositar(valor)
                                    else: 
                                        print("Senha incorreta")

                                    os.system("pause")

                                elif op2 == 2:
                                    print("SAQUE")
                                    print("Digite seu cpf para realizar o depósito: ")
                                    cpf2 = input(">> ")
                                    print("Digite sua senha para realizar o saque: ")
                                    senham2 = input(">> ")

                                    validacao3 = banco.validarSenha(cpf2, senham2)
                                    if validacao3 == 'ACESSO LIBERADO':
                                        cliente.sacar(valor)
                                    else: 
                                        print("Senha incorreta")
                                    
                                elif op2 == 3:
                                    print("TRANSFERÊNCIA")
                                    print (f"Seu saldo atual é de R${cliente.getSaldo():.2f}")
                                    print("Digite seu cpf para realizar o depósito: ")
                                    cpf3 = input(">> ")
                                    print("Digite sua senha para realizar a traferência: ")
                                    senham3 = input(">> ")

                                    validacao4 = banco.validarSenha(cpf3, senham3)
                                    if validacao4 == 'ACESSO LIBERADO':
                                        print("Digite o cpf do destinatário: ")
                                        cpfdes = input(">> ")
                                        validacao5 = banco.validarClientecpf(cpfdes)

                                        if validacao5 == 'CLIENTE ENCONTRADO':
                                            print("Digite o valor que deseja transferir: ")
                                            valor = float(input(">> "))
                                            destinatario = banco.clientes [cpfdes]
                                            cliente.transferencia(valor, destinatario)
                                    else: 
                                        print("Senha incorreta")

                                elif op2 == 4:
                                    print("ATUALIZAR DADOS")
                                    cpf = input("Digite o CPF do cliente a ser atualizado: ")
                                    clientee = banco.validarClientecpf(cpf)
                                    if clientee == "CLIENTE ENCONTRADO":
                                        novo_nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ")
                                        novo_cpf = input("Digite o novo CPF (ou pressione Enter para manter o atual): ")
                                        novo_email = input("Digite o novo email (ou pressione Enter para manter o atual): ")
                                        nova_idade = input("Digite a nova idade (ou pressione Enter para manter o atual): ")
                                        nova_senha = input("Digite a nova senha para acesso do sistema (ou pressione Enter para manter o atual): ")
                                        nova_senhaMovimentacoes = input("Digite a nova senha para liberação de movimentações de dinheiro (ou pressione Enter para manter o atual): ")
                                            
                                        cliente_atualizado = Cliente(novo_nome, novo_cpf, novo_email, nova_idade,nova_senha, nova_senhaMovimentacoes)
                                        banco.atualizarCadastro(cliente_atualizado)

                                elif op2 == 5: 
                                    print("EXCLUIR CONTA")
                                    cpf = input("Digite o CPF do cliente a ser excluido: ")
                                    cliente2 = banco.validarClientecpf(cpf)
                                    if cliente2 == 'CLIENTE ENCONTRADO':
                                        banco.excluirConta()

                                elif op2 == 6:
                                    os.system("cls")
                                    print("LISTA DE CLIENTES CADASTRADOS")
                                    clientes = banco.getClientes()
                                    for cpf, info in clientes.items():
                                        print(f"CPF: {cpf}")
                                        for chave, valor in info.items():
                                            print(f"{chave}: {valor}")
                                        print("-" * 20)                                    
                                    os.system("pause")
                                    print (" ")
                                    print("O QUE DESEJA FAZER? \n [1] VOLTAR \n [2] VOLTAR AO MENU INICIAL \n [3] SAIR")
                                    op3 = int(input(">> "))

                                    if op3 == 1:
                                        print ("VOLTANDO...")

                                    elif op3 == 2:
                                        print ("VOLTANDO AO MENU INICIAL...")
                                        break

                                    elif op3 == 2:
                                        print ("SAINDO...")
                                        y = 1
                                    
                                    else: 
                                        op_invalida()

                                elif op2 == 7:
                                    print("VOLTANDO AO MENU INICIAL...")
                                    os.system("pause")
                                    os.system("cls")

                                elif op2 == 8:
                                    print("SAINDO...")
                                    os.system("pause")
                                    os.system("cls")
                                    False
                                    y = 1
                                    

                                else:
                                    op_invalida()

                        else:
                            print("Senha ou CPF inválidos")
                            os.system("pause")
                            os.system("cls")
                            
                case 3:
                    print("SAINDO...")
                    os.system("pause")
                    os.system("cls")
                    y = 1
                
                case _:
                    op_invalida()

        except Exception:
            op_invalida()
