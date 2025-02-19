# Cenário:
# Vamos supor que estamos criando um sistema para registrar e processar as temperaturas
# de uma estação meteorológica automática durante um mês inteiro. A estação grava
# as leituras de temperatura a cada hora, gerando 744 valores no total (24 horas/dia * 31 dias).

# Cada leitura de temperatura é armazenada em uma matriz 2D. A matriz será preenchida automaticamente
# com valores de temperatura. Agora, vamos calcular algumas métricas, como a temperatura média ao meio-dia,
# a maior temperatura do mês e o número de dias com temperaturas quentes ao meio-dia.

# Criar a matriz de temperaturas (31 dias, 24 horas por dia)
temps = [[0.0 for h in range(24)] for d in range(31)]

# A matriz é atualizada automaticamente com as leituras de temperatura...

# Calcular a temperatura média ao meio-dia
total = 0.0

# Iterar pelos dias e somar as leituras do meio-dia (índice 11)
for day in temps:
    total += day[11]

# Calcular a média
average = total / 31
print("Temperatura média ao meio-dia:", average)

# Encontrar a temperatura mais alta durante todo o mês
highest = -100.0

# Iterar por todos os dias e todas as horas para encontrar a temperatura máxima
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("A maior temperatura foi:", highest)

# Contar os dias com temperatura ao meio-dia maior que 20°C
hot_days = 0

# Iterar pelos dias e verificar se a temperatura ao meio-dia é maior que 20°C
for day in temps:
    if day[11] > 20.0:
        hot_days += 1

print(hot_days, "dias estavam quentes.")

# Agora, vamos ver um exemplo de uma matriz tridimensional representando a ocupação de quartos em um hotel

# Criar a matriz de quartos para um hotel com 3 edifícios, 15 andares e 20 quartos por andar
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# Reservar um quarto para dois noivos no segundo edifício, décimo andar, quarto 14
rooms[1][9][13] = True

# Liberar a segunda sala no quinto andar do primeiro edifício
rooms[0][4][1] = False

# Verificar a quantidade de quartos disponíveis no 15º andar do terceiro edifício
vacancy = 0

# Iterar pelas 20 salas no 15º andar do terceiro edifício
for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1

print("Vagas no 15º andar do terceiro edifício:", vacancy)