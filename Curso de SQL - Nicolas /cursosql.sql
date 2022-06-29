-- Crea una base de Datos --
create database holamundos; 
-- Muestra las bases de datos creadas --
show databases;
use holamundos;
-- Crea una tabla --
CREATE TABLE animales(
	id int,
    tipo varchar(255),
    estado varchar(255), 
    PRIMARY KEY (id)
);
-- Inserta caracteristicas --
INSERT INTO animales (tipo, estado) VALUES ('chanchito', 'feliz');
-- Modificar tabla --
ALTER TABLE animales MODIFY COLUMN id int auto_increment;

SHOW CREATE TABLE animales;

CREATE TABLE `animales` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo` varchar(255) DEFAULT NULL,
  `estado` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO animales (tipo, estado) VALUES ('chanchito', 'feliz');
INSERT INTO animales (tipo, estado) VALUES ('dragon', 'feliz');
INSERT INTO animales (tipo, estado) VALUES ('felipe', 'triste');

SELECT * FROM animales;
-- Selecciona desde animales el id numero 1 --
SELECT * FROM animales WHERE id=1;
-- Selecciona desde animales donde el estado es feliz --
SELECT * FROM animales WHERE estado= 'feliz';
-- Selecciona desde animales el estado feliz y un tipo de chanchito.
SELECT * FROM animales WHERE estado= 'feliz' AND tipo= 'chanchito';

UPDATE animales SET estado = 'feliz' WHERE id = 3;

SELECT * FROM animales;
-- Eliminar un registro desde la tabla de animales --
DELETE from animales WHERE id = 3;
SELECT * FROM animales;
UPDATE animales set estado = 'triste' where tipo = 'dragon';
-- Tanto delete como updete si no le marcamos el id nos marcara error.








