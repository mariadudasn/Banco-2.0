from Classes import*
import os


def main():

    def op_invalida():
        print("\n Opção inválida. \n")
        os.system("pause")
        os.system("cls")
    
    cliente = Cliente()
    banco = Banco()
    
    while y == 0:
        try:
            print ("BEM-VINDO AO BANCO MMALT-PAY!")
            print ("O que você deseja fazer?")
            print ("[1] CADASTRO")
            print ("[2] LOGIN")
            print ("[3] SAIR")
            menu = int(input(">> "))
            match menu:
                case 1:
                    try:
                        os.system("cls")
                        print("Preencha as informações abaixo para se cadastrar: \n")
                        nome = input("Nome: ")
                        cpf = int(input("CPF: "))
                        email = input("Email: ")
                        idade = int(input("Idade: "))
                        senha = input("Digite sua senha: ")
                        senhaMovimentacoes = input("Digite uma senha para realizar transferências: ")
                        banco.cadastrarCliente(nome, cpf, email, idade, senha, senhaMovimentacoes)

                        if idade < 18:
                            print("\nDesculpe, você não pode ter uma conta se sua idade for menor de 18 anos.")     
                        else:
                            print("\n Usuário cadastrado com sucesso!")

                        op = int(input("\n [1] Voltar \n [2] Sair \n \nDigite a opção desejada: "))

                        if op == 1: #Voltar
                            y = 0
                            os.system("cls")

                        elif op == 2: #Sair
                            y = 1
                    
                        else: #Opção inválida
                            op_invalida()
                            
                    except Exception:
                        op_invalida()

                case 2:
                    try:
                        os.system("cls")
                        print("Preencha as informações para acessar sua conta: \n")
                        cpf = int(input("CPF: "))
                        senhaa = input("Digite sua senha: ")
                        validacao = banco.validarCliente(cpf, senhaa)

                        if validacao == 'ACESSO LIBERADO':
                            os.system("cls")
                            op2 = int(input("[1] DEPÓSITO \n [2] SAQUE \n [3] TRANSFERÊNCIA \n [4] ALTERAR DADOS \n [5] EXCLUIR CONTA  \n [6] VOLTAR AO MENU INICIAL \n \n Digite a opção desejada: "))
                            match op2:
                                case 1:
                                    print("DEPÓSITO")
                                    cliente.depositar()
                                case 2:
                                    print("SAQUE")
                                    cliente.sacar()
                                case 3:
                                    print("TRANSFERÊNCIA")
                                    print (f"Seu saldo atual é de R${getSaldo()}")
                                    print("Digite sua senha para realizar a traferência: ")
                                    senham = input(">> ")

                                    validacao4 = banco.validarSenha(senham)
                                    if validacao4 == 'ACESSO LIBERADO':
                                        print("Digite o cpf do destinatário: ")
                                        cpfdes = input(">> ")
                                        validacao5 = banco.validarCliente()

                    except Exception:
                        op_invalida()

                    # if trava == 1: #teste
                    #     os.system("cls")
                    #     print("Preencha as informações para acessar sua conta. \n")
                    #     cpf = int(input("CPF: "))
                    #     senhaa = getpass.getpass("Digite sua senha: ")
                    #     cliente_encontrado = banco.validar_cliente_por_cpf_e_senha(cpf, senhaa)

                    #     if cliente_encontrado:
                    #         os.system("cls")
                    #         op = int(input("[1] Transferência \n [2] Depósito \n [3] Saque \n [4] Alterar dados \n [5] Excluir conta  \n [6] Voltar \n \n Digite a opção desejada: "))
                    #         match op:
                    #             case 1:
                    #                 print("Lógica tranferência")
                    #                 cliente.transferencia()
                    #             case 2:
                    #                 print("Lógica depósito")
                    #                 cliente.depositar()
                    #             case 3:
                    #                 print("Lógica saque")
                    #                 cliente.sacar()
                    #             case 4:
                    #                 os.system("cls")
                    #                 menu2 = int(input("\n O que você deseja alterar? \n \n [1] Nome \n [2] Email \n [3] Telefone \n [4] CPF \n [5] Senha \n [6] Idade \n \n Digite a opção desejada: "))
                    #                 match menu2:
                    #                     case 1:
                    #                         novo_nome = input("Digite o novo nome: ")
                    #                         cliente.setNome(novo_nome)
                    #                     case 2:
                    #                         novo_email = input("Digite o novo email: ")
                    #                         cliente.setEmail(novo_email)
                    #                     case 3:
                    #                         novo_telefone = input("Digite o novo telefone: ")
                    #                         cliente.setTelefone(novo_telefone)
                    #                     case 4:   
                    #                         novo_cpf = input("Digite o novo CPF: ")
                    #                         cliente.setCPF(novo_cpf)
                    #                     case 5:
                    #                         nova_senha = input("Digite a nova senha: ")
                    #                         cliente.setSenha(nova_senha)
                    #                     case 6:
                    #                         nova_idade = input("Digite a nova idade: ")
                    #                         cliente.setIdade(nova_idade)
                            
                        #         case 5:
                        #             print("Lógica excluir conta")
                        #         case 6:
                        #             os.system("cls")
                        #         case _:
                        #             op_invalida()
                        # else:
                        #     print("Cliente não encontrado.")
                
                
                case 3:
                    y = 1
                
                case _:
                    op_invalida()

        except Exception:
            op_invalida()
