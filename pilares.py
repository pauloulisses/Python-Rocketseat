# Pilares

# Herança
print("\nExemplo de Herança:")
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome
    def andar(self):
        print(f"O animal {self.nome} andou")
        return
    
    def emitir_som(self):
        pass    


# Hernaça - class cahorro herda tudo da class Animal
class Animals(Animal):  # herança
       def emitir_som(self): # polimorfismo
            return "Au, au" # polimorfismo
       

       
# Herdando tudo da class anaiml      
class Gato(Animal):
     def emitir_som(self):
          return "Miau!" 
     


 # Herda tudo da class animal    
class Galinha(Animal):
     def emitir_som(self):
          return "Coroquico"     
     

     
# POLIMORFISMO
# Permite que classes filhas usem o mesmo método da classe mãe,
# mas com comportamentos diferentes.
# Ex: todas usam emitir_som(), cada uma faz de um jeito.
# EX: class mae Animals, clss filhas Gato que reutilizar emitir som da class mae so que comportamento diferente


class Lobo(Animal):  # classe Lobo herda da classe Animal
    def emitir_som(self):  # sobrescreve o método emitir_som
        return "Auuu"  # POLIMORFISMO: mesmo método, comportamento diferente
