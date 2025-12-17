# LISTA - É uma coleção de elementos ordenáveis e mutáveis.
# ordenáveis = possuem uma ordem definida (índices)
# mutáveis   = permitem alterar, adicionar e remover valores

# LISTA USA-SE [ ]
# TUPLA USA-SE ( )

# Exibindo a lista
minha_lista = [1,2,3,4,5, "Rocketseat", True, False]

print(F"Minha lista de exeplo: {minha_lista}")

# Exibindo índice da lista
print(f"Meu elemento 3 da lista é: {minha_lista[3]}")

# Fatiamento da lista
print(f"Minha lista fatiada do elemento 1 ao elemento 6: {minha_lista[1:6]}")

# Exibe os elementos da lista do índice 0 até o 5
# (o 6 não é incluído — o Python para um antes)
print(f"Minha lista exibindo do indice 0 ao 5 {minha_lista[:6]}")

