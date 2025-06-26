import mysql.connector

from config import HOST_DB, PASS_DB, USER_DB

try:
    # Conexión a la base de datos bd_cursos
    conexion = mysql.connector.connect(
        host = HOST_DB,
        user = USER_DB,
        password = PASS_DB,
        database = "bd_cursos"
    )

    cursor = conexion.cursor()

    # Consulta SQL
    # consulta = """
    # SELECT a.nombre AS Alumno, c.nombre AS Curso, i.fecha_inscripcion
    # FROM inscripciones i
    # JOIN alumnos a ON i.alumno_id = a.id
    # JOIN cursos c ON i.curso_id = c.id
    # """

    # cursor.execute(consulta)

    # insert_sql = """
    # INSERT INTO inscripciones (alumno_id, curso_id, fecha_inscripcion)
    # VALUES (%s, %s, CURDATE())
    # """
    # valores = (1,2)

    # cursor.execute(insert_sql, valores)

    # conexion.commit()
    # print("Inscripcion registrada!")

    # resultados = cursor.fetchall()

    # Mostrar los resultados en consola
    # for fila in resultados:
    #     print(f"Alumno: {fila[0]}, Curso: {fila[1]}, Fecha: {fila[2]}")

    # cursor.close()
    # conexion.close()

    cursor.execute("SELECT * FROM alumnos;")
    for fila in cursor.fetchall():
        print(fila)

except mysql.connector.Error as err:
    print("Ocurrio un error : ", err)

finally:
    if conexion.is_connected():
        cursor.close()
        conexion.close()
        print("Se cerraron las conexiones")