menu_platos = []
opcion=0

def mostrar_menu():
    print(  "--- RESTAURANT SEGUNDA ES TODO ---\n"
        "1.      Añadir plato al menú.\n"
        "2.      Buscar en el menú.\n"
        "3.      Eliminar plato del menú.\n"
        "4.      Mostrar platos del menú.\n"
        "5.      Salir.\n\n")
    
    try:
        global opcion
        opcion=int(input("Elija una opcion: "))
        if opcion >=1 and opcion <= 4:
            if opcion == 1:
                plato = input("Ingrese el nombre del plato para añadir al menu: ")
                menu_platos.append(plato)
                print(f"\n\n\tEl plato {plato} fue añadido correctamente\n\n")
            elif opcion == 2:
                plato = input("Ingrese el nombre del plato que busca: ")
                numero_plato = menu_platos.index(plato)
                print(f"\n\n\t Plato encontrado: {menu_platos[numero_plato]} \n\n")
            elif opcion == 3:
                plato = input("Ingrese el nombre del plato que desea eliminar: ")
                menu_platos.remove(plato)
                print(f"\n\n\tEl plato {plato} fue eliminado correctamente\n\n")
            elif opcion == 4:
                print(f"\n\n\t{menu_platos} \n\n")
            elif opcion == 5:
                print("Salir")
    except:
        print("\n\n\tDebe ingresar un numero\n\n")

while opcion != 5:
    mostrar_menu()

    
    



    

