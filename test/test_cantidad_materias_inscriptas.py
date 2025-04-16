from unittest import TestCase
from src.estudiante import Estudiante
from src.materia import Materia

class TestCantidadMateriasInscriptas(TestCase):
   
    def test_cantidad_materias_inscriptas(self):
        estudiante = Estudiante("9669","Daniel")
        materia1 = Materia("45475","SoftwareI")
        materia2 = Materia("5556","Bases II")
        estudiante.agregar_materia(materia1)
        estudiante.agregar_materia(materia2)
        self.assertEqual(estudiante.cantidad_materias_inscriptas(), 2)

    def test_cantidad_materias_inscriptas_vacio(self):
        estudiante_vacio = Estudiante("87654321", "Maria Lopez")
        self.assertEqual(estudiante_vacio.cantidad_materias_inscriptas(), 0)

