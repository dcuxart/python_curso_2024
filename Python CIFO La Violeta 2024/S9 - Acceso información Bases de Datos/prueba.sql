drop database if exists prueba;
create database prueba; -- Crea la base de datos "prueba"
use prueba; -- Selecciona la base de datos "prueba"

-- Creamos la tabla mis_datos
create table mis_datos(
    -- campo id (llave primeria): campo con valor único
    -- se incrementa automáticamente 1, 2, 3, 4, 5, 6...
    id int primary key auto_increment,
    dato varchar(255) -- cadena de caracteres de contenido variable
);