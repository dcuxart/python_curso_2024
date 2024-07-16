drop database if exists app;
create database app; -- Crea la base de datos "prueba"
use app; -- Selecciona la base de datos "prueba"

-- Creamos la tabla mis_datos
create table usuarios(
    id int primary key auto_increment,
    dni char(9),
    nombre varchar(255),
    email varchar(255),
    password varchar(255)
);

create table libros(
    id int not null primary key auto_increment,
    isbn varchar(20) not null,
    titulo varchar(50) not null,
    autor varchar(50) not null,
    genero varchar(50) not null
);

create table prestamos(
    id int not null primary key auto_increment,
    id_usuario int not null,
    id_libro int not null,
    fecha_prestamo date not null,
    foreign key (id_usuario) references usuarios(id),
    foreign key (id_libro) references libros(id)
);