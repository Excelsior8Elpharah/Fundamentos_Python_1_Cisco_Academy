# Definição da função 'message'
# A função exibe a mensagem solicitando a entrada do usuário
def message():
    print("Por favor, insira um valor: ")

# Início do código principal
print("Começamos aqui.")

# Chamada da função message, que exibe a mensagem de entrada
message()
# Lê o primeiro valor do usuário
a = int(input())  

# Chamada da função message novamente
message()
# Lê o segundo valor do usuário
b = int(input())  

# Chamada da função message novamente
message()
# Lê o terceiro valor do usuário
c = int(input())  

# Exibindo os valores inseridos
print("Você inseriu os valores:", a, b, "e", c)

# Explicações:
# 1. **Definição da função 'message()'**:
#    - A função é definida no início e simplesmente imprime a mensagem "Por favor, insira um valor: ".
# 2. **Chamada da função 'message()'**:
#    - Cada vez que a função é chamada, ela imprime a mensagem pedindo a entrada do usuário.
# 3. **Entrada do usuário**:
#    - Após cada chamada da função, o código usa a função input() para ler um valor do usuário e converte esse valor para um inteiro (int).
# 4. **Exibição dos valores**:
#    - Depois que os três valores são inseridos, o programa exibe os valores inseridos.
# 5. **Observações**:
#    - **Função 'message()'**: Você pode alterar a mensagem de solicitação de entrada de forma centralizada, editando apenas dentro da função. Isso facilita a manutenção.
#    - **Cuidado com a ordem de definição das funções**: A função precisa ser definida antes de ser chamada. Caso contrário, o Python não a reconhecerá.
#    - **Evite reusar o nome de funções como variáveis**: Atribuir um valor a 'message' após sua definição faria com que a função fosse sobrescrita e não pudesse ser chamada corretamente.
