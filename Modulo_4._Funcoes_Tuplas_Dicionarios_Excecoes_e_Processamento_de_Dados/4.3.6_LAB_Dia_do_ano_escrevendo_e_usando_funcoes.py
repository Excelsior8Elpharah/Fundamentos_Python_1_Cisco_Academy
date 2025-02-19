# 4.3.6   LAB   Dia do ano: escrevendo e usando funções
# Sua tarefa é escrever e testar uma função que usa três argumentos (um ano, um mês e um dia do mês) e retorna o dia correspondente do ano ou retorna None se algum dos argumentos for inválido.
# Use as funções escritas e testadas anteriormente. Adicione seus próprios casos de teste ao código.

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

# Função que retorna o número do dia correspondente do ano (ex: 1 de janeiro é o dia 1, 31 de dezembro é o dia 365/366)
def day_of_year(year, month, day):
    days = 0
    # Soma os dias de todos os meses anteriores ao mês fornecido
    for m in range(1, month):
        md = days_in_month(year, m)
        if md == None:
            return None  # Retorna None se o mês for inválido
        days += md
    # Verifica se o dia é válido para o mês fornecido
    md = days_in_month(year, month)
    if day >= 1 and day <= md:
        return days + day  # Retorna o número do dia no ano
    else:
        return None  # Retorna None se o dia não for válido

# Teste de exemplo para o dia 31 de dezembro de 2000
print(day_of_year(2000, 12, 31))  # Esperado: 366, pois 2000 é um ano bissexto