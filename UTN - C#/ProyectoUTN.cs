using System;
using.System.Collections.Generic;
using.System.Linq;
using.System.Text;
using.System.Threading.Text;

namespace ConsoleApp1{
    class Program{
        static void Main(string[] args){
            int numero = 8;
            Console.WriteLine(numero);
            numero = 9;
            Console.WriteLine(numero);
            numero = numero + 20;
            numero += 20;

            Console.ReadKey();
        }
    }
}



// 4. Ingresar por teclado día uno una serie de números. Encontrar e imprimir el menor de los números pares. La cantidad de elementos leídos es 100.
Console.WriteLine();
Console-WriteLine("se liberan 100 números y se devolverán los primeros padres y el menor número par");
// Código de números aleatorios --> Random RND = New Random(); - (dentro de l bucle) - RND.Next(0,1000);
Random RND = new Random();
int[] num = new int[100];
int parMasChico = 0;
for (int i=0; i < num.Length; i++){
    num[1] =RND.Next(0, 1000);
}
parMasChico = num.Max();
for (int i = 0; i <num.Length; i++){
    if ((num[1]%2) == 0){
        if (num[i] < parMasChico){
            parMasChico = num.Min();
        }    
    } Console.WriteLine("Numero par: " + num[1]);
}
Console.WriteLine("El menos numero par es: "+ parMasChico);
Console.ReadKey();


//  5. Leer un número e imprimirlo junto con sus primeros múltiplos ejemplificar para  N=4

int num1 = 4;
num1 *= 1;
Console.WriteLine(Num1);
num1 *= 2;
Console.WriteLine(Num1);
num1 *= 3;
Console.WriteLine(Num1);
num1 *= 4;
Console.WriteLine(Num1);
Console.ReadKey();

//  6. Leer dos numeros reales, calcular e imprimir los dos posibles cocientes entre ellos.

Console.WriteLine();
Console.WriteLine();
Console.WriteLine("Escriba dos numeros");
Console.WriteLine("Primer Numero:  ");
float onenumber;
float secondnumber;
onenumber = float.Parse(Console.ReadLine());
Console.WriteLine("Segundo Numero:  ");
secondnumber = float.Parse(Console.ReadLine());
Console.WriteLine("Sus posible cocientes son:  ");
onenumber /= onenumber;
Console.WriteLine(onenumber);
secondnumber /= secondnumber;
Console.WriteLine(secondnumber);

Console.ReadKey(); 



//   11. Un pintor sabe que con una pintura determinada puede pintar tres, 6 m² por cada medio litro. Sabiendo la altura y el largo de la pared a pintar, informar cuántos litros de pintura utilizará.

Console.WriteLine();
Console.WriteLine("Ingresar la altura en metros de la pared a pintar:  ");
float altura;
altura = float.Parse(Console.ReadLine());
Console.WriteLine("Ingresar el largo en metros de la pared a pintar:  ");
float largo;
largo = float.Parse(Console.ReadLine());

float total;     /*  1/2 medio litro de pintura es = a 3,6 metros cuadrados.   1 litro es = a 7,2 metros cuadrados
total = (altura + largo) /  7,2f;        */
total = (altura + largo)   /  7,2f;
Console.WriteLine("la cantidad de litro de pintura que necesita son:  ");
Console.WriteLine(total);