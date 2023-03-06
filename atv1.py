# Pedindo que o usuário insira os dois números
num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

# Pedindo que o usuário escolha uma operação
op = input("Escolha uma operação (+, -, *, /): ")

# Verificando se a operação escolhida é válida
if op not in ['+', '-', '*', '/']:
    print("Operação inválida!")
else:
    # Executando a operação escolhida e imprimindo o resultado
    if op == '+':
        print(f"{num1} + {num2} = {num1+num2}")
    elif op == '-':
        print(f"{num1} - {num2} = {num1-num2}")
    elif op == '*':
        print(f"{num1} * {num2} = {num1*num2}")
    else:  # op == '/'
        if num2 == 0:
            print("Não é possível dividir por zero!")
        else:
            print(f"{num1} / {num2} = {num1/num2}")