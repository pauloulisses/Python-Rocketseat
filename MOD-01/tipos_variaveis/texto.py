# DECLARAÇÃO

nome_completo = "Paulo Eberson Ulisses"

nome_completo_aspas = """"Paulo
Eberson
"""

nome_compelto_barra = "Paulo \
    Eberson"

nome = "Paulo"
sobrenome = "Eberson"


# Formatação

print("Nome completo (1a forma): ", nome_completo) # com a virgula para fazer essa concatenação tem o espaço altomatico
print("Nome completo (2a forma): " + nome_completo) # com + a concatenação não tem o espaço
print("Nome completo (3a forma):" + "Paulo" + " " +  "Ulisses")
print("Nome completo (4a forma):" + "Paulo", "Ulisses")
print("Nome completo (5a forma): ", nome_completo_aspas)
print("Nome completo (6a forma): ", nome_compelto_barra)
print("Nome completo (7a forma):%s" % nome_completo)
print("Nome completo (8a forma):%s %s" % (nome, sobrenome))
print("Nome completo (9a forma): {} {}".format(nome, sobrenome))

# Forma mais utilizada pela comuniodade
print(f"Nome completo (10a forma): {nome} {sobrenome}")