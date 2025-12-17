# CONDICIONAIS - if, elif, else

# IF = SE
# ELIF = SENÃOSE
# ELSE = SENÃO

# exeplo de if

idade = 18
print("Exemplo de comando if")
if idade >= 18: # se idade for maior ou igual
    print("Você é maior de idade.")

if idade == 19: # se idade for igaul a 
    print("Você tem 19 anos")

if idade <= 18: # se idade for menor ou igaual a 
    print("Você é menor de idade")

if idade != 10: # idade é diferente
    print("Você não tem 10 anos")

# usando elif

idade2 = int(input("Digite sua idade: "))
if idade2 == 18:
    print("Você é maior de idade")
elif idade2 >= 19 and idade2 <= 29:
    print("Você tem 19 anos ou mais")
elif idade2 >= 30 and idade2 <= 39:
    print("Você tem 30 anos ou mais")
else:
    print("Você tem 40 anos ou mais")
