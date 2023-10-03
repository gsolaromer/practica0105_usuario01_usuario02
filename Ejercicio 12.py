# Precio habitual de una barra de pan
precio_habitual = 3.49  # en euros

# Pedir al usuario el número de barras vendidas que no son del día
barras_vendidas = int(input("Por favor, introduce el número de barras vendidas que no son del día: "))

# Calcular el descuento del 60% por no ser fresca
descuento = precio_habitual * 0.60

# Calcular el precio de una barra no fresca
precio_no_fresca = precio_habitual - descuento

# Calcular la ganancia total
ganancia_total = barras_vendidas * precio_no_fresca

# Mostrar los resultados
print(f"Precio habitual de una barra de pan: {precio_habitual:.2f} euros")
print(f"Descuento por no ser fresca: {descuento:.2f} euros")
print(f"Ganancia final total: {ganancia_total:.2f} euros")