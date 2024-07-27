#importar las listas de ingredientes.py NO OLVIDAR
from ingredientes import carnicos_posibles, vegetales_posibles, masas_posibles

class Pizza:
    def __init__(self):
        self.proteico = None
        self.vegetal1 = None
        self.vegetal2 = None
        self.masa = None
        self.es_valida = False

    # Método de clase 
    @classmethod
    def validar_elemento(cls, elemento, lista_posibles):
        return elemento in lista_posibles

  
    def realizar_pedido(self):
        self.proteico = input("Ingrese el ingrediente proteico: ")
        self.vegetal1 = input("Ingrese el primer ingrediente vegetal: ")
        self.vegetal2 = input("Ingrese el segundo ingrediente vegetal: ")
        self.masa = input("Ingrese el tipo de masa: ")

        # Validación
        proteico_valido = self.validar_elemento(self.proteico, carnicos_posibles)
        vegetal1_valido = self.validar_elemento(self.vegetal1, vegetales_posibles)
        vegetal2_valido = self.validar_elemento(self.vegetal2, vegetales_posibles)
        masa_valida = self.validar_elemento(self.masa, masas_posibles)

        if proteico_valido and vegetal1_valido and vegetal2_valido and masa_valida:
            self.es_valida = True
        else:
            self.es_valida = False

#INSTANCIA
pizza = Pizza()
pizza.realizar_pedido()
if pizza.es_valida:
    print("La pizza es válida y su precio es $10.000.")
else:
    print("La pizza no es válida. Verifique los ingredientes y el tipo de masa.")
