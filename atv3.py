num = int(input("Digite um número inteiro: "))

# Verifica se o número é menor ou igual a 1
if num <= 1:
    print("O número não é primo")

# Verifica se o número é divisível por algum número entre 2 e a sua metade
for i in range(2, num//2+1):
    if num % i == 0:
        print("O número não é primo")
        break

# Se não encontrou nenhum divisor, o número é primo
else:
    print("O número é primo")