# LOOP WHILE (ENQUANTO) - É TIPO DE LOOP UTILIZADO PARA REPETIR UM BLOCO DE CÓDIGO ENQUANTO UMA CONDIÇÃO FOR VERDADEIRA

# inicia-se em 0 a contagem 
contador = 0
# enquanto contador for menor que 5
while contador < 5:
    print(f"Contagem: {contador}")
    contador += 1
    # incrementa 1 em cada numero do contador

print("-------------------------------------------------")

# usando o brak

contador2 = 0
while contador2 < 10:
    contador2 += 1
    if contador2 == 3:
        break
    print(f"Contador {contador2}")


