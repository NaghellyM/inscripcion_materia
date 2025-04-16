from unittest import TestCase
from unittest.mock import patch

from src.estudiante import Estudiante
from src.materia import Materia


class TestMostrarMateriasPorEstudiante(TestCase):

    @patch("builtins.print")
    def test_mostrar_materias_por_estudiante(self, mock_print):
        estudiante = Estudiante("9669", "Daniel")
        materia1 = Materia("45475", "SoftwareI")
        materia2 = Materia("5556", "Bases II")
        estudiante.agregar_materia(materia1)
        estudiante.agregar_materia(materia2)
        mock_print.assert_called_with("Daniel: 2 materias")

    def test_mostrar_materias_por_estudiante_vacio(self, mock_print):
        estudiante_vacio = Estudiante("87654321", "Maria Lopez")
        mock_print.assert_called_with("Maria Lopez: 0 materias")
