# Paso 1: Solicitar al usuario que ingrese el radio del círculo.

import math


radio = float(input("Por favor, ingrese el radio del círculo: "))

# Paso 2: Calcular el área del círculo utilizando la fórmula área = π * radio^2

area = math.pi * (radio**2)


# Paso 3: Mostrar al usuario el área calculada 

print("El área del círculo con radio", radio, "es:", area)