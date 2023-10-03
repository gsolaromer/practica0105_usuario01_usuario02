# Pedir al usuario la cantidad a invertir, la tasa de interés anual y el número de años

cantidad_invertir = float(input("Por favor, introduce la cantidad a invertir: "))

tasa_interes_anual = float(input("Por favor, introduce la tasa de interés anual (en porcentaje): "))

num_años = int(input("Por favor, introduce el número de años de la inversión: "))

# Calcular el capital obtenido en la inversión
tasa_interes_decimal = tasa_interes_anual / 100  # Convertir la tasa de interés a decimal
capital_obtenido = cantidad_invertir * (1 + tasa_interes_decimal) ** num_años

# Mostrar el capital obtenido en pantalla
print(f"El capital obtenido en la inversión es: {capital_obtenido:.2f}")