# Function - é um bloco de código reutilizavél

def saudacao(nome, idade, sexo):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo: ")
    print(f"Olá, seu nome é {nome}, sua idade é {idade} anos, e você é do sexo {sexo}")

saudacao("nome", "idade", "sexo")




# Function com retorno

def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("\n Chamando função quadrado:")

resultado_quadrado = quadrado(5)
print(f"Resultado da function quadradol: {resultado_quadrado}")




# Function com multiplos paramentros
def soma(numero1, numero2):
   resultado = numero1 + numero2 / 10
   return resultado 
print("\n Chamando a função soma:")
resultado_soma = soma(20, 50)
print(f"A soma do numero 20 e numero 50 é {resultado_soma}")