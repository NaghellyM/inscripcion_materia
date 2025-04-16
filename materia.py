class Materia:
    def __init__(self, codigo: str, nombre: str):
        self.__codigo = codigo
        self.__nombre = nombre

    @property
    def codigo(self) -> str:
        return self.__codigo
    
    @property
    def nombre(self) -> str:
        return self.__nombre

