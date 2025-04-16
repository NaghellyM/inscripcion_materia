import csv
from estudiante import Estudiante
from materia import Materia

class ControlEstudiante:
    def __init__(self):
        self.estudiantes = {}  # Diccionario {cedula: Estudiante}
    
    def leer_estudiante_csv(self, path: str) -> None:
        try:
            with open(path, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) != 4:
                        continue
                    
                    cedula, nombre, codigo_materia, nombre_materia = row
                    
                    if cedula not in self.estudiantes:
                        self.estudiantes[cedula] = Estudiante(cedula, nombre)
                    
                    materia = Materia(codigo_materia, nombre_materia)
                    self.estudiantes[cedula].agregarMateria(materia)
        
        except FileNotFoundError:
            print(f"Error: Archivo no encontrado en {path}")
        except Exception as e:
            print(f"Error al procesar archivo: {str(e)}")
    
    def mostrar_materias_por_estudiante(self) -> None:
        for estudiante in self.estudiantes.values():
            cantidad = estudiante.cantidadMateriasInscriptas()
            print(f"{estudiante.nombre}: {cantidad} materia{'s' if cantidad != 1 else ''}")