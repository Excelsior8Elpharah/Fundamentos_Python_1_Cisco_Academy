# Cenário
# A instrução continue é usada para ignorar o bloco atual e avançar para a próxima iteração, sem executar as instruções dentro do loop.
# Ele pode ser usado com loops while e for.
# Sua tarefa aqui é muito especial: você deve criar um comedor de vogal! Escreva um programa que use:
# - um loop for
# - o conceito de execução condicional (if-elif-else)
# - a declaração continue.
# Seu programa deve:
# 1. Peça ao usuário para inserir uma palavra;
# 2. Use user_word = user_word.upper() para converter em maiúsculas a palavra inserida pelo usuário;
# 3. Use execução condicional e a declaração continue para "consumir" as seguintes vogais A, E, I, O, U da palavra inserida;
# 4. Imprima as letras não consumidas na tela, cada uma delas em uma linha separada.

# Solicita que o usuário insira uma palavra e atribui à variável user_word
user_word = input("Insira uma palavra: ").upper()

# Itera por cada letra da palavra
for letter in user_word:
    # Se a letra for uma vogal, "consome" e continua para a próxima letra
    if letter in "AEIOU":
        continue
    # Se não for uma vogal, imprime a letra
    print(letter)