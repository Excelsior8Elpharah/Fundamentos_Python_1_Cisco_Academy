# 4.5.2 Funções de exemplo: triângulos
# Vamos jogar com triângulos agora. Vamos começar com uma função para verificar se três lados de determinados comprimentos podem construir um triângulo.
# Sabemos pela escola que a soma de dois lados arbitrários precisa ser maior que o terceiro lado.
# Não será um desafio difícil. A função terá três parâmetros - um para cada lado.
# Ele retornará True se os lados puderem construir um triângulo, e False caso contrário. Nesse caso, is_a_triangle é um bom nome para essa função.

# Função para verificar se os lados podem formar um triângulo
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

# Teste para verificar se os lados formam um triângulo
print(is_a_triangle(1, 1, 1))  # Esperado: True
print(is_a_triangle(1, 1, 3))  # Esperado: False

# Agora, vamos tentar garantir que um triângulo seja um triângulo de ângulo reto usando o teorema de Pitágoras
# O teorema de Pitágoras diz que: c² = a² + b² (onde c é a hipotenusa)

# Função para verificar se o triângulo é de ângulo reto
def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    return False

# Testes para verificar se o triângulo é de ângulo reto
print(is_a_right_triangle(5, 3, 4))  # Esperado: True
print(is_a_right_triangle(1, 3, 4))  # Esperado: False

# Avaliando a área de um triângulo usando a fórmula de Heron
# A fórmula de Heron é: A = √(p * (p - a) * (p - b) * (p - c)), onde p é o semiperímetro: p = (a + b + c) / 2

# Função auxiliar para calcular a área do triângulo com a fórmula de Heron
def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

# Função para calcular a área do triângulo
def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)

# Teste para calcular a área de um triângulo com lados 1, 1 e √2 (triângulo retângulo)
print(area_of_triangle(1., 1., 2. ** 0.5))  # Esperado: 0.5

# Como esperado, o resultado não é exatamente 0.5 devido à precisão da representação numérica em ponto flutuante