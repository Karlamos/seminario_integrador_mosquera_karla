class UnidadTransporte:
    nombre: str
    __kilometro: int

    def __init__(self, nombre: str, kilometro: int):
        self.nombre = nombre
        self.kilometro = kilometro

    def mostrar_info(self):
        print("Unidad: ", self.nombre)
        print("Kilometraje: ", self.__kilometro)



trole1 = UnidadTransporte("Trole-01", 90000)
ecovia1 = UnidadTransporte("Ecovía-05", 6000)
ecovia2 = UnidadTransporte("Alimentador-12", 16000)
ecovia3 = UnidadTransporte("Karla", 5000)