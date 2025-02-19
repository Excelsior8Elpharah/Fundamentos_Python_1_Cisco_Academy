# Cenário:
# Sua tarefa é completar o código para avaliar a seguinte expressão:
# Expressão matemática:
# O resultado deve ser atribuído a y.
# Tenha cuidado - observe os operadores e mantenha suas prioridades em mente.
# Não hesite em usar quantos parênteses forem necessários.
# Você pode usar variáveis adicionais para encurtar a expressão (mas não é necessário).
# Teste seu código com cuidado.

# Solicitando ao usuário o valor de x
x = float(input("Digite o valor para x: "))

# Calculando a expressão e atribuindo o resultado à variável y
y = 1./(x + 1./(x + 1./(x + 1./x)))

# Imprimindo o valor de y
print("y =", y)