from unittest import TestCase
from unittest.mock import patch

from src.control_estudiante import ControlEstudiante


class TestMostrarMateriasPorEstudiante(TestCase):

    @patch("builtins.print")
    def test_mostrar_materias_por_estudiante(self, mock_print):
        control = ControlEstudiante()
        control.leer_estudiante_csv("test/test_inscriptos.txt")
        control.mostrar_materias_por_estudiante()

        mock_print.assert_called_with("Daniel: 2 materias")
