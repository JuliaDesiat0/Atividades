numero = int(input("Digite um número inteiro: "))

# converte o número em uma string para que possamos iterar sobre seus dígitos
numero_str = str(numero)

# inicializa a variável soma como 0
soma = 0

# itera sobre cada dígito do número e adiciona o cubo do dígito à soma
for digito in numero_str:
    soma += int(digito) ** 3

# verifica se a soma é igual ao número original e exibe uma mensagem apropriada
if soma == numero:
    print(numero, "é um número de Armstrong!")
else:
    print(numero, "não é um número de Armstrong.")