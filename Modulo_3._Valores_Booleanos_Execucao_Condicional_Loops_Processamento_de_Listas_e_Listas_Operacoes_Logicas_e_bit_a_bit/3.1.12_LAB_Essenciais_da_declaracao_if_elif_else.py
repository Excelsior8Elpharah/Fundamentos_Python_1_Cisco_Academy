# Solicitando o ano do usuário
year = int(input("Digite um ano: "))

# Verificando se o ano está dentro do período do calendário gregoriano
if year < 1582:
    print("Não dentro do período do calendário gregoriano")
else:
    # Verificando as condições para um ano bissexto ou comum
    if year % 4 != 0:
        print("Ano comum")
    elif year % 100 != 0:
        print("Ano bissexto")
    elif year % 400 != 0:
        print("Ano comum")
    else:
        print("Ano bissexto")