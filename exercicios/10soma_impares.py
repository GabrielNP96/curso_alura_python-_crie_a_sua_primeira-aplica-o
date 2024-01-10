#criar uma lista com numeros de 1 a 10 e somar os impares

lista = [0,1,2,3,4,5,6,7,8,9,10]
soma = 0

for numero in lista:
    if(numero % 2 != 0):
        soma += numero
print(soma)
