class Evaluacion:
    def __init__(self, calificacion):
        self.calificacion = calificacion

    def determinar_calificacion(self):
        if self.calificacion>9.0:
            return "A"
        elif self.calificacion>8.0:
            return "B"
        elif self.calificacion>=7.5:
            return "C"
        else:
            return "R"
    def mostrar_calificacion(self):
        clasificacion = self.determinar_calificacion()
        print(f"La calificacion es {clasificacion}.")

def main():
    calificacion = float(input("Ingrese calificacion: "))
    evaluacion = Evaluacion(calificacion)
    evaluacion.mostrar_calificacion()

if __name__ == "__main__":
    main()