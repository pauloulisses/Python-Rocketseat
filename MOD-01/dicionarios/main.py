# Dicionários - Coleção não ordenada de pares chave e valor

pessoa = {"nome": "Paulo", "idade": 33, "cidade": "Exu-PE"}
print(f"Meu dicionário de pessoa: {pessoa}")

# Acessando valores por chaves
print(f"Nome: {pessoa['nome']}")

# Acessando todos os valores - recomendado pela comunidade
print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Cidade: {pessoa['cidade']}")

# Acessando todos os valores (transformando em lista)
print(list(pessoa.values()))

# Adicionando um valor ao dicionário
pessoa["Sobrenome"] = "Ulisses"
print(f"Adicionando o sobrenome ao meu dicionário: {pessoa['Sobrenome']}")

# Atualizando um valor existente
pessoa["idade"] = 31
print(f"Idade atualizada: {pessoa['idade']}")

# Removendo um par chave-valor
del pessoa["nome"]     # remove a chave "nome"
print(f"Meu dicionário depois da remoção: {pessoa}")

# Métodos keys(), values(), items()

# keys() - Retorna apenas as CHAVES do dicionário
chaves = pessoa.keys()
print(f"Chaves do dicionário: {chaves}")

# values() - Retorna apenas os VALORES do dicionário
valores = pessoa.values()
print(f"Valores do dicionário: {valores}")

# items() - Retorna pares (CHAVE, VALOR) como tuplas
itens = pessoa.items()
print(f"Pares chave-valor do dicionário: {itens}")

# Convertendo items() em lista para acessar individualmente
itens2 = list(pessoa.items())
print(f"Acessando o primeiro item (valor): {itens2[0][1]}")

# Acessando cada elemento individualmente como se fosse uma lista

# Transforma as chaves do dicionário em uma lista
chaves2 = list(pessoa.keys())

# Acessando a primeira chave da lista de chaves
print(f"A primeira chave do meu dicionário é: {chaves2[0]}")

