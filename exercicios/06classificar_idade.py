#pergunte o usuário sua idade e classifique entre criança, aadolescente e adulto.

def classificar_idade():

    idade_usuario = int(input('Digite sua idade: '))

    if idade_usuario >= 0 and idade_usuario <= 12:
        print('Você é uma criança.')

    elif idade_usuario >= 13 and idade_usuario <= 18:
        print('Você é um(a) adolescente.')

    else:
        print('Você é um adulto.')

classificar_idade()
