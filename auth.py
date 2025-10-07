import cadastro
import os
from time import sleep
import json


def cadastrar():
    cadastro.limpaTerminal()
    nome = cadastro.validanome()
    senha = cadastro.validasenha()
    email = cadastro.validaemail()

    if os.path.exists('nome.json'):
        with open('nome.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
    else:
        dados = {}  # começa vazio

    dados[email] = {"Nome": nome, "Senha": senha}
    
        # Salva os dados no JSON
    with open('nome.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    print(f'Usuário "{nome}" cadastrado com sucesso!')

if __name__ == "__main__":
    cadastrar()