# método upper()
nome = "Paulo Ulisses"

print(nome.upper())  
# Converte toda a string para MAIÚSCULO
# IMPORTANTE: strings são IMUTÁVEIS, então 'nome' não muda, só retorna a nova versão

print(nome.lower())  
# Converte toda a string para minúsculo
# Também não altera a string original (imutável)

print(nome.count("s", 1, 6))  
# Conta quantas vezes a letra "s" aparece ENTRE as posições 1 e 6
# OBS: o índice final (6) NÃO é incluído na contagem

print(nome.find("u"))  
# Retorna o índice onde encontra a letra "u"
# Se NÃO encontrar, retorna -1

print(nome.encode())  
# Codifica a string para bytes usando UTF-8 (padrão)
# Exemplo de saída: b'Paulo Ulisses'

print(nome.encode().decode())  
# Primeiro codifica para bytes
# Depois decodifica de volta para string normal
# Ou seja, retorna exatamente: 'Paulo Ulisses'

print(nome.replace("s", "123"))  
# Substitui todas as ocorrências de "s" por "123"
# Exemplo de resultado: "Paulo Uli123123e123"

print("-".join("paulo"))
# Junta cada caractere da string "paulo" usando "-" entre eles
# Resultado: p-a-u-l-o

print(nome.split(" "))
# Divide a string em uma lista, separando pelos espaços
# Exemplo: ["Paulo", "Ulisses"]

print(nome.strip("P"))
# Remove o caractere "P" apenas do INÍCIO e/ou do FINAL da string
# NÃO remove caracteres do meio da palavra
# Exemplo: "Paulo Ulisses" → "aulo Ulisses"
# (porque só havia "P" no começo)

print(nome.rstrip())
# Remove ESPAÇOS em branco somente do FINAL da string
# Não remove nada do início
# Exemplo: "Paulo Ulisses   " → "Paulo Ulisses"

# comparadores
print(nome.startswith("Pa"))
# Verifica se a string COMEÇA exatamente com "Pa"
# Retorna True ou False
# Exemplo: "Paulo Ulisses" → começa com "Pa" → resultado: True

print("Pa" in nome)
# Verifica se "Pa" está CONTIDO em qualquer lugar da string
# Retorna True ou False
# Exemplo: "Paulo Ulisses" contém "Pa" → resultado: True

print("ss" not in nome)
# Verifica se "EBE" NÃO está contido na string
# Retorna True se NÃO existir, e False se existir
# Exemplo: "EBE" não aparece em "Paulo Ulisses" → resultado: True
