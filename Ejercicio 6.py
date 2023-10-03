# Pedir al usuario que introduzca un entero positivo
n = int(input("Por favor, introduce un entero positivo: "))

# Verificar que n sea un entero positivo
if n <= 0:
    print("El número ingresado no es positivo.")
else:
    # Calcular la suma de los primeros n enteros positivos
    suma = n * (n + 1) // 2  # Usamos // para la división entera

    # Mostrar la suma en pantalla
    print(f"La suma de los primeros {n} enteros positivos es: {suma}")