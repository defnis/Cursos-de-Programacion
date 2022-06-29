create table products (
id int not null auto_increment,
name varchar(50) not null,
created_by int not null,
marca varchar (50) not null,
primary key (id),
foreign key (created_by) references user(id)
);

rename table products to product;

insert into product (name, created_by, marca)
values
	('ipad', 1, 'apple'),
    ('iphone', 1, 'apple'),
    ('watch', 3, 'apple'),
    ('macbook', 2, 'apple'),
    ('ipad mini', 1, 'apple');
    
select * from product;
-- Left join nos une los datos de usuarios con nuestros productos hacia la izquierda. 
select u.id, u.email, p.name from user u left join product p on u.id = p.created_by;
-- Right join nos une los datos de usuarios con nuestros productos hacia la derecha. 
select u.id, u.email, p.name from user u right join product p on u.id = p.created_by;
-- Inner join nos va a mostrar la unir entre un usuario y un producto que esten asociados.
select u.id, u.email, p.name from user u inner join product p on u.id = p.created_by;
-- cross join va a cruzar cada id con todos los productos. 
select u.id, u.email, p.id, p.name from user u cross join product p;
-- Group by va a agrupar los registros segun un pivote, por ejemplo la marca.
select count(id), marca from product group by marca; -- Count(id) tiene que estar todo unido sino no funciona. 

select count(p.id), u.name from product p left join user u
on u.id = p.created_by group by p.created_by having count(p.id) >= 1;

drop table product;

-- Esto fue copiado desde EER Diagram 
CREATE TABLE IF NOT EXISTS `mydb`.`user` (
  `id` INT NOT NULL,
  `username` VARCHAR(16) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)






