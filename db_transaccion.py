import mysql.connector
from mysql.connector import Error

from config import HOST_DB, PASS_DB, USER_DB


def inscribir_alumno(alumno_id, curso_id):
    try:
        # Conexión a la base de datos bd_cursos
        conexion = mysql.connector.connect(
            host = HOST_DB,
            user = USER_DB,
            password = PASS_DB,
            database = "bd_cursos"
        )

        if conexion.is_connected():
            print("Conexión creada exitosamente!")

            cursor = conexion.cursor()

            #Iniciamos una transaccion
            conexion.start_transaction()

            cursor.execute(
                """
                SELECT vacantes_disponibles
                FROM cursos 
                WHERE id = %s
                FOR UPDATE
                """, (curso_id,)
            )
            resultado = cursor.fetchone()

            if not resultado:
                print("El curso no existe")
                conexion.rollback()
                return
            
            vacantes = resultado[0]
            print(f"Vacantes disponibles: {vacantes}")

            if vacantes > 0:
                #Actualizacion de curso
                cursor.execute(
                    """
                    UPDATE cursos
                    SET vacantes_disponibles = vacantes_disponibles - 1
                    WHERE id = %s
                    """, (curso_id,)
                )

                cursor.execute(
                    """
                    INSERT INTO inscripciones (alumno_id, curso_id,fecha_inscripcion)
                    VALUES (%s,%s, CURDATE())
                    """, (alumno_id, curso_id)
                    )

                conexion.commit()
                print("Inscripcion realizada y vacante descontada")
            else:
                print("No hay vacantes para el curso")
                conexion.rollback()
    except Error as e:
        print("Error durante la transaccion: ", e)
        conexion.rollback()
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Se cerraron las conexiones")

inscribir_alumno(alumno_id=2, curso_id=3)