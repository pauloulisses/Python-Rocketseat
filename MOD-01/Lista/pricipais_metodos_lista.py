# Adicionando (na verdade substituindo) um elemento na lista

minha_lista = [1, 2, 3, 4, 5, "Lista", True, False]

# Substitui o valor do índice 0 (que era 1) por "Python"
minha_lista[0] = "Python"

# Exibe a lista atualizada
print(minha_lista)


# Metodos de listas 

# metodos append() - adiciona um elemento ao final da lista

minha_lista.append("JAVA")
print(f"Após append(python): {minha_lista}")


# Método index

# Procura pelo valor 6 dentro da lista e retorna o índice onde ele está.
# OBS: Se o valor não existir na lista, o Python gera um erro.
indice = minha_lista.index(4)

# Exibe o índice encontrado
print(f"Índice do elemento 4: {indice}")

# Metodo insert: Insere um elemento em um indice especifico
minha_lista.insert(2, 10)
print(f"Após o insert(2,10) {minha_lista}")

# Metodo pop - só aceita indice numerico
elemento_removido = minha_lista.pop(1)
print(f"Elemento removido: {minha_lista}")


# Metodo remove
minha_lista.remove(True)
print(f"Após remover True{minha_lista}")



# Método sort - Organiza a lista em ordem crescente

# IMPORTANTE:
# A lista só pode ser organizada se todos os elementos forem do MESMO tipo.
# Exemplo: só números, ou só strings. Se misturar (int, str, bool), dá erro.

minha_lista.sort()  # Ordena a lista em ordem crescente

print(f"Organizando a lista com método sort: {minha_lista}")
