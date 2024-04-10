datos = []

num = int(input("Cuantos datos desea ingresar?: "))

for i in range(num):
    entrada = input(f"Ingrese el dato {i+1}: ")
    # Verificar si es un número
    if entrada.isdigit():
        datos.append(int(entrada))
    # Verificar si es un número flotante
    elif entrada.replace('.', '', 1).isdigit():
        datos.append(float(entrada))
    # Verificar si es una cadena
    else:
        datos.append(entrada)

print(f"Su lista es: {datos}")

