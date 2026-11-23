from base_datos import ejecutar_consulta
from colores import mostrar_aviso, mostrar_error, mostrar_exito, mostrar_titulo
from registro_log import registrar_log
from reportes import mostrar_tabla
from validaciones import confirmar, pedir_decimal, pedir_entero, pedir_texto

# LÓGICA DE CRUD

# Busca y devuelve un producto a partir de su id
def obtener_producto_por_id(id_producto):
    resultado = ejecutar_consulta(
        "SELECT * FROM productos WHERE id = ?", (id_producto,), traer_datos=True
    )
    return resultado[0] if resultado else None


def registrar_producto():
    mostrar_titulo("REGISTRAR PRODUCTO")
    nombre = pedir_texto("Nombre")
    descripcion = pedir_texto("Descripción (opcional)", obligatorio=False)
    cantidad = pedir_entero("Cantidad")
    precio = pedir_decimal("Precio")
    categoria = pedir_texto("Categoría (opcional)", obligatorio=False)

    sql = """
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
    """
    filas = ejecutar_consulta(sql, (nombre, descripcion, cantidad, precio, categoria))
    if filas > 0:
        mostrar_exito(f"Producto '{nombre}' registrado correctamente.")
        registrar_log("INFO", f"Producto registrado: {nombre} (cant: {cantidad}, precio: {precio})")


def ver_productos():
    mostrar_titulo("LISTADO DE PRODUCTOS")
    productos = ejecutar_consulta("SELECT * FROM productos ORDER BY id", traer_datos=True)
    mostrar_tabla(productos)
    registrar_log("INFO", "Se consultó el listado de productos.")


def buscar_producto():
    mostrar_titulo("BUSCAR PRODUCTO")
    nombre = pedir_texto("Nombre del producto a buscar")
    productos = ejecutar_consulta(
        "SELECT * FROM productos WHERE nombre LIKE ? ORDER BY id",
        (f"%{nombre}%",),
        traer_datos=True,
    )
    mostrar_tabla(productos)
    registrar_log("INFO", f"Se buscó el producto: {nombre}")


def actualizar_producto():
    mostrar_titulo("ACTUALIZAR PRODUCTO")
    productos = ejecutar_consulta("SELECT * FROM productos ORDER BY id", traer_datos=True)

    if not productos:
        mostrar_tabla(productos)
        return

    mostrar_aviso("Elegí el ID del producto que querés actualizar.")
    mostrar_tabla(productos)
    id_producto = pedir_entero("ID del producto a actualizar")
    producto = obtener_producto_por_id(id_producto)

    if producto is None:
        mostrar_error(f"No existe un producto con ID {id_producto}.")
        return

    _, nombre, descripcion, cantidad, precio, categoria = producto
    mostrar_aviso("Presioná Enter para mantener el valor actual.")
    nuevo_nombre = pedir_texto("Nombre", actual=nombre)
    nueva_descripcion = pedir_texto("Descripción", actual=descripcion or "")
    nueva_cantidad = pedir_entero("Cantidad", actual=cantidad)
    nuevo_precio = pedir_decimal("Precio", actual=precio)
    nueva_categoria = pedir_texto("Categoría", actual=categoria or "")

    sql = """
        UPDATE productos
        SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
        WHERE id = ?
    """
    filas = ejecutar_consulta(
        sql,
        (nuevo_nombre, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_categoria, id_producto),
    )
    if filas > 0:
        mostrar_exito("Producto actualizado correctamente.")
        registrar_log("INFO", f"Producto actualizado: ID {id_producto} ({nuevo_nombre})")


def eliminar_producto():
    mostrar_titulo("ELIMINAR PRODUCTO")
    productos = ejecutar_consulta("SELECT * FROM productos ORDER BY id", traer_datos=True)

    if not productos:
        mostrar_tabla(productos)
        return

    mostrar_aviso("Elegí el ID del producto que querés eliminar.")
    mostrar_tabla(productos)
    id_producto = pedir_entero("ID del producto a eliminar")
    producto = obtener_producto_por_id(id_producto)

    if producto is None:
        mostrar_error(f"No existe un producto con ID {id_producto}.")
        return

    mostrar_tabla([producto])
    if not confirmar("¿Seguro que querés eliminarlo?"):
        mostrar_aviso("Eliminación cancelada.")
        return

    filas = ejecutar_consulta("DELETE FROM productos WHERE id = ?", (id_producto,))
    if filas > 0:
        mostrar_exito("Producto eliminado correctamente.")
        registrar_log("WARNING", f"Producto eliminado: ID {id_producto} ({producto[1]})")
