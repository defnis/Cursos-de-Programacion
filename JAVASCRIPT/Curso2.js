/*      CAPITULO 7        */
/*
42)    INTRODUCCION A WINDOWS   windows object javascrips (esta toda la info sobre este tema)

- Hereda las propiedades de EventTarget.
- open() - Carga un recurso en el contexto de un nuevo navegador o uno que ya existe.*/
let youtubeURL = "https://youtube.com";
let ventana = window.open(youtubeURL);

/* En el ejemplo anterior lo usamos Open cuando queremos que el usuario clic en un botón y abra una nueva página.
- close() - Cierra la ventana actual o la ventana en la a la que se llamo. Cuando el usuario termina de hacer la accion, la pagina se cierra. */
let ventana = window.close(youtubeURL);

/*
- closed - Indica si la ventana referenciada está cerrada o no. (En la consola vemos si la ventana esta abierta o no, nos devuelve un resultado boleano, true or false)

- stop() - Detiene la carga de recursos en el contexto de navegación actual. Cuando se esta cargando una pagina con este codigo le decimos que se pare.*/
let ventana = window.stop(youtubeURL);

/*
- alert() - Muestra un cuadro de alerta con el contexto específico y un botón aceptar.*/
window.alert("Bienvenidos a Josesito");
alert("Bienvenido Josesito");

/* Las dos forma de escribir alert esta bien.
- print() - Abre el cuadro de diálogo imprimir para imprimir el documento actual. 
- promt() - Abre un cuadro de diálogo con un mensaje que solicita al usuario un dato. (String)
- conform() - Abre un cuadro de diálogo con un mensaje y dos botones aceptar y cancelar. Eje: Estas seguro que deseas salir de la pagina.

- screen - Devuelve una referencia al objeto de pantalla asociado con la ventana.
- screenLeft - Devuelve la distancia horizontal entre el borde izquierdo del navegador y el borde izquierdo de la pantalla.
- screenTop - Devuelve la distancia vertical entre el borde superior del navegador y el borde superior de la pantalla.*/
const screenLeft = window.screenLeft;
const screenTop = window - screenTop;

document.write(screenLeft);
document.write(`Left: <b>${screenLeft}</b><br>`);
document.write(`Top: <b>${screenTop}</b><br>`);


/*
- scrollX - Devuelve el número de pixeles que el documento se desplaza actualmente horizontalmente.
- scrollY - Devuelve el número de pixeles que el documento se desplaza actualmente verticalmente.
- scroll() - Desplaza la ventana a un lugar particular del documento. (con options y con posiciones). Escribimos en la console y nos desplaza a la posicion que le pedimos.

- minimize() - minimiza la ventana.
- resizeBy() - Cambia el tamaño de la ventana actual en una cantidad específica.
- resizaTo() - Re dimensiones dinámicamente la ventana.
- moveBy() - Mueve la ventana en una ubicación relativa.
- moveTo() - Mueve la ventana en una ubicación absoluta. 

- Objetivos barprop (En caso que sea visible nos va a decir true sino es false)
        -localizados
        - menubar
        - personalbar
        - scrollbars
        - statusbars
        - toolbar       */

let href = window.location.href;
let pathname = window.location.pathname;
let hostname = window.location.hostname;
let protocol = window.location.protocol;

let html = `Protocolo: <b>${protocol}</b><br>`;
html += `Hostname: <b>${hostname}</b><br>`;
html += `Pathname: <b>${pathname}</b><br>`;
html += `URL Completa: <b>${href}</b><br>`;

document.write(html)



/*    CAPITULO 8    */

/*
45)  Herramientos de Desarrrollo del navegador (Chromoe)

46)  Pestaña Elements
        - Filtros y Buscar por palabras claves.
        - Modificar, crear y eliminar etiquetas.
        - Modificar propiedades de CSS.
        - Event Listeners.
        - Properties.
        - Opciones para copiar.
        - Seguir explorando.

47)  Pestaña Resources
        - Very guardar archivos.
        - Información ofrecida.
        - Cambio en tiempo real.
        - Snippets - Ejecutar codifo de fragmentos.

48)  Pestaña Networks
        - Interfaz.
        - Sort By y filtros de búsqueda.
        - Limpiar cookies y caché.
        - Importar y exportar.

49)  Pestaña Timeline
        - Tu grabación.
        - Screenshots de la grabación.
        - Controls.
        - Overview.
                *Fps, CPU y Net.
        - Flame Chart.
        - Details.
        - Gerencia de grabación.

50)  Pestaá Application.
        - Aplication.
        - Storege
        - Caché.
        - Backgraund Services.
        - Frames.
*/

/*       CAPITULO  9     */

/*
EVENTOS
        - Definicion.
        - de Eventos o Event Handles.
        - Escucha de eventos o Event Listeners.
        - El objert Event
        - Flujo de enventos o Event flow.
        - Event Bubbing vs Event Capturing.
        - event.stopPropagation()

EVENTOS DEL MOUSE
        - click - ocurri con un click.
        - dbclick - ocurre con un doble click.
        - mouseover - Ocurre cuando el puntero se mueve sobre un elemento o sobre uno de sus hijos.
        - mouseout - Ocurre cuando se mueve el puntero fuera de un elemento o de sus elementos secundarios.  -  Otros -
        - contextmenu - Ocurre con un clic en el botón derecho en un elemento para abrir un menú contextual.
        - mouseenter - Ocurre cuando el puntero se mueve sobre un elemento.
        - mouseleave - Ocurre cuando el puntero se mueve fuera de un elemento.
        - mouseup - Ocurre cuando un usuario suelta un botón del mouse sobre un elemento.
        - mousemove - Ocurre cuando el puntero se mueve mientras está sobre un elemento.
        
EVENTOS DEL TECLADO
        - keypress - Corre con una tecla se presiona.
        - keydown - Ocurre con una tecla se deja de presionar.
        - onkeyup - Ocurre después de qué los dos eventos anteriores hayan concluido consecutivamente.

EVENTOS DE LA INTERFAZ
        - error - Ocurre cuando sucede un error durante la carga de un archivo multimedia.
        - load - Ocurre cuando un objeto se ha cargado.
        - beforeunload - Ocurre antes de que el documento esté apunto de descargarse.
        - unload - Ocurre una vez que se ha descargado una página.
        - resize - Curre cuando se cambia el tamaño de la vista del documento.
        - acroll - Ocurre cuando se desplaza la barra de desplazamiento de un elemento.
        - Select - Ocurre después de qué el usuario selecciona algún texto de input o 

TIMERS
        - setTimeOut()
        - setInterval()
        - clearTimeout()
        - clearInterval()
*/


/*       PROBLEMA DE COFLA      */

/*
A) Coge reprobó dos materias y ahora tiene que enviar un formulario para registrarse en la materia que debe.
        - El formulario debe contener nombre completo Male y materia adeudada.
        - Se debe validar que el Male sea válido, que los nombres eran reales.
        - Se debe enviar al servidor de manera pulida.

Archivo HTML
<body>
        <form autocomplete="off">
                <h2>Inscripcion de materias adeudadas</h2>
                <input type="text" placeholder="Nombre Completo" id="nombre">
                <input type="email" placeholder="Mail" id="mail" required="">  //Required es obligatoria rellenar el campo.
                <input type="text" placeholder="Materia Adeudada" id="materia">
                <input type="submit" valu="Solicitar Mesa" id="btn-enviar">
        </form>
        <script src="codigo.js"></script>
<body>
*/

const nombre = document.getElementById("nombre");
const mail = document.getElementById("mail");
const materia = document.getElementById("materia");
const boton = document.getElementById("boton");
const resultado = document.querySelector("resultado");

boton.addEventListener("click", (e) => {
    e.preventDefault();
    let error = validarCampos();
    if (error[0]) {
        resultado.innerHTML = error[1];
        resultado.classList.add("red"); //Resuldaro negativo.
    } else {
        document.querySelector("resultado").innerHTML = "Solicitud enviada correctamente";
        resultado.classList.add("green"); //Resultado positivo.
    }
})

const validarCampos = () => {
    let error = []; //Error va a ser un array.
    if (nombre.Value.length < 5) {
        error[0] = true;
        error[1] = "El nombre no puede contener menos de 5 caracteres.";
        return error;
    } else if (nombre.Value.length > 40) {
        error[0] = true;
        error[1] = "El nombre no puede superar los 40 caracteres.";
        return error;
    } else if (mail.value.length < 5 || mail.value.length > 40 || mail.indexOf("@") == -1 || mail.indexOf(".")) {
        error[0] = true;
        error[1] = "El mail es invalido"
        return error;
    } else if (materia.value < 4 || materia.value > 40) {
        error[0] = true;
        error[1] = "La materia no existe";
    }
    error[0] = false;
    return error;
}


/*   SEGUNDO PROBLEMA DE COFLA   */
/*   
B) Los datos de copla y de otros alumnos fueron recibidos Y ya están almacenados, ahora hay que crear un sistema que muestre esa información y se pueda asignar cuando rinde.

        - La interfaz debe ser agradable y atractiva.
        - Debe contener todos los datos de manera estructurada.
        - El profesor puede seleccionar en cuál de las dos semanas rinde el usuario.
        - Si el profesor confirma, los datos se deben actualizar y reemplazar el espacio de selección de semana por la semana seleccionada.
*/
/*   HTML5

<head>
<titler> Historia de cofla 9 </title>
<body>
<div class="grid-container">
</div>
<button class="boton-confirmar">Confirmar</button>
<script src="codigo.js"></script>
*/

let alumnos = [{
    nombre = "Lucas Dalto",
    mail = "soydalto@gmail.com",
    materia = "Fisica 3",
}, {
    nombre = "Belen Rodriguez",
    mail = "belu@gmail.com",
    materia = "Analisis 2",
}, {
    nombre = "Dario Waiman",
    mail = "paleta@gmail.com",
    materia = "Matematica 3",
}, {
    nombre = "Cofla",
    mail = "cofla@gmail.com",
    materia = "Logica 4",
}];



for (alumno in alumnos) {
    let datos = alumnos[alumno];
    let nombre = datos["nombre"];
    let mail = datos["mail"];
    let materia = datos["materia"];
    let htmlCode = `
        <div class="grid-item nombre">${nombre}</div> 
        <div class="grid-item mail">${mail}</div> 
        <div class="grid-item materia">${materia}</div> 
        <div class="grid-item semana"> 
                <select class="grid-item semana-elegida">
                        <option value="1">Semana 1</option>
                        <option value="2">Semana 2</option>
                </selection>
        </div>`;
    document.querySelector(".grid-container").innerHTML += htmlCode;
}

boton.addEventListener("click", () => {
    let elemento = document.querySelectorAll(".semana");
    let semanasElegidas = document.querySelectorAll(".semana-elegida")
    for (elemento in elementos) {
        semana = elementos[elemento];
        semana.innerHTML = semanasElegidas[elemento].value;
    }
})

/*    CAPITULO  10     */
/*
 Control de flujo y manejo de errores.
  - Sentencia de bloque.   bloque es estar entre {}
  - Sentencias de control de flujo.  if  else   else if
  - Sentencias de manejo de excepciones.

Sentencia Switch
  - Sintaxis y clausura de clase.
  - break.
  - default.  */

let fruta = "Pera";
switch (expr) {
    case "Banana":
        consolo.log("fruta es amarilla");
        break;
    case "Pera":
        console.log("tiene forma de mi tio Roberto");
        break;
    case "Manzana":
        console.log("Los primeros humanos la comienron");
        break;
}



/*  Problema de Cofla numero 10  */

/* 
A) Las mesas de examen ya finalizaron y el profesor le tomo un último examen especial a cofre, Yakov la hizo dos pruebas más, pero lamentablemente se rompió el sistema de inscripción de Notas, por ende habrá que crear una solución a este problema, desarrollando una web que sea capaz de simular su funcionamiento.

    - Crear mini interfaz para introducir nota.
    - Validar que no haya errores.
    - Se debe promediar la nota del profesor, con otras dos notas de trabajo anteriores.
    - Si el promedio es mayor a siete aprobó la materia. */

/*
<head>
    <title>Historia de Cofla 10</title>
    <link rel="stulesheet" type="text/css" href="estilos.css">
</head>
<body>
    <form class="formulario-de-notas">
        <h2> Introduce la nota del alumno</h2>
        <nput type="number" id="note">
        <input type="button" id="snd-nota" value="Otorgar Nota">
    </form>
<script src="codigo.js"></script>
</body>  */

const snedButton = document.getElementById('snd-nota');

snedButton.addEventListener("click", () => {
    let resultado, mensaje;
    try {
        prevRes = parseInt(document.getElementById('nota').value);
        if (isNaN(prevRes)) {
            throw "Gracioso";
        }
        mensaje = definirMensaje(prevRes)
        resultado = verificarAprobacion(8, 5, prevRes);
    } catch (e) {
        resultado = "¿Sos Gracioso?";
        mensaje = "He descubierto que intentaste hachear el sitio web";
    }
    abrirModal(resultado, mensajes);
})

const verificarAprobacion = (pr) => {
    let resultado;
    switch (pr) {
        case 1:
            resultado = "No podes ser tan HDP";
            break;
        case 2:
            resultado = "Horrible";
            break;
        case 3:
            resultado = "Demasiado mal";
            break;
        case 4:
            resultado = "Muy mal";
            break;
        case 5:
            resultado = "Bastante mal";
            break;
        case 6:
            resultado = "Mal";
            break;
        case 7:
            resultado = "Con lo justo";
            break;
        case 8:
            resultado = "Bien";
            break;
        case 9:
            resultado = "Muy bien";
            break;
        case 10:
            resultado = "Increible";
            break;
        default:
            resultado = null;
    }
    return resultado
}
constverificarAprobacion = (nota1, nota2, prevRes) => {
    promedio = (nota1 + nota2 + prevRes) / 3;
    if (promedio >= 7) {
        return "<span class='green'> Aprobado</spam>";
    }
    return "<spam class='red'>Desaprobado</span>";
}

const abrirModal = (res, msg) => {
    document.querySelector(".resultado").innerHTML = res;
    document.querySelector(".mensaje").innerHTML = "Tu prueba: " + msg;
    let modal = document.querySelector(".modal-background");
    console.log(res);
    console.log(msg);
}


/* CAPITULO 11  */

/*   DESVENTAJAS DE TRABAJAR DE MAERA OBSOLETA

    - ¿cuándo algo se vuelve obsoleto?
        - "Deprecated"
        - Inutil
        - No recomendado
        - Con bigs o fallos.
        - Está por ser reemplazada.
        - Hay mejores formas de hacerlo.
    
    - Los efectos negativos (aplicados a métodos, clases y propiedades).
        - Su excesivo de recursos.
        - Código con Bugs o Fallos.
        - Código innesesariamente largo.
        - SEO
    
    - ¿cómo verificar si está obsoleto?
        - Uno de cada tres webs utiliza librerías de JavaScript obsoletas.
        - Verificar si tienen o usan funciones, métodos, objetos o metodologías obsoletas.
        - Verificar si los sitios basados en estándares oficiales.*/

let resultado = variable.anchor() // .anchor es un METODO.



/*   CAPITULO 12   -  CALLBACKS   */

/*
        - Conceptos (Funtion in funtion)    //Funcion dentro de otra funcion.
        - Ejemples 
        - Problema de los callbacks  */

function prueba(callbacks) {
    callbacks("Roberto");
}

prueba(nombre => console.log(nombre))


class Persona {
    constructor(nombre, instagram) {
        this.nombre = nombre;
        this.instagram = instagram
    }
}

console.log(new Persona("lucas dalto", "@soydalto"))

const datos = [ //Creamos una constante para nombrar varios nombres.
    ["Lucas Dalto", "@soydalto"],
    ["Roberto", "@roberto"],
    ["Rancio", "@rancio"],
    ["Camila", "@camila"]
]

constpersonas = [];

for (let i = 0; i < DataTransfer.length; i++) {
    personas[i] = new Persona(data[i][0], dalta[i][1]);
}

console.log(Persona[0]) //Nos muestra el nombre que esta en la posicion 0.


/*   PROMESAS  */

/* 
        - Concepto

        - ¿Que puede representar?
            - terminacion de una opetacion asíncrona.   //Operaciones resolve, reject
            - fracaso de una operacion asíncrona.

        -Ejemplos y solución al problema de los callbacks.    */

let nombre = "pedro";
const promesa = new Promise((resolve, reject) => {
    if (nombre !== "pedro") reject("Lo siento, el nombre no es pedro")
    else resolve(nombre)
})

console.log(promesa) //No nos muestra el valor que tiene porque esta encapsuado. nos muestra undefined

promesa.then((resultado) => {
    console.log(resultado)
}).catch((e) => { //Catch sirve para corregir el error.
    consolo.log(e)
})


/*   FUNCIONES ASINCRONAS */

const objeto = {
    propiedad1: "valor1",
    propiedad2: "valor2",
    propiedad3: "valor3"
};

const obtenerInformacion = () => {
    return objeto;
}

console.log(obtnerInformacion())
    //--------------------------------------------

const mostrarResultado = async() => {
    resultado = await obtenerInformacion();
    console.log(resultado);
}