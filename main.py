from control_estudiante import ControlEstudiante

def main():
    control = ControlEstudiante()
    ruta = input("Ingrese la ruta del archivo CSV: ")
    control.leerEstudianteCsv(ruta)
    control.mostrarMateriasPorEstudiante()

if __name__ == "__main__":
    main()