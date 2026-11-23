from datetime import datetime


RUTA_LOG = "inventario.log"

#Agrega una línea con fecha y hora al archivo de registro 
def registrar_log(nivel, mensaje):
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"{fecha_hora} | {nivel} | {mensaje}\n"
    with open(RUTA_LOG, "a", encoding="utf-8") as archivo:
        archivo.write(linea)
