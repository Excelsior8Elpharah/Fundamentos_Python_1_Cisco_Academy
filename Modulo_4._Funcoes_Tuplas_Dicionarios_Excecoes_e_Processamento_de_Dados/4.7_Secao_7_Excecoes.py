# 1. Erros em Python
# Existem dois tipos principais de erros em Python:
# - Erros de sintaxe (SyntaxError)
# - Exceções (Errors que ocorrem em tempo de execução)

# Exemplo de erro de sintaxe (faltando aspas)
# print("Olá Mundo!)  # Isso geraria um SyntaxError

# Exemplo de exceção (divisão por zero)
# print(1/0)  # Isso geraria um ZeroDivisionError

# 2. Capturando exceções com try-except
while True:
    try:
        number = int(input("Insira um número inteiro: "))  # Tenta converter a entrada para int
        print(number / 2)  # Divide o número por 2
        break  # Se tudo der certo, sai do loop
    except:
        print("Aviso: o valor inserido não é um número válido. Tente novamente...")  
        # Se ocorrer um erro, avisa o usuário e pede outra entrada

# 3. Tratando múltiplas exceções
while True:
    try:
        number = int(input("Digite um número int: "))  # Entrada do usuário
        print(5 / number)  # Tentativa de divisão
        break  # Sai do loop se tudo der certo
    except ValueError:
        print("Valor errado.")  # Captura erro se a entrada não for um número
    except ZeroDivisionError:
        print("Desculpe. Não consigo dividir por zero.")  # Captura divisão por zero
    except:
        print("Eu não sei o que fazer...")  # Captura qualquer outro erro

# 4. Capturando múltiplas exceções na mesma cláusula
while True:
    try:
        number = int(input("Digite um número int: "))  # Entrada do usuário
        print(5 / number)  # Tentativa de divisão
        break  # Sai do loop se tudo der certo
    except (ValueError, ZeroDivisionError):
        print("Valor errado ou nenhuma divisão por zero permitida.")  
        # Captura erros de entrada inválida ou divisão por zero
    except:
        print("Desculpe, algo deu errado...")  # Captura qualquer outro erro

# 4.7.4 A exceção confirma a regra
try:
    value = int(input('Insira um número natural: '))
    print('O recíproco de', value, ' é', 1 / value)
except:
    print('Não sei o que fazer.')

# 4.7.5 Como lidar com mais de uma exceção
# Para tratar erros específicos, podemos definir exceções separadas para cada caso.
try:
    value = int(input('Digite um número natural: '))
    print('O recíproco de', value, ' é', 1 / value)
except ValueError:
    print('Eu não sei o que fazer.')
except ZeroDivisionError:
    print('A divisão por zero não é permitida em nosso Universo.')

# 4.7.6 A exceção padrão e como usá-la
try:
    value = int(input('Insira um número natural:'))
    print('O recíproco de', value, ' é', 1 / value)
except ValueError:
    print('Não sei o que fazer.')
except ZeroDivisionError:
    print('Divisão por zero não é permitida em nosso universo.')
except:
    print('Algo de estranho aconteceu aqui ... Desculpe!')

# 4.7.7 Algumas exceções úteis
# - ZeroDivisionError: Divisão por zero (/, //, %)
# - ValueError: Valor inaceitável para uma função (ex: int("abc"))
# - TypeError: Uso de tipo inadequado (ex: lista[0.5])
# - AttributeError: Acesso a um método inexistente em um objeto
# - SyntaxError: Erro de sintaxe no código

# 4.7.8 Por que testar seu código
# Testar códigos garante a qualidade e permite encontrar erros antes que cheguem ao usuário.
# Teste cada caminho de execução possível do seu programa.

# 4.7.9 Quando Python fecha os olhos
# Pequenos erros podem passar despercebidos em tempo de execução, como typos.
temperature = float(input('Digite a temperatura atual:'))
if temperature > 0:
    print("Acima de zero")
elif temperature < 0:
    prin("Abaixo de zero")  # Erro de digitação aqui (prin ao invés de print)
else:
    print("Zero")

print("Fim do programa. Código testado com sucesso!")