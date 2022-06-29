CREATE TABLE user (
id int not null auto_increment,
name varchar(50) not null,
edad int not null,
email varchar(100) not null,
PRIMARY KEY (id)
);

INSERT INTO user (name, edad, email) values ('Oscar', 55, 'oscar@gmail.com');
INSERT INTO user (name, edad, email) values ('Layla', 35, 'layla@gmail.com');
INSERT INTO user (name, edad, email) values ('Jose', 25, 'jose@gmail.com');
INSERT INTO user (name, edad, email) values ('Chanquito', 5, 'chanchito@gmail.com');

select * from user;
select * from user limit 1;
select * from user where edad > 15;
select * from user where edad >= 20;
select * from user where edad >15 and email='jose@gmail.com';
select * from user where email != 'layla@gmail.com';
select * from user where edad between 15 and 36;
select * from user where email like '%gmail%'; -- Busca todo lo que contenga gmail no importa lo que este delante o final. 
select * from user where email like '%gmail'; -- No importa lo que este delante de gmail, pero tiene que terminar si o si.  

select * from user order by edad asc;  -- Busca la edad por orden ascendente.  
select * from user order by edad desc; 

select max(edad) as mayor from user; -- Buscara quien tiene la erdad mayor. Y el texto de la columna se llamara MAYOR

select id, name from user;
select id name from nombre; -- Cambiamos el nombre de name por nombre.  




