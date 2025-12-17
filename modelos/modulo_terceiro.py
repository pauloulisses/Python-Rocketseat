# ================================
# MÓDULOS DE TERCEIROS EM PYTHON
# ================================

# Módulos de terceiros são pacotes ou bibliotecas criados por outras pessoas
# Eles NÃO vêm instalados por padrão no Python

# Exemplo:
# pip install requests
# Instala a biblioteca Requests, usada para fazer requisições HTTP
# (GET, POST, PUT, DELETE) e consumir APIs em Python


# ================================
# O QUE É .venv
# ================================

# .venv é um ambiente virtual do Python
# Ele cria uma instalação isolada de bibliotecas só para este projeto
# Evita conflitos entre dependências de projetos diferentes


# ================================
# IMPORTAÇÃO DO MÓDULO
# ================================

print("\nImportação e uso de um módulo de terceiros")

# Importa toda a biblioteca requests
import requests


# ================================
# FAZENDO UMA REQUISIÇÃO HTTP
# ================================

# URL do site para o qual será feita a requisição
url = "https://www.google.com"

# Envia uma requisição HTTP do tipo GET para a URL
resposta = requests.get(url)

# ================================
# EXIBINDO O RESULTADO
# ================================

# status_code retorna o código HTTP da resposta
# 200 = sucesso
# 404 = não encontrado
# 500 = erro no servidor
print(f"Solicitação HTTP para {url} retornou o status {resposta.status_code}")
