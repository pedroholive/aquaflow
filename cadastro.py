import os


def limpaTerminal(): 
    #Função para limpar o terminal 
    return os.system('cls' if os.name == 'nt' else 'clear')


def validanome():
    #Função para inserir o nome e validá-lo
    while True:
        nome = input('Nome: ').strip()
        if nome == '':
            print('\033[31;mERRO! Entrada inválida\033[m')
            continue
        temp = ''.join(nome.split(' '))
        if not temp.isalpha():
            print('\033[31mERRO! Digite um nome válido (somente letras)\033[m')
            continue
        else:
            return nome.strip(' ')
def validasenha():
    #Função para inserir a senha e validá-la
    while True:
        senha = input("Senha: ").strip()
        if senha == '':
            print('\033[31mERRO! Entrada inválida\033[m')
            continue
        if len(senha) < 4 or len(senha) > 8:
            print('\033[31mERRO! A senha deve conter entre 4 e 8 caracteres.\033[m')
            continue
        if senha == senha.lower():
            print('\033[31mERRO! Sua senha deve conter pelo menos uma letra maiúscula.\033[m')
            continue
        tem_numero = False
        for char in senha:
            if char.isdigit():
                tem_numero = True
                break
        if not tem_numero:
            print('\033[31mERRO! Sua senha deve conter pelo menos um número.\033[m')
            continue
        
        return senha

def verificaemail(email):
    return email.endswith('@gmail.com')

def validaemail(): 
    while True:
        email = input("Digite seu email: ").strip().lower()
        if email == '':
            print('\033[31mERRO! Entrada inválida\033[m')
            continue
        if not verificaemail(email):
            print('\033[31mERRO! O email deve conter "@gmail.com".\033[m')
            continue
        return email
    

