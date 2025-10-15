from time import sleep
import json
import valida
import sys
import menu

def MostraDados(email):
    valida.limpaTerminal()
    with open('nome.json', 'r', encoding='utf-8') as arq:
        dados = json.load(arq)
        
    print("\033[34m=== SEUS DADOS CADASTRADOS ===\033[m")
    print(f"Email: {email}")
    for chave, valor in dados[email].items():
        print(f"{chave}: {valor}")
    
    deseja = input('Deseja atualizar algum desses dados? [s/n] ').strip().lower()

    while deseja not in ['s', 'n']:
        print('\033[1;31mA opção é inválida.\033[m')
        deseja = input('Digite apenas [s/n]: ').strip().lower()

    if deseja == 's':
        return AtualizarDados(email)
    elif deseja == 'n':
        return menu.MenuPrincipal(email)
        
def AtualizarDados(email_atual):
    valida.limpaTerminal()
    with open('nome.json', 'r', encoding='utf-8') as arq:
        dados = json.load(arq)

    print("\nO que deseja atualizar?")
    print("[1] Nome")
    print("[2] Senha")
    print("[3] Email")
    print("[4] Todos")
     
    opcao = input("Escolha: ").strip()
    while opcao not in ['1', '2', '3', '4']:
        print("\033[31mOpção inválida!\033[m")
        opcao = input("Digite 1, 2, 3 ou 4: ").strip()

    novo_email = email_atual 
    
    # Atualizar Nome
    if opcao in ['1', '4']:
        novo_nome = valida.validanome()
        if novo_nome:
            dados[email_atual]['Nome'] = novo_nome

    # Atualizar Senha
    if opcao in ['2', '4']:
        nova_senha = valida.validasenha()
        if nova_senha:
            dados[email_atual]['Senha'] = nova_senha

    # Atualizar Email (mudar a chave)
    if opcao in ['3', '4']:
        novo_email = valida.validaemail()
        if novo_email == email_atual:
            print("\033[33mO e-mail informado é igual ao atual. Nenhuma alteração feita.\033[m")
        else:
            dados[novo_email] = dados[email_atual]
            del dados[email_atual]
            print("\033[32mE-mail alterado com sucesso!\033[m")

    # Salvar alterações
    with open('nome.json', 'w', encoding='utf-8') as arq:
        json.dump(dados, arq, ensure_ascii=False, indent=4)

    print("\033[32mDados atualizados com sucesso!\033[m")
    input("Pressione Enter para voltar...")

    return novo_email  

def DeletarConta(email):
    valida.limpaTerminal()
    with open('nome.json', 'r', encoding='utf-8') as arq:
        dados = json.load(arq)

    print("\033[33mAtenção! Você está prestes a deletar sua conta.\033[m")
    print("Todos os seus dados serão apagados permanentemente.\n")
    print('Confirme a sua senha abaixo')
    senha = valida.validasenha()
    if senha != dados[email]['Senha']:
        print("\033[31mSenha incorreta. Cancelando exclusão da conta.\033[m")
        sleep(2)
        return email

    confirma = input("Tem certeza que deseja deletar sua conta? [s/n]: ").strip().lower()
    while confirma not in ['s', 'n']:
        print("\033[1;31mOpção inválida.\033[m")
        confirma = input("Digite apenas [s/n]: ").strip().lower()

    if confirma == 's':
        del dados[email]  # remove o usuário do JSON
        with open('nome.json', 'w', encoding='utf-8') as arq:
            json.dump(dados, arq, ensure_ascii=False, indent=4)
        print("\033[32mConta deletada com sucesso!\033[m")
        sleep(2)
        sys.exit()  # encerra o programa após apagar a conta
    else:
        print("Exclusão cancelada. Voltando ao menu...")
        sleep(1)
        return email