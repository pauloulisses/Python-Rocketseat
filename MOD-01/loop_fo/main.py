# É UMA ESTRUTURA QUE PERMITI A GENTE REPETIR UM BLOCO DE CÓDIGO EQUANTO UMA CONDIÇÃO FOR VERDADEIRA
# O for serve para repetir um código para cada item de uma lista, intervalo ou sequência.

# for com uma lista - [lista]

lista = [1, 2, 3, 4, 5]
# in - dentro
for elemento in lista:
    print(f"Os elementos da lista com loop for é {elemento}")

print("----------------------------------------------------------------------------")

# for com uma tupla - (tupla)

tupla = (6, 7, 8, 9, 10)
for elementos in tupla:
    print(f"Os elementos da tupla com loop for é: {elementos}")


# for com um dicionario - {dicionário}

dicionario = {"nome": "João", "idade":30, "cidade":"São Paulo"}
for elements in dicionario.keys(): # Mostra todas as CHAVES do dicionário.
    print(f"OS elementos do dicionário com loop for é: {dicionario}")

# Mostra todos os VALORES do dicionário.
for valor in dicionario.values():
    print(f"O valor doe elemntos do dicionario com o loop for é: {valor}")


# Mostra chaves e valor do dicionário
for chaves, valor in dicionario.items():
    print(f"AS CHAVES E VALORES SAÃO: {chaves}, {valor}") 


# TRUQUES COM LOOP FOR E RANGE()- intervalo de númerico 
# [0,1,2,3,4,5,6,7,8,9]

# range() cria uma sequência de números para você repetir algo várias vezes.
for numero in range(10):
    print(f"Número: {numero}")


# len() mostra o tamanho: quantos elementos, caracteres ou itens tem.
lista2 = [1, 2, 3, 4, 5]
for indice in range(0, len(lista2)):
    print(f"Indice: {indice}")
