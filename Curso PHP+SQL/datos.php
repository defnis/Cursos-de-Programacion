<?php 
//  Funcion GET....obtener datos
// Funcion POST.....enviar datos.

header('Content-type: application/json');

require("conexion.php");           // Estoy importando los datos de mi archivo
$conexion = regresarConexion();    // Y aca los estoy guardando.

switch ($_GET['accion']) {
    case 'listar':
        $datos = mysqli_query($conexion, "select id, nombre, precio from articulos")
        $resultado = mysqli_fetch_all($datos, MYSQLI_ASSOC);
        echo json_encore($resultado);
        break;
    case 'agregar':
        $respuesta = mysqli_query($conexion, "insert into articulos (nombre, precio) values ('$_POST[nombre]','$_POST[precio]')");
        echo json_encode($respuesta); //Esto es para convertirlo en json.
        break;
    case 'borrar':
        $respuesta = mysqli_query($conexion, "delete from articulos where id=$_GET[id]");
        echo json_encode($respuesta);
        break;
}




// Listar los elementos.
//"select id, nombre, precio from articulos"

//Agregar
//"insert into articulos (nombre, precio) values ('$_POST[nombre]','$_POST[precio]')"

//Borrar
//"delete from articulos where id=$_GET[id]"

//Consultar
//"select id, nombre, precio from articulos where id=$_GET[id]"

//Modificar o Actualizar
//"update articulos set nombre='$_POST[nombre]'   
 //                    precio='$_POST[precios]'
 //                    where id=$_GET[id] "  //Post es los datos que envio y get los que recibe y modifica.


?>