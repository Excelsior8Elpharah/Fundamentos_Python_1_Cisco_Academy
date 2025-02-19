# Cenário
# Em 1937, um matemático alemão chamado Lothar Collatz formulou uma hipótese intrigante (ainda não comprovada) que pode ser descrita da seguinte forma:
# - Pegue qualquer número inteiro diferente de zero e nomeie-o como c0;
# - Se for par, avalie um novo c0 como c0 ÷ 2;
# - Caso contrário, se for ímpar, avalie um novo c0 como 3 × c0 + 1;
# - Se c0 ≠ 1, volte ao ponto 2.
# A hipótese diz que, independentemente do valor inicial de c0, ela sempre vai para 1.
# Obviamente, é uma tarefa extremamente complexa usar um computador para provar a hipótese de qualquer número natural (pode até exigir inteligência artificial),
# mas você pode usar o Python para verificar alguns números individuais. Talvez você até encontre aquele que refutaria a hipótese.
# Escreva um programa que leia um número natural e execute as etapas acima, desde que c0 permaneça diferente de 1. 
# Também queremos que você conte as etapas necessárias para atingir o objetivo. Seu código deve gerar todos os valores intermediários de c0 também.

# Solicita ao usuário que insira um número natural
c0 = int(input("Insira um número natural: "))

# Inicializa o contador de etapas
steps = 0

# Loop que segue as regras da hipótese de Collatz até que c0 seja igual a 1
while c0 != 1:
    # Imprime o valor atual de c0
    print(c0, end=" -> ")
    # Se c0 for par, divide por 2
    if c0 % 2 == 0:
        c0 //= 2
    # Se c0 for ímpar, multiplica por 3 e adiciona 1
    else:
        c0 = 3 * c0 + 1
    # Incrementa o contador de etapas
    steps += 1

# Imprime o valor final de c0 (que será 1) e o número de etapas
print(c0)
print(f"Total de etapas: {steps}")