# Cenário
# Um jovem mágico escolheu um número secreto. Ele o ocultou em uma variável chamada secret_number.
# Ele quer que todos que executam seu programa joguem o jogo Adivinhe o número secreto e adivinhem qual número ele escolheu para eles.
# Quem não adivinhar o número ficará para sempre em um loop infinito! Infelizmente, ele não sabe como completar o código.

secret_number = 777  # O número secreto escolhido pelo mágico

# Exibe o texto de boas-vindas para o jogo
print(
"""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+
""")

# O loop continuará até que o usuário adivinhe corretamente
while True:
    # Solicita ao usuário que insira um número
    user_guess = int(input("Qual é o número secreto? "))
    
    # Verifica se o número inserido pelo usuário é o número secreto
    if user_guess == secret_number:
        print("Muito bem, trouxa! Você está livre agora.")
        break  # Sai do loop se o número estiver correto
    else:
        print("Ha ha! Você está preso no meu loop!")  # Se o número não for correto, avisa o usuário
