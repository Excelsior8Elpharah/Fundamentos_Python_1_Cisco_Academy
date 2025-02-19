# Cenário
# A declaração break é usada para sair/encerrar um loop.
# Projete um programa que use um loop while e solicite continuamente que o usuário insira uma palavra,
# a menos que o usuário insira "chupacabra" como a palavra de saída secreta, caso em que a mensagem 
# "Você saiu do loop com sucesso" deve ser impressa na tela, e o loop deve terminar.
# Não imprima nenhuma das palavras inseridas pelo usuário. Use o conceito de execução condicional e a declaração break.

while True:
    user_input = input("Insira uma palavra: ")  # Solicita ao usuário que insira uma palavra
    
    if user_input == "chupacabra":  # Verifica se a palavra inserida é a palavra secreta
        print("Você saiu do loop com sucesso.")
        break  # Encerra o loop se a palavra secreta for inserida