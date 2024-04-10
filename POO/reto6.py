class Auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = 0

    def mostrar_informacion(self):
        print(self.__dict__)

    def actualizar_kilometraje(self, kilometraje):
        if kilometraje >= self.kilometraje:
            self.kilometraje = kilometraje
        else:
            print("No se puede reducir el kilometraje.")

    def realizar_viaje(self, kilometros):
        if kilometros > 0:
            self.kilometraje += kilometros
        else:
            print("La cantidad de kilómetros debe ser positiva.")

    def estado_auto(self):
        if self.kilometraje < 20000:
            print("Estoy como nuevo")
        elif 20000 <= self.kilometraje <= 100000:
            print("Ya estoy usado")
        else:
            print("¡Ya déjame descansar por favor!")

mi_auto = Auto("Toyota", "Corolla", 2020)
mi_auto.mostrar_informacion()
mi_auto.actualizar_kilometraje(15000)
mi_auto.actualizar_kilometraje(10000)
mi_auto.realizar_viaje(5000)
mi_auto.realizar_viaje(-200)
mi_auto.estado_auto()

