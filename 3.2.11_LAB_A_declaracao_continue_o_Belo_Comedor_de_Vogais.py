# Cenário
# Sua tarefa aqui é ainda mais especial do que antes: você deve reprojetar o (feio) comedor de vogal do laboratório anterior e criar um melhor (bonito) comedor de vogal!
# Escreva um programa que use:
# - um loop for
# - o conceito de execução condicional (if-elif-else)
# - a declaração continue.
# Seu programa deve:
# 1. Peça ao usuário para inserir uma palavra;
# 2. Use user_word = user_word.upper() para converter em maiúsculas a palavra inserida pelo usuário;
# 3. Use execução condicional e a declaração continue para "consumir" as seguintes vogais A, E, I, O, U da palavra inserida;
# 4. Atribua as letras não consumidas à variável word_without_vowels e imprima a variável na tela.

# Solicitar ao usuário que digite uma palavra e atribua-a à variável user_word
user_word = input("Insira uma palavra: ").upper()

# Inicializa a variável word_without_vowels como uma string vazia
word_without_vowels = ""

# Itera sobre cada letra da palavra
for letter in user_word:
    # Se a letra for uma vogal, "consome" e continua para a próxima letra
    if letter in "AEIOU":
        continue
    # Se não for uma vogal, adiciona a letra em word_without_vowels
    word_without_vowels += letter

# Imprime a palavra sem as vogais
print(word_without_vowels)