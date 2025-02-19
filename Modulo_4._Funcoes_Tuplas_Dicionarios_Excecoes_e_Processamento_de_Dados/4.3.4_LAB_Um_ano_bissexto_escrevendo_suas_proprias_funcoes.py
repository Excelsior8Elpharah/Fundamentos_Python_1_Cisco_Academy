# 4.3.4   LAB   Um ano bissexto: escrevendo suas próprias funções: cenário
# Sua tarefa é escrever e testar uma função que usa um argumento (um ano) e retorna True se o ano for um ano bissexto ou False caso contrário.
# A semente da função já é mostrada no código esqueleto do editor.
# Nota: também preparamos um código de teste curto, que você pode usar para testar sua função.
# O código usa duas listas - uma com os dados de teste e a outra contendo os resultados esperados. O código informará se algum dos resultados é inválido.

# Função que determina se um ano é bissexto
def is_year_leap(year):
    # Se o ano não for múltiplo de 4, não é bissexto
    if year % 4 != 0:
        return False
    # Se for múltiplo de 4, mas não de 100, é bissexto
    elif year % 100 != 0:
        return True
    # Se for múltiplo de 100, mas não de 400, não é bissexto
    elif year % 400 != 0:
        return False
    # Se for múltiplo de 400, é bissexto
    else:
        return True

# Dados de teste com anos e os resultados esperados
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

# O código abaixo testa se a função retorna o resultado esperado
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "-> ", end="")
    result = is_year_leap(yr)  # Chama a função para verificar o ano
    # Compara o resultado da função com o valor esperado
    if result == test_results[i]:
        print("OK")  # Se o resultado for correto, imprime "OK"
    else:
        print("Fracassado")  # Caso contrário, imprime "Fracassado"