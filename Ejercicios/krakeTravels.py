pais = input("Ingrese el país de destino (En mayusculas y sin tildes): ")
zona = input("Ingrese la zona en la que se encuentra (En mayusculas y sin tildes): ")
velocidad = float(input("Ingrese la veloCidad actual del automovil: "))

# PARA ECUADOR
if pais == "ECUADOR":
    if zona == "URBANA":
        if velocidad >= 10 and velocidad <= 50:
            print("SI Respeta el límite de velocidad")
        elif velocidad < 10:
            print("Se encuentra por DEBAJO del minimo de velocidad")
        else:
            print("Se encuentra por ENCIMA del maximo de velocidad")
    elif zona == "RURAL":
        if velocidad >= 51 and velocidad <= 70:
            print("SI Respeta el límite de velocidad")
        elif velocidad < 51:
            print("Se encuentra por DEBAJO del minimo de velocidad")
        else:
            print("Se encuentra por ENCIMA del maximo de velocidad")
    elif zona == "PERIMETRAL":
        if velocidad >= 71 and velocidad <= 90:
            print("SI Respeta el límite de velocidad")
        elif velocidad < 71:
            print("Se encuentra por DEBAJO del minimo de velocidad")
        else:
            print("Se encuentra por ENCIMA del maximo de velocidad")

# PARA COLOMBIA
elif pais == "COLOMBIA":
    if zona == "URBANA":
        if velocidad >= 10 and velocidad <= 30:
            print("SI Respeta el límite de velocidad")
        elif velocidad < 10:
            print("Se encuentra por DEBAJO del minimo de velocidad")
        else:
            print("Se encuentra por ENCIMA del maximo de velocidad")
    elif zona == "RURAL":
        if velocidad >= 31 and velocidad <= 80:
            print("SI Respeta el límite de velocidad")
        elif velocidad < 31:
            print("Se encuentra por DEBAJO del minimo de velocidad")
        else:
            print("Se encuentra por ENCIMA del maximo de velocidad")
    elif zona == "PERIMETRAL":
        if velocidad >= 81 and velocidad <= 100:
            print("SI Respeta el límite de velocidad")
        elif velocidad < 81:
            print("Se encuentra por DEBAJO del minimo de velocidad")
        else:
            print("Se encuentra por ENCIMA del maximo de velocidad")
            
# PARA PERU
elif pais == "PERU":
    if zona == "URBANA":
        if velocidad >= 10 and velocidad <= 40:
            print("SI Respeta el límite de velocidad")
        elif velocidad < 10:
            print("Se encuentra por DEBAJO del minimo de velocidad")
        else:
            print("Se encuentra por ENCIMA del maximo de velocidad")
    elif zona == "RURAL":
        if velocidad >= 41 and velocidad <= 60:
            print("SI Respeta el límite de velocidad")
        elif velocidad < 41:
            print("Se encuentra por DEBAJO del minimo de velocidad")
        else:
            print("Se encuentra por ENCIMA del maximo de velocidad")
    elif zona == "PERIMETRAL":
        if velocidad >= 61 and velocidad <= 120:
            print("SI Respeta el límite de velocidad")
        elif velocidad < 61:
            print("Se encuentra por DEBAJO del minimo de velocidad")
        else:
            print("Se encuentra por ENCIMA del maximo de velocidad")

else:
    print("Nombre del pais invalido")

    

