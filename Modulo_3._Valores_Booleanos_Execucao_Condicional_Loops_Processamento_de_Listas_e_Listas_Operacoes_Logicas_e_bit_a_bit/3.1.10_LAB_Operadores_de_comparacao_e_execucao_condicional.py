# Cenário:
# Imagine que seu programa de computador adora essas fábricas. Sempre que recebe uma entrada na forma da palavra Spathiphyllum, involuntariamente grita para o console a seguinte string: "Spathiphyllum é a melhor fábrica de todos os tempos!"
# Escreva um programa que utilize o conceito de execução condicional, use uma string como entrada e:
# - Imprime a frase "Sim - Spathiphyllum é a melhor fábrica de todos os tempos!" se a sequência inserida for "Spathiphyllum" (maiúscula)
# - Imprime "Não, eu quero um grande Spathiphyllum!" se a sequência inserida for "spathiphyllum" (letra minúscula)
# - Imprime "Spathiphyllum! Not[input]!" caso contrário, com o valor de [input] sendo a string inserida.

# Solicitando o nome da flor como entrada
name = input("Insira o nome da flor: ")

# Condições baseadas na string inserida
if name == "Spathiphyllum":
    print("Sim - Spathiphyllum é a melhor planta de todos os tempos!")
elif name == "spathiphyllum":
    print("Não, eu quero uma grande Spathiphyllum!")
else:
    print("Spathiphyllum! Não", name + "!")