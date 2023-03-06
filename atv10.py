# solicita ao usuário que insira três números inteiros
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))

# cria uma lista com os três números
lista_numeros = [num1, num2, num3]

# ordena a lista em ordem crescente
lista_numeros.sort()

# exibe os números em ordem crescente
print("Os números em ordem crescente são:", lista_numeros[0], lista_numeros[1], lista_numeros[2])