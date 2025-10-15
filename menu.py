from time import sleep
import auth
import login
import dados
import sys
import modoadm
def MenuInicial():
    opcao = ''
    while opcao != '3':
        print('\033[1;34m--- AquaFlow ---\033[m')
        print('1 - Cadastro')
        print('2- Login')
        print('3 - Sair do programa')
        
        opcao = input('Escolha uma opção: ').strip()
        if opcao == '1':
            auth.cadastrar()
        elif opcao == '2':
            login.login()
        elif opcao == '3':
            print('Encerrando programa...')
            sleep(1)
            break
        else:
            print('\033[1;31mA opção é inválida.\033[m')
            sleep(1)
            
def menu_admin(email_logado):
    while True:
        print("\n--- MENU ADMINISTRATIVO ---")
        print("1 - Gerenciar Estoque")
        print("2 - Visualizar Dados")
        print("3 - Configurações")
        print('4 - Deletar conta')
        print("4 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("Abrindo menu de estoque...")
        elif opcao == "2":
            modoadm.MostrarDados(email_logado)
        elif opcao == "3":
            print("Configurações do sistema...")
        elif opcao == '3':
            modoadm.DeletarContaAdmin(email_logado)
        elif opcao == "4":
            print("Saindo do modo ADM...")
            sleep(1)
            break
        else:
            print("Opção inválida!")
            sleep(1)
            
def MenuPrincipal(email_logado):
    opcao = ''
    while opcao != '4':
        print('\033[1;34m--- Menu principal ---\033[m')
        print('1 - Configurações')
        print('2- Compras')
        print('3 - Rankings')
        print('4 - Fechar programa')
        
        opcao = input('Escolha uma opção: ').strip()
        if opcao == '1':
            configuracoes(email_logado)
        elif opcao == '2':
            print('Compras')
        elif opcao == '3':
            print('Rankings')
        elif opcao == '4':
            print('Fechando programa...')
            sleep(1)
            sys.exit()
        else:
            print('\033[1;31mA opção é inválida.\033[m')
            sleep(1)
def configuracoes(email_logado):
    opcao = ''
    while opcao != '4':
        print('\033[1;34m---Configurações---\033[m')
        print('1 - Ver dados')
        print('2- Atualizar Dados')
        print('3 - Deletar Conta')
        print('4 - Retornar ao Menu principal')
        
        opcao = input('Escolha uma opção: ').strip()
        if opcao == '1':
            dados.MostraDados(email_logado)
        elif opcao == '2':
            dados.AtualizarDados(email_logado)
        elif opcao == '3':
            dados.DeletarConta(email_logado)
        elif opcao == '4':
            print('Retornando ao Menu principal...')
            sleep(1)
            MenuPrincipal(email_logado)
            break
        else:
            print('\033[1;31mA opção é inválida.\033[m')
            sleep(1)
if __name__ == "__main__":
    MenuInicial()