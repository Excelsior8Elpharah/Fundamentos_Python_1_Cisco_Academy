# 4.5.1 Funções de Exemplo: avaliando o IMC
# Vamos começar uma função para avaliar o índice de massa corporal (IMC).
# Como você pode ver, a fórmula obtém dois valores:
# - peso (originalmente em quilogramas)
# - altura (originalmente em metros)
# Parece que essa nova função terá dois parâmetros. O nome será bmi, mas se você preferir outro nome, use-o.

# Função para calcular o IMC
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None  # Verifica se os valores são confiáveis
    return weight / height ** 2

# Teste para avaliar o IMC com valores válidos
print(bmi(52.5, 1.65))

# Agora vamos incluir as funções para conversão de unidades imperiais para métricas

# Função auxiliar para converter libras em quilogramas
def lb_to_kg(lb):
    return lb * 0.45359237

# Teste de conversão de libras para quilogramas
print(lb_to_kg(1))

# Função auxiliar para converter pés e polegadas em metros
def ft_and_inch_to_m(ft, inch=0.0):
    return ft * 0.3048 + inch * 0.0254

# Teste de conversão de pés e polegadas para metros
print(ft_and_inch_to_m(1, 1))

# Função completa para calcular o IMC com unidades imperiais
def ft_and_inch_to_m(ft, inch=0.0):
    return ft * 0.3048 + inch * 0.0254

def lb_to_kg(lb):
    return lb * 0.4535923

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    return weight / height ** 2

# Teste final para calcular o IMC com altura de 5'7" e peso de 176 libras
print(bmi(weight=lb_to_kg(176), height=ft_and_inch_to_m(5, 7)))
