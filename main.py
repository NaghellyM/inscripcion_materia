from control_estudiante import ControlEstudiante

def main():
    control = ControlEstudiante()
    control.leerEstudianteCsv( "materia.txt")
    control.mostrarMateriasPorEstudiante()

if __name__ == "__main__":
    main()