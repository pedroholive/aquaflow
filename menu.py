from time import sleep
import auth
def MenuInicial(usuario): 
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
            print('Ir para o cadastro')
        elif opcao == '3':
            print('Encerrando programa...')
            sleep(1)
            return None
        else:
            print('\033[1;31mA opção é inválida.\033[m')
            sleep(1)

if __name__ == "__main__":
    usuario = None  # pode ser um dicionário ou lista de usuários futuramente
    MenuInicial(usuario)