# POO - (Programação Orientada a Objetos) é um paradigma que organiza o código em objetos, que combinam dados (atributos) e comportamentos (métodos).

# class - Uma classe é um modelo base que define as características (atributos) e as ações (métodos) que todos os objetos criados a partir dela terão; o objeto é a classe em uso, com valores reais.
# Atributos - Propriedades da class
# Metodos - As ações


# Classe Pessoa → modelo de um objeto Pessoa
class Pessoa:

    # __init__ → construtor (executa ao criar o objeto)
    # self → referência ao próprio objeto
    # -> None → não retorna valor

    def __init__(self, nome, idade) -> None:
        # Atributos - propriedades do objeto como nome e idade
        self.nome = nome   # atributo nome do objeto
        self.idade = idade # atributo idade do objeto

        # metodos - Ações do objeto
    def saudacao(self):
            return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos"

# objeto - É uma instância da class
# objeto
pessoa1 = Pessoa("Paulo", 33)
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa(nome="Chayenne", idade= 25)
mensagem = pessoa2.saudacao()
print(mensagem)

pessoa3 = Pessoa(nome="Lecy", idade=8)
mensagem = pessoa3.saudacao()
print(mensagem)