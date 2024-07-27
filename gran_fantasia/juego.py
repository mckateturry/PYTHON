import random
from personaje import Personaje

    # BIENVENIDO
def jugar():
    print("¡Bienvenido al juego Gran Fantasía!")
    print("Los personajes disponibles son: Akemi, Radka, Thor, Sakura")
    nombre_jugador = input("Por favor, selecciona el nombre de tu personaje: ").capitalize()

    # CREAR EL PERSONAJE DEL JUGADOR
    if nombre_jugador in ["Akemi", "Radka", "Thor", "Sakura"]:
        jugador = Personaje(nombre_jugador)
    else:
        print("Nombre de personaje no válido.")
        return

    print("Estado de tu personaje:")
    print(jugador.obtener_estado())

    # CREAR A ORCO
    orco = Personaje("Orco")

    probabilidad = jugador.probabilidad_ganar(orco)

    # Informar al jugador sobre la aparición del orco
    opcion = Personaje.enfrentar_orco(probabilidad)

    while opcion == 1:
        resultado = random.uniform(0, 1)
        if resultado <= probabilidad:
            print("¡Has ganado el ataque!")
            jugador.asignar_experiencia(50)
            orco.asignar_experiencia(-30)
        else:
            print("Has perdido el ataque...")
            jugador.asignar_experiencia(-30)
            orco.asignar_experiencia(50)

        print("Estado actualizado de tu personaje:")
        print(jugador.obtener_estado())
        print("Estado actualizado del orco:")
        print(orco.obtener_estado())

        # Calcular la nueva probabilidad de ganar del jugador contra el orco
        probabilidad = jugador.probabilidad_ganar(orco)

        # Consultar al jugador si desea atacar nuevamente o huir
        opcion = Personaje.enfrentar_orco(probabilidad)

    print("Has decidido huir. El orco ha quedado atrás.")

# Ejecutar el juego
if __name__ == "__main__":
    jugar()
