from colores import mostrar_aviso, texto_encabezado_tabla, texto_separador_tabla
from base_datos import ejecutar_consulta
from colores import mostrar_titulo
from registro_log import registrar_log

# Muestra una lista de productos en formato de tabla
def mostrar_tabla(productos):
    if not productos:
        mostrar_aviso("No hay productos para mostrar.")
        return

    encabezado = f"{'ID':<5}{'NOMBRE':<22}{'CANT.':<8}{'PRECIO':<12}{'CATEGORÍA':<16}DESCRIPCIÓN"
    print(texto_encabezado_tabla(encabezado))
    print(texto_separador_tabla("-" * 85))
    for producto in productos:
        id_producto, nombre, descripcion, cantidad, precio, categoria = producto
        print(
            f"{id_producto:<5}{nombre[:20]:<22}{cantidad:<8}"
            f"${precio:<11.2f}{(categoria or '')[:14]:<16}{descripcion or ''}"
        )
    print(texto_separador_tabla("-" * 85))
    print(f"Total: {len(productos)} producto(s)")


# Muestra los productos que tienen 5 unidades o menos
def reporte_de_stock_bajo():
    mostrar_titulo("REPORTE DE STOCK BAJO")
    productos = ejecutar_consulta(
        "SELECT * FROM productos WHERE cantidad <= ? ORDER BY cantidad, id",
        (5,),
        traer_datos=True,
    )
    mostrar_tabla(productos)
    registrar_log("INFO", "Se consultó el reporte de stock bajo.")
