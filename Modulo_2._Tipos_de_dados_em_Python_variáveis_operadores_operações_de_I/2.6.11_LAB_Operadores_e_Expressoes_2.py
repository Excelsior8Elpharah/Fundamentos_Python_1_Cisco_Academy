# Cenário:
# Sua tarefa é preparar um código simples capaz de avaliar a hora de término de um período, dado como um número de minutos (pode ser arbitrariamente grande).
# A hora de início é fornecida como um par de horas (0..23) e minutos (0..59). O resultado deve ser impresso no console.
# Por exemplo, se um evento começa às 12:17 e dura 59 minutos, termina às 13:16.
# Não se preocupe com imperfeições no código - tudo bem se ele aceitar um tempo inválido - o mais importante é que o código produza resultados válidos para dados de entrada válidos.
# Teste seu código com cuidado. Dica: usar o operador % pode ser a chave para o sucesso.

# Solicitando ao usuário a hora de início (horas, minutos) e a duração do evento
hour = int(input("Hora de início (horas): "))
mins = int(input("Hora de início (minutos): "))
dura = int(input("Duração do evento (minutos): "))

# Encontrando o total de minutos somando a duração
mins = mins + dura

# Encontrando as horas escondidas nos minutos e atualizando a hora
hour = hour + mins // 60

# Corrigindo os minutos para garantir que fiquem no intervalo (0..59)
mins = mins % 60

# Corrigindo as horas para garantir que fiquem no intervalo (0..23)
hour = hour % 24

# Imprimindo a hora de término no formato "hora:minutos"
print(hour, ":", mins, sep='')