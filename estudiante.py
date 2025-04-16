from materia import Materia

class Estudiante:
    def __init__(self, cedula: str, nombre: str):
        self.__cedula = cedula
        self.__nombre = nombre
        self.materias = []
    
    @property
    def cedula(self) -> str:
        return self.__cedula
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    def agregar_materia(self, materia: Materia) -> None:
        self.materias.append(materia)
    
    def cantidad_materias_inscriptas(self) -> int:
        return len(self.materias)