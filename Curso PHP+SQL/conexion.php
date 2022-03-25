<?php 

function regresarConexion(){
    $server="localhost";
    $usuario="root";    //Se puede agregar un usuario y contrase;a si lo desea.
    $clave="";
    $base="piuquelom";  // Este nombre lo extraemos desde XAMPP.
    $conexion=mysqli_connect($server,$usuario,$clave,$base) or die ("Error de Conexion!");  //Esto nos mostrara en pantalla si hay algun error.
    mysqli_set_charset($conexion,'utf8');
    return $conexion;
}

?>
