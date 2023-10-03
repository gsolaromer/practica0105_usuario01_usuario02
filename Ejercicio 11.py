# Pedir al usuario la cantidad de dinero depositada en la cuenta de ahorros

cantidad_inicial = float(input("Por favor, introduce la cantidad de dinero depositada: "))

# Tasa de interés anual

tasa_interes_anual = 0.04  # 4% de interés

# Calcular los ahorros después del primer año

ahorros_despues_del_primer_año = cantidad_inicial * (1 + tasa_interes_anual)

# Calcular los ahorros después del segundo año

ahorros_despues_del_segundo_año = ahorros_despues_del_primer_año * (1 + tasa_interes_anual)

# Calcular los ahorros después del tercer año

ahorros_despues_del_tercer_año = ahorros_despues_del_segundo_año * (1 + tasa_interes_anual)

# Mostrar los ahorros después de cada año, redondeados a dos decimales

print(f"Ahorros después del primer año: {ahorros_despues_del_primer_año:.2f}")

print(f"Ahorros después del segundo año: {ahorros_despues_del_segundo_año:.2f}")

print(f"Ahorros después del tercer año: {ahorros_despues_del_tercer_año:.2f}")