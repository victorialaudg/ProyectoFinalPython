from colorama import Fore, Style, init


init(autoreset=True) #reinicia los colores de Colorama dspués de c/print 

#MENSAJES EN COLORAMA
def mostrar_exito(texto):
    print(Fore.GREEN + f"[OK] {texto}")


def mostrar_error(texto):
    print(Fore.RED + f"[ERROR] {texto}")


def mostrar_aviso(texto):
    print(Fore.YELLOW + f"[AVISO] {texto}")


def mostrar_titulo(texto):
    print()
    print(Fore.CYAN + Style.BRIGHT + f"=== {texto} ===")


def texto_menu(texto):
    return Fore.MAGENTA + Style.BRIGHT + texto


def texto_encabezado_tabla(texto):
    return Fore.CYAN + Style.BRIGHT + texto


def texto_separador_tabla(texto):
    return Fore.CYAN + texto


def mostrar_despedida():
    print(Fore.CYAN + "¡Hasta luego!")
