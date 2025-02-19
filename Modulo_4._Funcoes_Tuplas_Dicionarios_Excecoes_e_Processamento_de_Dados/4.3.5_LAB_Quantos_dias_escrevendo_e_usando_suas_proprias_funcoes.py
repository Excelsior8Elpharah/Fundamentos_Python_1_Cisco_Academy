# 4.3.5   LAB   Quantos dias: escrevendo e usando suas próprias funções
# Sua tarefa é escrever e testar uma função que usa dois argumentos (um ano e um mês) e retorna o número de dias para o determinado par de ano-mês (embora apenas fevereiro seja sensível ao valor do year, sua função deve ser universal).
# A parte inicial da função está pronta. Agora, convença a função a não retornar None se os argumentos não fizerem sentido.
# Obviamente, você pode (e deve) usar a função previamente testada e escrita (LAB 4.3.1.6). Pode ser muito útil. Recomendamos que você use uma lista com os comprimentos dos meses. Você pode criá-la dentro da função - esse truque diminuirá significativamente o código.

# Função que determina se um ano é bissexto
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

# Função que retorna o número de dias de um determinado mês de um ano
def days_in_month(year, month):
    # Verifica se o ano e o mês são válidos
    if year < 1582 or month < 1 or month > 12:
        return None  # Retorna None se os argumentos forem inválidos
    # Lista com o número de dias de cada mês (index 0 é janeiro, index 1 é fevereiro, etc.)
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res = days[month - 1]  # Pega o número de dias do mês
    # Se o mês for fevereiro e o ano for bissexto, ajusta para 29 dias
    if month == 2 and is_year_leap(year):
        res = 29
    return res

# Dados de teste para os anos e meses
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

# Teste para verificar se a função retorna o número correto de dias
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "-> ", end="")
    result = days_in_month(yr, mo)  # Chama a função para obter o número de dias
    if result == test_results[i]:
        print("OK")  # Se o resultado for correto, imprime "OK"
    else:
        print("Fracassado")  # Caso contrário, imprime "Fracassado"