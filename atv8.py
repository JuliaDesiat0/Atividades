idade = int(input("Digite sua idade: "))
cigarros_por_dia = int(input("Digite quantos cigarros você fuma por dia: "))

total_cigarros = cigarros_por_dia * 365 * (idade - 1)
# O número de cigarros fumados até o dia de hoje, desconsiderando o cigarro do dia atual

dias_perdidos = total_cigarros * 10 / (24 * 60)
# O número de dias perdidos devido aos cigarros

print("Você perdeu aproximadamente {:.2f} dias de vida devido ao hábito de fumar.".format(dias_perdidos))