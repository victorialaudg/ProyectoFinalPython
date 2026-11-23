import sqlite3

from colores import mostrar_error
from registro_log import registrar_log


RUTA_DB = "inventario.db"

# BASE DE DATOS 

# Ejecuta una consulta SQL y devuelve filas o la cantidad afectada
def ejecutar_consulta(sql, parametros=(), traer_datos=False):
    conexion = sqlite3.connect(RUTA_DB)
    try:
        cursor = conexion.cursor()
        cursor.execute(sql, parametros)
        if traer_datos:
            return cursor.fetchall()
        conexion.commit()
        return cursor.rowcount
    except sqlite3.Error as error:
        conexion.rollback()
        mostrar_error(f"Error en la base de datos: {error}")
        registrar_log("ERROR", f"Base de datos: {error}")
        return [] if traer_datos else 0
    finally:
        conexion.close()

# Crea la tabla de productos si todavía no existe.
def crear_tabla():
    sql = """
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
    """
    ejecutar_consulta(sql)
    registrar_log("INFO", "Programa iniciado. Tabla 'productos' verificada.")
