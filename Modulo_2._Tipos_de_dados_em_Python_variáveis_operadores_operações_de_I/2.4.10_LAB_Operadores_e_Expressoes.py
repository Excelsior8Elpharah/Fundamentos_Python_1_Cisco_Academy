# Cenário:
# Dê uma olhada no código no editor: ele lê um valor float, coloca-o em uma variável chamada x e imprime o valor de uma variável chamada y.
# Sua tarefa é completar o código para avaliar a seguinte expressão:
# 3x³ - 2x² + 3x - 1
# O resultado deve ser atribuído à variável y.
# Lembre-se de que a notação algébrica clássica gosta de omitir o operador de multiplicação - você precisa usá-la explicitamente.
# Observe como mudamos o tipo de dados para garantir que x seja do tipo float.
# Mantenha seu código limpo e legível e teste-o usando os dados que fornecemos, atribuindo-o sempre à variável x (codificando-o).
# Não desanime por qualquer falha inicial. Seja persistente e inquisitivo.

# Testando com o valor de x = 0
x = 0
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

# Testando com o valor de x = 1
x = 1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

# Testando com o valor de x = -1
x = -1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)