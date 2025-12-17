#Módulos são arquivos que contêm código reutilizável (funções, classes e variáveis) para organizar e reaproveitar funcionalidades em Python.

# tem que importar só oque for usar expecifico  pq importando tudo pode da problema no sistema
print("EXEMPLO DE IMPOTAÇÃO DE MÓDULO PADRÃO")

# Aqui importa tudo
import math

# Aqui  importa só oque for utilizar
from math import sqrt


raiz_quadrada = math.sqrt(25)
print(f"A raiz quadrada de 25 é {raiz_quadrada}")


print("\n Exwplo de criação e utilização de um módulo personalizado ")

# importando o arquivo modulo
import meu_modulo

# importação especifica
from meu_modulo import saudacao, dobro


# Acessando as funções do arquivo meu_modulo
menssagem = meu_modulo.saudacao("Paulo")
resultado_dobro = meu_modulo.dobro(5)
print(menssagem)
print(f"O dobro de 5 é {resultado_dobro}")
