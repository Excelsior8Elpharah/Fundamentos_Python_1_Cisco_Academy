# Cenário
# Ouça esta história: um garoto e seu pai, um programador de computador, estão jogando com blocos de madeira. Eles estão construindo uma pirâmide.
# A pirâmide deles é um pouco esquisita, pois na verdade é uma parede em forma de pirâmide - é plana. A pirâmide é empilhada de acordo com um princípio simples:
# cada camada inferior contém um bloco a mais do que a camada acima.
# Sua tarefa é escrever um programa que lê o número de blocos que os construtores têm e gera a altura da pirâmide que pode ser construída usando esses blocos.
# Nota: a altura é medida pelo número de camadas totalmente concluídas; se os construtores não tiverem um número suficiente de blocos e não puderem concluir a próxima camada, eles terminarão seu trabalho imediatamente.

# Solicita ao usuário que insira o número de blocos
blocks = int(input("Insira o número de blocos:"))

# Inicializa a variável que irá armazenar a altura da pirâmide
height = 0
# Inicializa a variável que irá controlar o número de blocos necessários para cada camada
layer_blocks = 1

# Enquanto houver blocos suficientes para construir a próxima camada
while blocks >= layer_blocks:
    # Consome os blocos para a camada
    blocks -= layer_blocks
    # Aumenta a altura da pirâmide
    height += 1
    # A próxima camada precisará de um bloco a mais
    layer_blocks += 1

# Exibe a altura da pirâmide construída
print("A altura da pirâmide:", height)