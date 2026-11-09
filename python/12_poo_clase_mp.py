class UnidadTransporte:
    nombre: str
    tipo: str

    def __init__(self, nombre: str, tipo: str):
        self.nombre = nombre
        self.tipo = tipo

    def mostrar_info(self):
        print("Unidad: ", self.nombre)
        print("Tipo: ", self.tipo)



trole1 = UnidadTransporte("Trole-01", "Articulado")
ecovia1 = UnidadTransporte("Ecovía-05", "Biarticulado")
ecovia2 = UnidadTransporte("Alimentador-12", "Convencional")
ecovia3 = UnidadTransporte("Karla", "Administrativa")