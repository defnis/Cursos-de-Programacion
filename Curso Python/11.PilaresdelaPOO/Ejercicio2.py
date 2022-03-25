
'''   
Ejercicio 1

Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.
'''

class Calculadora():
    def __init__(self, num1 , num2):
        self.num1 = int(input("Ingrese el primer valor: "))
        self.num2 = int(input("Ingrese el segundo valor: "))

    def suma(self):
        self.suma = self.num1 + self.num2
        return " La suma da como resultado: ", self.suma

    def renta(self):
        self.rensta = self.num1 - self.num2
        return " La resta da como resultado: ", self.resta

    def multiplicacion(self):
        self.multiplicacion = self.num1 * self.num2
        return " La multiplicacion da como resultado: ", self.multiplicacion

    def division(self):
        self.division = self.num1 / self.num2
        return " La division da como resultado: ", self.division

    
calcular = calculadora
calcular.suma()
print(calcular.resta)
print(calcular.multiplicacion)
print(calcular.division)