from abc import ABC, abstractmethod

class UnidadTransporte(ABC):
    @abstractmethod
    def iniciar_ruta(self):
        pass

class Trolebus(UnidadTransporte):
    def iniciar_ruta(self):
        return "despacho autorizado"

trole1 = Trolebus()
print(trole1.iniciar_ruta())