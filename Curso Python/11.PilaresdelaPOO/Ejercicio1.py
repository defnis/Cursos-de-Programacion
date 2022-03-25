'''    
Ejercicio 1

Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
'''

class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota 

    def imprimir(self):
        print("Nombre: {} \n Nota: {}".format(self.nombre, self.nota))

    #Condicional para mostrar los resultados.
    def resultados(self):
        if self.nota < 7:
            print("Has Desaprobado!")
        else:
            print("Has Aprobado.")

estudiante1 = Estudiante("Daniel", 10)
estudiante1.imprimir()
estudiante1.resultados()


