# Tuplas - Coleção ordenada e imutavél de elementos (imutáveis não pode mudar diferente da lista que pode)

# TUPLA USA-SE ( )
# LISTA USA-SE [ ]

# Criando uma tupla de exemplo:

minha_tupla = (1, 2, 2 , 3, 4)

print(f"Minha tupla: {minha_tupla}")

# Acessa Indices igual a lista
print(f"Minha tupla acessando inces: {minha_tupla[3]}")

# Acesando Indice do ultimo elemento da tuplas 
print(f"Minha tupla acessando último índice {minha_tupla[-1]}")


"""
Aqui irá da um erro pois a tupla é imutvel e não pode ser mudado nem um elemento

minha_tupla [0] = 7
print(minha_tupla)

"""

# Metodo count - (serve para mostra quantas vezes um elemento aparece na tupla)

contagem = minha_tupla.count(2)
print(f"Quantidade de vezes que o elemento 2 aparece  {contagem} vezes")

# passano o índice do elemento
indice = minha_tupla.index(1)
print(f"O elemento 1 da minha tupla está no índice {indice}")

