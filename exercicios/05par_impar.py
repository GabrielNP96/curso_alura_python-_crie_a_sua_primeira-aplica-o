# Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

user_number = int(input('Digite um número: '))

def par_impar(): 
    if user_number % 2 == 0:
        print(f'{user_number} é par')
    else:
        print(f'{user_number} é impar')

par_impar()
