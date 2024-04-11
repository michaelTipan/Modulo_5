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

    @classmethod
    def auto_nuevo(cls):
        return cls("Toyota", "Fortuner", 2024)

    @staticmethod
    def comparar_kilometraje(auto1, auto2):
        if auto1.kilometraje == auto2.kilometraje:
            print("Tienen el mismo kilometraje")
        else:
            print("Tienen diferente kilmetraje")

    @staticmethod
    def es_auto_nuevo(auto):
        if auto.año == 2024 and auto.kilometraje == 0:
            print("El auto es nuevo")
        else:
            print("El auto es usado")

    @classmethod
    def auto_usado(cls):
        marca = "Chevrolet"
        modelo = "Spark"
        año = "2020"
        auto = cls(marca, modelo, año)
        auto.actualizar_kilometraje(35000)
        return auto



mi_auto = Auto("Toyota", "Corolla", 2020)
mi_auto.mostrar_informacion()
mi_auto.actualizar_kilometraje(15000)
mi_auto.actualizar_kilometraje(10000)
mi_auto.realizar_viaje(5000)
mi_auto.realizar_viaje(-200)
mi_auto.estado_auto()

auto1 = Auto.auto_nuevo()
auto1.mostrar_informacion()
Auto.es_auto_nuevo(auto1)
auto2 = Auto.auto_usado()
auto2.mostrar_informacion()
Auto.es_auto_nuevo(auto2)
Auto.comparar_kilometraje(auto1, auto2)


