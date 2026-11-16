class Guerrero:
    nombre: str
    __poder: int

    def __init__(self, nombre:str, poder:int):
        self.nombre = nombre
        self.poder = poder

    def mostrar_info(self):
        print("Nombre ", self.nombre)
        print("Poder ", self.__poder)



goku = Guerrero("Goku", 90000 )
vegeta = Guerrero("Vegeta", 6000)
vegeta = Guerrero("Piccolo", 16000)
vegeta = Guerrero("Karla", 5000)

