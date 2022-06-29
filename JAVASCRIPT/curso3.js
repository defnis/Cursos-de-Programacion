//      CAPITULO 14   PROTOPITOS......

/*
27)  Prototipos.
    - Definicion.
    - Prototype chain.  Cadena de prototipo.
    - Prototype Object.

28)   Caracteristicas.
    - Un prototipo definido en un código fuente es mudable.
    - Es encimismo un objeto así como otros.
    - Tiene una existencia física en la memoria.
    - Puede ser modificado y llamado. 
    - Puede ser visto como un modelo ejemplar de una familia objeto.
    - Un objeto hereda propiedades (valores y métodos) de un prototipo.
*/

let objeto = {
    "propiedad": "datos"
}

console.log(objeto)

//.........................

let variable = ["pedro", 234, null];

variable.reverse() // La variable reverse no esta en el array sino en el proto.

console.log(variable)

//.............................

let variable = "string";

console.log(variable.__proto__)


//................................

class Objeto {       //   Esto es como funciona con un metodo.
    constructor(){
        hablar(){
            console.log("Hola!")
        }
    }
}

const Objeto = Objeto();  // Asi Funciona desde el prototipo.

let arr = []
arr.__proto__ = objeto;

arr.hablar()


/*
81)  Modo Estricto ("use strict")
    - Convierte errores de JavaScript en excepciones. 
    - Mejorando la optimización de los errores y consigue mejores tiempos de ejecución.
    - Evita sintaxis usadas en posteriores a ES6.
    - No permite que el programador realice una mala sintaxis.
*/

"use strict";

const obj = {};
Object.defineProperties(obj,'nombre',{value: "pedro", writeable: false})
obj.nombre = "roberto";
console.log(obj.nombre) 

/*
83)  Funciones Flecha.
    - Por qué aparecieron? (funciones compactas y el uso de This)
    - Si sólo hay una explicación, la retornan.
    - Paréntesis opcionales ante un solo parámetro (sin parámetros se requieren paréntesis).
    - No son adecuados para ser usadas como métodos y no pueden ser usadas como constructores.
    - Retornan literales si su cuerpo está entre ().
    - This contextual (no tiene propio This, sino que toman el de la función que lo envuelve)
    - Las reglas del modo estrictos aplicadas a this son ignoradas.
    - Función flecha invocada a través de los métodos call, apply y bind.
    - No tiene objetos Arguments.
    - No tiene propiedad del prototipo prototype.
    - No se puede usar Yield (por ende no se puede usar como funciones generadoras).
    - No puede contener saltos de línea entre sus parámetros y su flecha.
    - orden de parseo.
*/

let arr = ["manzana", "pera", "banana"];
let arr2 = ["kiwi", "naranja"];

arr.push(arr2[0], arr2[1]);
//arr.push(...arr2)  // De esta manera tengamos 50 o 1000 parametros nos agrega todos y no tenemos que escribir uno por uno.
console.log(arr);    // Esto esta bien cuando son pocos arrays, pero que pasa cuanto tengo que agregar 50 parametros.


/*
86)  Operadores Bit a bit
 - And  &
 - Or   |
 - XOR  ^
 - NOT  ~
*/


/*   CAPITULO 15 ....LAS APIS

API  Aplication programing interface ....Solicita informacion a otro sitio y resive un resultado.

88)  Objeto Date

 - getDate()    //  const fecha = new getDate(100000000000)   //100000000 es la cantidad de milisegundos que pasaron desde la fecha impuesta por la API. 
 - getDay()
 - getMonth()   // Enero = 0, Febrero = 1, Marzo = 2
 - getYear()    //console.log(fecha.getYear, + 1900)   //Por defecto la API resta 1900 a;os al a;o actual.
 - getHours()   
 - getMinutes()
 - getSeconds()
 - Ejemplo de uso Alarma.
 */

 "use strict";

const fecha = Date();  //Sin los ( ) el resultado es undefined.
console.log(fecha)


const fecha = new Date();  // Agregandole new podemos agregar metodos y objetos.
console.log(fecha)

const fecha = new Date(); 
console.log(fecha.getDate)  // Nos devuelve la fecha.  Domingo = 0, Lunes = 1 ...


/*
CREAR UN RELOG CON HTML, CSS Y JS

//CODIGO HTML
<body>
    <div class="reloj">
        <div class="hora">00</div>
         <div class="min">00</div>
         <div class="sec">00</div>
    </div>
<script src="codigo.js"></script>
</body>

//CODIGO CSS

body {
    color: #222;
    font-family: sans-serif;
}

.reloj {
    backgroung: linear-gradient(#111, #666);
    border: 2px solid #000;
    display: inline-flex;
    border-radius: 5px
}

.reloj div {
    color: #fff;
    padding:5px 7px;
    font-size: 20px;
    font-family: monospace;
}

*/
//CODIGO EN JAVASCRIPT

"use strict";

const addZeros = n =>{
    if(n.toString().length < 2) return "0".concat(n);
    return n;  //  Le digo, si el numero de 1 cifra, concatenar 0, Ejem: 01, 03, 06. Si el numero es de 2 cifras solo impriir ese numero.
}

const actualizarHora = ()=>{
    const time = new Date();
    let hora = time.getHours();
    let minutos = time.getMinutes();
    let segundos = time.getSeconds();
    console.log(segundos)
}

actualizarHora()
setInterval(actualizarHora,1000)  //Nos actualiza la hora cada segundo.
//  setInterval, ya no se usa m'as porque consume muchos recursos ya se usan librerias.

/*
89)  localStorage y SeccionStorage   // Almacenamiento local y almacenamiento de seccion. 
// localStorega almacena info y si cerramos la app no desaparece, SeccionStores cuendo salimos se borra.
    - diferencias.
    - setItem()   // A;ade un Item
    - getItem()  // obtiene ese Item.
    - removeItem()
    - Clear()
    - Ejemplos de Uso(Idiomas)


90)  Drag and Drop   /// Arratar y soltar.

    - Eventos del objeto
      - dragstart
      - drag
      - dragend
    
    - Eventos de zona
      - dragenter
      - dragmove
      - drop
      - dragleave
    
    - propiedad dataTransfer
      - getData()
      - setData()

    Ejemplos de Uso (Texturizador)

*/

"use strict"

const circulo = document.querySelector(".circulo");

circulo.addEventListener("dragstart", ()=>console.log(1)); //Cuando hago click sobre el circulo.
circulo.addEventListener("drag",()=>console.log(2));   //Cuenta los segundos que lo sostengo apretado.
circulo.addEventListener("dragend",()=>alert("Soldato"));  //Me da un alert cuando levano el dedo del objeto.


/*
91)   Geolocalizacion.

    - getCurrentPosition()
        -parametros (posicion, error, optiones)
    - watchCurrentPosition()    //  Es cuando se mueve, el watch actualiza la localizacion de posicion.
*/

"use strict";

const Geolocalization = navigator.geolocation;

const position = (pos)=>{
    console.log(log)
}

geolocation.getCurrentPosition(position)

/*
Historial (Libreria)

    - back() (vuelve atras)   // Es como tocar la flacha para retroceder en el navegador
    - forward() (va hacia adelante)
    - tama;o del historial.
    - go() (Va al sitio con un numero relativo)
    - pushState() (modifica URL y conserva la info)  ///le agrego al final jajaja...
    - propiedad state y evento popsatate.
    - replace

FieReader
    - ReadAsText()
    - ReadAsDataURL()
    - Ejemplo de uso, (Cargar galeria dinamina, conbinar drag and drop, barra de progresa con progress y loadendv )

IndexedBD (Es una ase de datos indexada, Mongo la usa)
    - Almacena información en el navegador de forma similar a localStorage.
    - Es orentada a objetos.
    - Es asincroma.
    - Trabaja con eventos del DOM.
    - Se puede hacer un CRUD (Create Read Update Delete)
    Toda esta info se encuentra en el inspector. Aplicatios Storage.
*/

"use strict"

const IDBRequest = indexedDB //(Crea la base de datos)
const IDBRequest = indexedDB.open("soydalto", 1) //(Abre la base de datos) 

IDBRequest.addEventListener("success", ()=>{
    console.log("Todo salio bien");  //Llamamos a la base de datos qye ya esta abierta.
})

IDBRequest.addEventListener("error",()=>{
    console.log("Ocurrio un error al abrir la base de datos");
})

console.log(IDBRequest);






