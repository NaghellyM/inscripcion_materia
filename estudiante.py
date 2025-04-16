from materia import Materia

class Estudiante:
    def __init__(self, cedula: str, nombre: str):
        self.__cedula = cedula
        self.__nombre = nombre
        self.materias = []
    
    def agregarMateria(self, materia: Materia) -> None:
        self.materias.append(materia)
    
    def cantidadMateriasInscriptas(self) -> int:
        return len(self.materias)