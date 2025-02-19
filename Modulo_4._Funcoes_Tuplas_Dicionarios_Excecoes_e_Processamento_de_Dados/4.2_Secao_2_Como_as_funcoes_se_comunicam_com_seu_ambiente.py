# Funções parametrizadas - Exemplo 4.2.1
# A função abaixo tem um parâmetro, que será usado para mostrar ao usuário um número.
def message(number):
    # A função imprime a mensagem com o número passado como argumento
    print("Digite um número:", number)

# Chamando a função com um valor para o parâmetro 'number'
message(1)  # Saída esperada: Digite um número: 1

# A variável 'number' fora da função não interfere com o parâmetro 'number' dentro da função (shadowing)
number = 1234
message(1)  # Saída esperada: Digite um número: 1
print(number)  # Saída esperada: 1234

# Função com dois parâmetros - Exemplo 4.2.2
# A função agora tem dois parâmetros: 'what' e 'number'
def message(what, number):
    # A função imprime uma mensagem usando os dois parâmetros
    print("Entrar", what, "número", number)

# Chamando a função com dois argumentos
message("telefone", 11)  # Saída esperada: Entrar telefone número 11
message("preço", 5)  # Saída esperada: Entrar preço número 5
message("número", "número")  # Saída esperada: Entrar número número número

# Função de passagem de parâmetros posicionais - Exemplo 4.2.3
# A função 'introduction' usa passagem posicional para os parâmetros 'first_name' e 'last_name'
def introduction(first_name, last_name):
    # A função imprime o nome completo usando os parâmetros
    print("Olá meu nome é", first_name, last_name)

# Chamando a função usando passagem posicional
introduction("Luke", "Skywalker")  # Saída esperada: Olá meu nome é Luke Skywalker
introduction("Jesse", "Quick")  # Saída esperada: Olá meu nome é Jesse Quick
introduction("Clark", "Kent")  # Saída esperada: Olá meu nome é Clark Kent

# Função usando passagem de parâmetros por palavra-chave - Exemplo 4.2.4
# Agora usamos parâmetros por palavra-chave, onde a ordem não importa
def introduction(first_name, last_name):
    # A função imprime o nome completo com base nos parâmetros fornecidos
    print("Olá meu nome é", first_name, last_name)

# Chamando a função usando passagem de palavra-chave
introduction(first_name="James", last_name="Bond")  # Saída esperada: Olá meu nome é James Bond
introduction(last_name="Skywalker", first_name="Luke")  # Saída esperada: Olá meu nome é Luke Skywalker

# Função com mistura de argumentos posicionais e de palavras-chave - Exemplo 4.2.5
# Função 'adding' que soma três números
def adding(a, b, c):
    # A função soma os três valores e imprime o resultado
    print(a, "+", b, "+", c, "=", a + b + c)

# Passagem de parâmetros posicionais
adding(1, 2, 3)  # Saída esperada: 1 + 2 + 3 = 6

# Passagem de parâmetros por palavra-chave
adding(c=1, a=2, b=3)  # Saída esperada: 2 + 3 + 1 = 6

# Mistura de ambos os estilos
adding(3, c=1, b=2)  # Saída esperada: 3 + 2 + 1 = 6

# Erro ao passar o mesmo parâmetro de forma posicional e por palavra-chave
# O código a seguir gerará erro:
# adding(3, a=1, b=2)  # TypeError: adding() got multiple values for argument 'a'

# Função com valores padrão para parâmetros - Exemplo 4.2.6
# A função 'introduction' tem valores padrão para os parâmetros 'first_name' e 'last_name'
def introduction(first_name="John", last_name="Smith"):
    # A função imprime o nome completo, usando valores padrão se os argumentos não forem fornecidos
    print("Olá meu nome é", first_name, last_name)

# Chamando a função sem argumentos, usando os valores padrão
introduction()  # Saída esperada: Olá meu nome é John Smith

# Chamando a função com um argumento de palavra-chave, o outro usa o valor padrão
introduction(last_name="Hopkins")  # Saída esperada: Olá meu nome é John Hopkins

# Chamando a função com todos os argumentos fornecidos
introduction(first_name="Henry")  # Saída esperada: Olá meu nome é Henry Smith