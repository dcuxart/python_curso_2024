drop database if exists apirest;
create database apirest;
use apirest;

create table doctores(
    id int primary key auto_increment,
    colegiado char(9),
    nombre varchar(255),
    especialidad varchar(255),
    password varchar(255)
);

create table pacientes(
    id int not null primary key auto_increment,
    dni char(9),
    nombre varchar(50) not null,
    apellido varchar(50) not null,
    email varchar(50) not null
);

create table citas(
    id int not null primary key auto_increment,
    id_doctor int not null,
    id_paciente int not null,
    fecha_cita date not null,
    foreign key (id_doctor) references doctores(id),
    foreign key (id_paciente) references pacientes(id)
);