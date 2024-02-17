class Persona:
 
    def __init__(self, nombre, edad):
        self.nombre = nombre 
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} tengo: {self.edad} años.")

persona1 = Persona("DEM",20)
persona1.saludar()


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def estudiar(self):
        print(f"{self.nombre} esta estudiando el {self.grado}.")

estudiante1=Estudiante("Gabriela", 29, "maestria")
estudiante1.saludar()
estudiante1.estudiar()