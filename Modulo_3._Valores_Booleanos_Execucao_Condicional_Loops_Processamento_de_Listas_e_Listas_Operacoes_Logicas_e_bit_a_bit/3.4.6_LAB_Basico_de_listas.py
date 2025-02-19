# Cenário
# Era uma vez um chapéu. O chapéu não continha coelhos, mas uma lista de cinco números: 1, 2, 3, 4 e 5.
# Sua tarefa:
# - Escreva uma linha de código que solicite que o usuário substitua o número do meio na lista por um número inteiro inserido pelo usuário (Etapa 1)
# - Escreva uma linha de código que remova o último elemento da lista (Etapa 2)
# - Escreva uma linha de código que imprima o comprimento da lista atual (Etapa 3)
# hat_list = [1, 2, 3, 4, 5]  # Esta é uma lista atual de números ocultos no hat.

# Lista inicial
hat_list = [1, 2, 3, 4, 5]

# Etapa 1: Solicita ao usuário que substitua o número do meio
hat_list[2] = int(input("Insira um número inteiro para substituir o número do meio: "))

# Etapa 2: Remove o último elemento da lista
hat_list.pop()

# Etapa 3: Imprime o comprimento da lista atual
print("O comprimento da lista atual é:", len(hat_list))

# Imprime a lista final
print(hat_list)
