import json
import valida
from time import sleep
import menu

ADMIN_EMAIL = "phdeoliveira14@gmail.com"
ADMIN_SENHA = "P97hol"

def login():
    while True:
        valida.limpaTerminal()
        email = valida.validaemail()
        senha = valida.validasenha()

        with open('nome.json', 'r', encoding='utf-8') as arq:
            dados = json.load(arq)

        # Verifica se o email existe no arquivo
        if email in dados:
            if dados[email]["Senha"] == senha:
                email_logado = email
                print("\033[32mLogin realizado com sucesso!\033[m")
                sleep(1)

                # Verifica se é o administrador
                if email == ADMIN_EMAIL and senha == ADMIN_SENHA:
                    print("\033[33mModo Administrador ativado!\033[m")
                    sleep(1)
                    menu.menu_admin(email_logado)  # chama o menu do admin
                else:
                    menu.MenuPrincipal(email_logado)  # menu normal para clientes
                return
            else:
                print("\033[31mEmail ou senha incorretos.\033[m")
                input("Pressione Enter para tentar novamente...")
        else:
            print("\033[31mEsse email não está no nosso banco de dados.\033[m")
            input("Pressione Enter para tentar novamente...")
