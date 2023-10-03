# Peso de un payaso y una muñeca en gramos
peso_payaso = 112
peso_muñeca = 75

# Pedir al usuario el número de payasos y muñecas vendidos
num_payasos = int(input("Por favor, introduce el número de payasos vendidos: "))
num_muñecas = int(input("Por favor, introduce el número de muñecas vendidas: "))

# Calcular el peso total del paquete
peso_total = (num_payasos * peso_payaso) + (num_muñecas * peso_muñeca)

# Mostrar el peso total en gramos
print(f"El peso total del paquete que será enviado es: {peso_total} gramos")