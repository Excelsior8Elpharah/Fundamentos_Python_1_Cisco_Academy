# Criando um dicionário com pares chave-valor
my_dict = {
    "nome": "Raphael",
    "idade": 25,
    "cidade": "São Paulo",
    "profissão": "Analista de TI"
}

# Acessando valores por chave
print(my_dict["nome"])  # Saída: Raphael
print(my_dict.get("idade"))  # Saída: 25

# Adicionando um novo par chave-valor ao dicionário
my_dict["empresa"] = "Tech Solutions"
print(my_dict)  
# Saída: {'nome': 'Raphael', 'idade': 25, 'cidade': 'São Paulo', 'profissão': 'Analista de TI', 'empresa': 'Tech Solutions'}

# Modificando o valor de uma chave existente
my_dict["cidade"] = "Taboão da Serra"
print(my_dict["cidade"])  # Saída: Taboão da Serra

# Removendo um item do dicionário usando 'del'
del my_dict["profissão"]
print(my_dict)  
# Saída: {'nome': 'Raphael', 'idade': 25, 'cidade': 'Taboão da Serra', 'empresa': 'Tech Solutions'}

# Removendo um item do dicionário usando 'pop()' e armazenando o valor removido
idade = my_dict.pop("idade")
print(idade)  # Saída: 25
print(my_dict)  
# Saída: {'nome': 'Raphael', 'cidade': 'Taboão da Serra', 'empresa': 'Tech Solutions'}

# Verificando se uma chave existe no dicionário usando 'in'
print("empresa" in my_dict)  # Saída: True
print("salário" in my_dict)  # Saída: False

# Iterando sobre as chaves do dicionário
for key in my_dict:
    print(key, "->", my_dict[key])
# Saída:
# nome -> Raphael
# cidade -> Taboão da Serra
# empresa -> Tech Solutions

# Iterando sobre as chaves e valores do dicionário usando 'items()'
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Saída:
# nome: Raphael
# cidade: Taboão da Serra
# empresa: Tech Solutions

# Copiando um dicionário usando 'copy()'
copy_dict = my_dict.copy()
print(copy_dict)  
# Saída: {'nome': 'Raphael', 'cidade': 'Taboão da Serra', 'empresa': 'Tech Solutions'}

# Limpando um dicionário, removendo todos os itens com 'clear()'
copy_dict.clear()
print(copy_dict)  # Saída: {}

# Deletando um dicionário completamente usando 'del'
del copy_dict
# print(copy_dict)  # Isso causaria um NameError, pois copy_dict foi deletado