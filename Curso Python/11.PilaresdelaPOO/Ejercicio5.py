'''   
Ejercicio 1

Crear un programa con tres clases Universidad, con atributos nombre (Donde se almacena el nombre de la Universidad). Otra llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.
'''

class Universidad():
    def __init__(self, nombre):
        self.nombre = nombre 

class Carrera():
    def carrera(self,especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carrera):
    def datos(self, nombre, edad):
        self.nombre = nombre 
        self.edad = edad 
        print("Mi nombre es {}, tengo {} anios, mi especialidad es {}. Estudio en la universidad{}".format(self.nombre, self.edad, self.especialidad, self.nombre))

persona = Estudiante("Don Bosco")
persona.carrera("Sistema")
persona.datos("Carlos",20)