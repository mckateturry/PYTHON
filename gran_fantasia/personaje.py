# Cada personaje tiene un nombre, el cual debe ser especificado al momento de crear
#  un personaje.
class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

# Cada personaje recién creado tiene nivel 1 y experiencia 0 (estos son los únicos
#  valores posibles al momento de crear un personaje).
    def obtener_estado(self):
        """Muestra el estado actual del personaje"""
        return f"Nombre: {self.nombre}, Nivel: {self.nivel}, Experiencia: {self.experiencia}"

#  Los valores posibles de experiencia son entre 0 y 99 inclusive.
#  ○ El nivel mínimo es 1 y no hay máximo.
#  ○ Cada 100 puntos de experiencia recibidos, el personaje sube 1 nivel (su nivel
#  aumenta en 1).
    def asignar_experiencia(self, experiencia_recibida):
        """Asignar experiencia al personaje y actualizar su nivel"""
        experiencia_total = self.experiencia + experiencia_recibida

        while experiencia_total >= 100:
            self.nivel += 1
            experiencia_total -= 100
        
        while experiencia_total < 0:
            if self.nivel > 1:
                self.nivel -= 1
                experiencia_total += 100
            else:
                experiencia_total = 0
                break

        self.experiencia = experiencia_total

    def __lt__(self, otro):
        """Compara si el personaje actual es menor que otro personaje basado en el nivel"""
        return self.nivel < otro.nivel

    def __gt__(self, otro):
        """Compara si el personaje actual es mayor que otro personaje basado en el nivel"""
        return self.nivel > otro.nivel

    def probabilidad_ganar(self, otro):
        """Calcula la probabilidad de ganar del personaje actual contra otro personaje"""
        if self > otro:
            return 0.66
        elif self < otro:
            return 0.33
        else:
            return 0.50

    @staticmethod
    def enfrentar_orco(probabilidad):
        """Muestra el diálogo del enfrentamiento al orco y retorna la opción del jugador"""
        print(f"Ha aparecido un orco. Tienes una probabilidad de {int(probabilidad * 100)}% de ganarle.")
        print("En caso de ganar, recibirás 50 puntos de experiencia y el orco perderá 30.")
        print("En caso de perder, perderás 30 puntos de experiencia mientras que el orco ganará 50.")
        opcion = int(input("¿Deseas atacar (1) o huir (2)? "))
        return opcion
