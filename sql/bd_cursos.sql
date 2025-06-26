-- Crear una bd
CREATE DATABASE bd_cursos;

-- Usar bd
USE bd_cursos;

-- Creamos las tablas
CREATE TABLE cursos (
id INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100),
duracion INT, -- horas
precio DECIMAL(10,2)
);

CREATE TABLE alumnos(
id INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100),
email VARCHAR(100)
);

CREATE TABLE inscripciones(
id INT PRIMARY KEY AUTO_INCREMENT,
alumno_id INT,
curso_id INT,
fecha_inscripcion DATE,
FOREIGN KEY (alumno_id) REFERENCES alumnos(id),
FOREIGN KEY (curso_id) REFERENCES cursos(id)
);

-- Insertartamos datos
INSERT INTO cursos (nombre, duracion, precio) VALUES
('SQL Básico', 20 , 500),
('SQL Avanzado', 30, 1000),
('Power BI',25,800),
('Python para datos', 35, 1500);

INSERT INTO alumnos (nombre, email) VALUES
('Ana Lopez', 'ana@email.com'),
('Bruno Diaz','asd@ads.com'),
('Carla Gomez','carla@gmail.com');

INSERT INTO inscripciones (alumno_id, curso_id, fecha_inscripcion) VALUES
(1,1, '2025-06-01'),
(1,3, '2025-06-01'),
(2,2, '2025-06-01'),
(3,1, '2025-06-01'),
(3,4, '2025-06-01');

-- Subconsultas 
-- Alumnos que se inscribieron en mas de un curso
SELECT nombre
FROM alumnos
WHERE id IN (
	SELECT alumno_id
	FROM inscripciones
	GROUP BY alumno_id
	HAVING COUNT(*) < 1
);

ALTER TABLE cursos ADD COLUMN vacantes_disponibles INT DEFAULT 10;