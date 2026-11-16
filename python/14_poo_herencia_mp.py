class UnidadTransporte:
    nombre: str
    tipo: str

    def __init__(self, nombre: str, tipo: str):
        self.nombre = nombre
        self.tipo = tipo

    def mostrar_info(self):
        print("Unidad: ", self.nombre)
        print("Tipo: ", self.tipo)

class UnidadArticulada(UnidadTransporte):
    def __init__(self, nombre: str, tipo: str):
        super().__init__(nombre, tipo)

    def muestra_nombre(self):
        print("Nombre de unidad: ", self.nombre)

trole1 = UnidadArticulada("Trole-01", "Articulado")
ecovia1 = UnidadArticulada("Ecovía-05", "Biarticulado")
trole1.mostrar_info()
ecovia1.mostrar_info()
trole1.muestra_nombre()
ecovia1.muestra_nombre()