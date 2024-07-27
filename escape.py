import math

radio_km = float(input("Ingrese el radio del planeta en kilómetros: "))

radio_m = radio_km * 1000

# En m/s²
g = float(input("Ingrese la constante gravitacional g (en m/s²): "))

# Aquí la velocidad de escape 
velocidad_escape = math.sqrt(2 * g * radio_m)

# imprimir, :.1f= formato decimal
print(f"La velocidad de escape es {velocidad_escape:.1f} m/s")
