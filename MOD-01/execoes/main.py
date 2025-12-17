print("Exemplo de captura de execções")
try:
    numero = int(input("Digite um número inteiro: "))
    resultado = 10 / numero
except Exception as e:
    print(f"Erro: {e}")