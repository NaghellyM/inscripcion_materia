from src.control_estudiante import ControlEstudiante

def main():
    control = ControlEstudiante()
    control.leer_estudiante_csv( "src/materia.txt")
    control.mostrar_materias_por_estudiante()

if __name__ == "__main__":
    main()