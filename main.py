from base_datos import crear_tabla
from colores import mostrar_despedida, mostrar_error
from menu import mostrar_menu
from productos import actualizar_producto, buscar_producto, eliminar_producto, registrar_producto, ver_productos
from registro_log import registrar_log
from reportes import reporte_de_stock_bajo


def main():
    crear_tabla()
    acciones = {
        "1": registrar_producto,
        "2": ver_productos,
        "3": actualizar_producto,
        "4": eliminar_producto,
        "5": buscar_producto,
        "6": reporte_de_stock_bajo,
    }

    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ").strip()

        if opcion == "0":
            registrar_log("INFO", "Programa finalizado.")
            mostrar_despedida()
            break
        if opcion in acciones:
            acciones[opcion]()
        else:
            mostrar_error("Opción inválida. Probá de nuevo.")


if __name__ == "__main__":
    main()
