# Pedir al usuario dos números enteros
n = int(input("Por favor, introduce el primer número entero (n): "))
m = int(input("Por favor, introduce el segundo número entero (m): "))

# Calcular el cociente y el resto de la división entera
c = n // m
r = n % m

# Mostrar los resultados en pantalla
print(f"{n} entre {m} da un cociente de {c} y un resto de {r}")