from colores import mostrar_error

#VALIDACIONES
def pedir_texto(mensaje, obligatorio=True, actual=None):
    while True:
        if actual is not None:
            texto = input(f"{mensaje} [{actual}]: ").strip()
            if texto == "":
                return actual
            return texto
        texto = input(f"{mensaje}: ").strip()
        if texto == "" and obligatorio:
            mostrar_error("Este campo no puede estar vacío.")
            continue
        return texto


def pedir_entero(mensaje, actual=None):
    while True:
        if actual is not None:
            texto = input(f"{mensaje} [{actual}]: ").strip()
            if texto == "":
                return actual
        else:
            texto = input(f"{mensaje}: ").strip()
        try:
            numero = int(texto)
            if numero < 0:
                mostrar_error("El número no puede ser negativo.")
                continue
            return numero
        except ValueError:
            mostrar_error("Ingresá un número entero válido (ej: 10).")


def pedir_decimal(mensaje, actual=None):
    while True:
        if actual is not None:
            texto = input(f"{mensaje} [{actual}]: ").strip()
            if texto == "":
                return actual
        else:
            texto = input(f"{mensaje}: ").strip()
        try:
            numero = float(texto.replace(",", "."))
            if numero < 0:
                mostrar_error("El número no puede ser negativo.")
                continue
            return numero
        except ValueError:
            mostrar_error("Ingresá un número válido (ej: 1500.50).")


def confirmar(mensaje):
    respuesta = input(f"{mensaje} (s/n): ").strip().lower()
    return respuesta == "s"
