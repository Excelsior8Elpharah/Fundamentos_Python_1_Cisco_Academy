# 4.3.8   LAB   Convertendo o consumo de combustível
# O consumo de combustível de um carro pode ser expresso de várias maneiras diferentes. 
# Por exemplo, na Europa, ele é mostrado como a quantidade de combustível consumida por 100 quilômetros.
#
# Nos EUA, é mostrado como o número de quilômetros percorridos por um carro usando um litro de combustível.
#
# Sua tarefa é escrever um par de funções convertendo l/100 km em mpg e vice-versa.
#
# As funções:
# - são nomeados liters_100km_to_miles_gallon e miles_gallon_to_liters_100km respectivamente;
# - use um argumento (o valor correspondente aos nomes)
# Preencha o código no editor e execute-o para verificar se a sua saída é igual à nossa.
#
# Aqui estão algumas informações para ajudá-lo:
#
# 1 milha americana = 1609.344 metros;
# 1 galão americano = 3,785411784 litros.

# Função que converte de litros por 100 km para milhas por galão
def liters_100km_to_miles_gallon(litres):
    gallons = litres / 3.785411784  # Converte litros para galões
    miles = 100 * 1000 / 1609.344  # Converte 100 km para milhas
    return miles / gallons  # Retorna o valor em milhas por galão

# Função que converte de milhas por galão para litros por 100 km
def miles_gallon_to_liters_100km(miles):
    km100 = miles * 1609.344 / 1000 / 100  # Converte milhas por galão para km por 100 km
    litres = 3.785411784  # Valor de um galão em litros
    return litres / km100  # Retorna o valor em litros por 100 km

# Testes para a conversão de consumo de combustível
print(liters_100km_to_miles_gallon(3.9))  # Exemplo com 3.9 litros por 100 km
print(liters_100km_to_miles_gallon(7.5))  # Exemplo com 7.5 litros por 100 km
print(liters_100km_to_miles_gallon(10.))  # Exemplo com 10 litros por 100 km
print(miles_gallon_to_liters_100km(60.3))  # Exemplo com 60.3 milhas por galão
print(miles_gallon_to_liters_100km(31.4))  # Exemplo com 31.4 milhas por galão
print(miles_gallon_to_liters_100km(23.5))  # Exemplo com 23.5 milhas por galão