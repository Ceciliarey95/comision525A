CREATE DATABASE empleados_db;

USE empleados_db;

CREATE TABLE departamento (
id INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(45) NOT NULL
);

CREATE TABLE empleado (
id INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100) NOT NULL,
salario DECIMAL(10, 2),
id_departamento INT,
FOREIGN KEY (id_departamento) REFERENCES departamento(id)
);

CREATE TABLE proyecto (
id INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(255)
);

CREATE TABLE asignaciones (
id INT PRIMARY KEY AUTO_INCREMENT,
id_empleado INT,
id_proyecto INT,
FOREIGN KEY (id_empleado) REFERENCES empleado(id),
FOREIGN KEY (id_proyecto) REFERENCES proyecto(id)
);

INSERT INTO departamento (nombre) VALUES ("RRHH"),("Desarrollo"),("Ventas"),("Compras");

INSERT INTO empleado (nombre,salario,id_departamento) VALUES
("Ana Lopez", 1500 , 2),
("Juan Gomez", 2000,3),
("Carlos Perez", 1500, 2),
("Juan Mostaza",25000, 3);


INSERT INTO proyecto(nombre) VALUES ("Proyecto 1"), ("Proyecto 2") , ("Proyecto 3");

INSERT INTO asignaciones (id_empleado, id_proyecto) VALUES 
(2,1),
(3,2),
(1,1),
(4,3),
(2,3);

-- Mostrar nombre de empleado con el nombre del departamento al que pertenece
SELECT e.nombre AS NombreEmpleado , d.nombre AS NombreDPTO 
FROM empleado e
JOIN departamento d 
ON e.id_departamento = d.id;

-- Mostrar empleados del area de DESARROLLO que tengan un salario mayor a 1000
SELECT e.nombre AS Empleado, e.salario AS Salario
FROM empleado e
JOIN departamento d ON e.id_departamento = d.id
WHERE d.nombre = "Desarrollo" AND e.salario > 1000;

-- Calcular el salario promedio por departamento
SELECT d.nombre AS NombreDPTO , AVG(e.salario) AS SalarioPromedio
FROM empleado e JOIN departamento d ON e.id_departamento = d.id
GROUP BY d.nombre;

-- Mostrar departamentos donde el salario promedio es mayor a 1000
SELECT d.nombre AS NombreDPTO , AVG(e.salario) AS SalarioPromedio
FROM empleado e JOIN departamento d ON e.id_departamento = d.id
GROUP BY d.nombre
HAVING AVG(e.salario) > 1500;

-- Mostrar la sumatoria de todos los salarios
SELECT SUM(salario) AS Total
FROM empleado;