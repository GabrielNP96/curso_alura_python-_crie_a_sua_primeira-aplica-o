#Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

def verifica_usuario_senha(nome, senha):
    verifica_nome_usuario = input('Digite seu nome de usuário: ')
    verifica_senha = input('Digite sua senha: ')

    if nome != verifica_nome_usuario:
        print(f'usuario {verifica_nome_usuario} não se encontra no nosso sistema.')
    if senha != verifica_senha:
        print('Senha incorreta')
    if nome == verifica_nome_usuario and senha == verifica_senha:
        print('logado')

def cadastro():
    nome_usuario = input('Digite um nome de usuário: ')
    senha = input('Digite uma senha: ')
    verifica_usuario_senha(nome_usuario, senha)


cadastro()