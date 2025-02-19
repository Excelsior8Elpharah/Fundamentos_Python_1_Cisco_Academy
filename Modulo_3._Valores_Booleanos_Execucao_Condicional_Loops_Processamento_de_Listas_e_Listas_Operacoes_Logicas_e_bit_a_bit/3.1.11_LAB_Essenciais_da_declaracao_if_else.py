# Cenário:
# O imposto de renda é calculado conforme a renda do cidadão.
# Se a renda for inferior a 85.528 talões, o imposto é igual a 18% da renda menos 556,02 talões.
# Se a renda for superior a 85.528 talões, o imposto é 14.839,02 talões mais 32% do valor excedente.
# O imposto nunca pode ser negativo. Em caso de cálculo negativo, o imposto é zero.
# O resultado do imposto deve ser arredondado para o inteiro mais próximo.

# Solicitando a entrada da renda
income = float(input("Entre com os rendimentos: "))

# Cálculo do imposto dependendo do valor da renda
if income < 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + (income - 85528) * 0.32

# Garantindo que o imposto não seja negativo
if tax < 0:
    tax = 0

# Arredondando o imposto para o inteiro mais próximo
tax = round(tax, 0)

# Exibindo o imposto calculado
print("A taxa é:", int(tax), "thalers")