import json
import menu
import valida
from time import sleep
def MostrarDados(email):
    valida.limpaTerminal()
    with open ('nome.json', 'r', encoding='utf-8') as arq:
        dados = json.load(arq)
        
    print("\033[34m=== DADOS DE TODOS OS USUÁRIOS ===\033[m")
    for email, info in dados.items():
        print(f'\n Email :{email}')
        for chave, valor in info.items():
            print(f"{chave}: {valor}")
    deseja = input('Deseja atualizar algum desses dados? [s/n] ').strip().lower()

    while deseja not in ['s', 'n']:
        print('\033[1;31mA opção é inválida.\033[m')
        deseja = input('Digite apenas [s/n]: ').strip().lower()

    if deseja == 's':
        return AtualizarDados(email)
    elif deseja == 'n':
        return menu.menu_admin(email)
    
def AtualizarDados(email):
    valida.limpaTerminal()
    with open('nome.json', 'r', encoding='utf-8') as arq:
        dados = json.load(arq)
    print("=== Atualizar Usuário ===")
    email = valida.validaemail()  
    with open('nome.json', 'r', encoding='utf-8') as arq:
        dados = json.load(arq)
    if email not in dados:
        print("\033[31mUsuário não encontrado!\033[m")
        sleep(2)
        return  
    print("\nDados atuais do usuário:")
    for chave, valor in dados[email].items():
        print(f"{chave}: {valor}")

    print("\nO que deseja alterar?")
    print("1 - Nome")
    print("2 - Senha")
    print("3 - Email")
    print("4 - Cancelar")

    opcao = input("Escolha uma opção: ").strip()
    if opcao == '1':
        novo_nome = valida.validanome()
        dados[email]['nome'] = novo_nome
    elif opcao == '2':
        nova_senha = valida.validasenha()
        dados[email]['senha'] = nova_senha
    elif opcao == '3':
        novo_email = valida.validaemail()
        dados[novo_email] = dados[email]  
        del dados[email]                 
    elif opcao == '4':
        print("Alteração cancelada.")
        return
    else:
        print("Opção inválida.")
        return
    with open('nome.json', 'w', encoding='utf-8') as arq:
        json.dump(dados, arq, ensure_ascii=False, indent=4)
    print("\033[32mDados atualizados com sucesso!\033[m")
    
def DeletarContaAdmin(email):
    valida.limpaTerminal()
    print("=== Deletar Conta (Admin) ===")

    email = valida.validaemail()  # Admin informa qual conta deletar

    with open('nome.json', 'r', encoding='utf-8') as arq:
        dados = json.load(arq)

    if email not in dados:
        print("\033[31mUsuário não encontrado!\033[m")
        input("Pressione Enter para voltar...")
        return

    print(f"\nVocê está prestes a deletar a conta de: {email}")
    print(f"Nome: {dados[email].get('Nome')}")
    print(f"Senha {dados[email].get('Senha')}")

    confirma = input("\nTem certeza que deseja deletar esta conta? [s/n]: ").strip().lower()
    while confirma not in ['s', 'n']:
        print("\033[1;31mOpção inválida.\033[m")
        confirma = input("Digite apenas [s/n]: ").strip().lower()

    if confirma == 's':
        del dados[email] 

        with open('nome.json', 'w', encoding='utf-8') as arq:
            json.dump(dados, arq, ensure_ascii=False, indent=4)

        print("\033[32mConta deletada com sucesso!\033[m")
        sleep(2)
    else:
        print("Exclusão cancelada.")
        sleep(1)