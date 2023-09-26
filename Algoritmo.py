from Classes import *
import os

usuario = Usuário()
ploja = Produtos_Loja()

def main():
    sair = False
    while sair == False:
        try:
            os.system("cls")
            print("---BEM VINDO A PAPELARIA MOON---")
            print("---MENU INICIAL---")
            print("01 - CADASTRAR")
            print("02 - LOGIN")
            print("00 - SAIR")
            print("--------")
            print ("")

            print ("Qual opção deseja?")
            menu = int(input(">> "))
            os.system ("pause")

            match menu:
                case 1:
                    os.system ("cls")
                    print ("---CADASTRAR---")
                    print ("INFORME OS SEUS DADOS")
                    nome = input ("Nome - ")
                    email = input ("Email - ")
                    senha = input("Senha - ")
                
                    usuario.cadastrarCliente (nome, email, senha)
                
                    print ("VOCÊ FOI CADASTRADO")
                    print ("-------------------")
                    os.system("pause")

                case 2:
                    os.system("cls")
                    print ("---LOGIN---")
                    print ("INFORME OS SEUS DADOS")
                    nome = input ("Email - ")
                    senha = input("Senha - ")

                    resultado = usuario.verificar_usuario(email,senha)
                    print (resultado)
                    os.system("pause")





                    if resultado == 'ACESSO LIBERADO':
                        s = 0
                        while s == 0:
                            os.system("cls")
                            print("---MENU---")
                            print("01 - CADASTRAR PRODUTO")
                            print("02 - LISTAR PRODUTOS")
                            print("03 - ADICIONAR AO CARRINHO")
                            print("04 - VISUALIZAR CARRINHO")
                            print("05 - EXCLUIR PRODUTO DO CARRINHO")
                            print("06 - VOLTAR")
                            print("00 - SAIR")
                            print("--------")
                            print ("") 

                            print ("Qual opção deseja?")

                            menu2 = int(input(">> "))

                            os.system ("pause")

                            l = 0
                            while l == 0:
                                match menu2:
                                    case 1:
                                        os.system ("cls")
                                        print ("---CADASTRAR PRODUTO---")
                                        print ("INFORME AS INFORMAÇÕES NECESSÁRIAS")

                                        nome2 = input ("Qual o nome do produto? \n >>")
                                        valor = float(input ("Qual o valor do produto? \n >>"))
                                        

                                        produtos = ploja.cadastrar_produto(nome2, valor)
                                        print (produtos)
                                        os.system("pause")

                                        if produtos == 'PRODUTO ADICIONADO':
                                            z = 0
                                            while z == 0:
                                                os.system("cls")
                                                print("PRODUTO ADICIONADO")
                                                print("---O QUE DESEJA FAZER AGORA?---")
                                                print("01 - ADICIONAR OUTRO PRODUTO")
                                                print("02 - VOLTAR PARA O MENU")
                                                print("03 - VOLTAR PARA O MENU INICIAL")
                                                print("00 - SAIR")
                                                print("--------")
                                                print ("") 

                                                print ("Qual opção deseja?")

                                                menu3 = int(input(">> "))

                                                os.system ("pause")

                                                match menu3:
                                                    case 1:
                                                        z = 1

                                                    case 2:
                                                        z = 1
                                                        l = 1

                                                    case 3:
                                                        z = 1
                                                        l = 1
                                                        s = 1

                                                    case 0:
                                                        print ("SAINDO...")
                                                        print ("------")
                                                        z = 1
                                                        l = 1
                                                        s = 1
                                                        sair = True

                                                    case _:
                                                        print("Valor inválido")
                                                        print ("-------")

                                        os.system("pause")
                                    
                                    case 2:
                                        ploja.listar_produtos()
                                        l = 1
                                        os.system("pause")
                                        g = 0
                                        while g == 0:
                                            os.system("cls")
                                            print("---O QUE DESEJA FAZER AGORA?---")
                                            print("01 - VOLTAR PARA O MENU")
                                            print("02 - VOLTAR PARA O MENU INICIAL")
                                            print("00 - SAIR")
                                            print("--------")
                                            print ("") 

                                            print ("Qual opção deseja?")

                                            menu4 = int(input(">> "))

                                            os.system ("pause")

                                            match menu4:
                                                case 1:
                                                    g = 1
                                                    l = 1

                                                case 2:
                                                    g = 1
                                                    l = 1
                                                    s = 1

                                                case 0:
                                                    print ("SAINDO...")
                                                    print ("------")
                                                    g = 1
                                                    l = 1
                                                    s = 1
                                                    sair = True

                                                case _:
                                                    print("Valor inválido")
                                                    print ("-------")
                                           

                                    case 3:
                                        ploja.listar_produtos()
                                        f = 1
                                        os.system("pause")
                                        g = 0
                                        while g == 0:
                                            os.system("cls")
                                            print("---O QUE DESEJA FAZER AGORA?---")
                                            print("01 - VOLTAR PARA O MENU")
                                            print("02 - VOLTAR PARA O MENU INICIAL")
                                            print("00 - SAIR")
                                            print("--------")
                                            print ("") 

                                            print ("Qual opção deseja?")

                                            menu4 = int(input(">> "))

                                            os.system ("pause")

                                            match menu4:
                                                case 1:
                                                    g = 1
                                                    f = 1

                                                case 2:
                                                    g = 1
                                                    f = 1
                                                    s = 1

                                                case 0:
                                                    print ("SAINDO...")
                                                    print ("------")
                                                    g = 1
                                                    f = 1
                                                    s = 1
                                                    sair = True

                                                case _:
                                                    print("Valor inválido")
                                                    print ("-------")

                                    case 4:
                                        pass

                                    case 5:
                                        pass

                                    case 6:
                                        l = 1
                                        s = 1

                                    case 0:
                                        print ("SAINDO...")
                                        print ("------")
                                        l = 1
                                        s = 1
                                        sair = True

                                    case _:
                                        print("Valor inválido")
                                        print ("-------")

        

                case 0:
                    print ("SAINDO...")
                    print ("------")
                    sair = True

                case _:
                    print("Valor inválido")
                    print ("-------")
        
        except Exception as erro:
            print ("Valor inválido")
            print (erro.__class__.__name__)
            print("")
