#Importamos los modulos
import ventanas
import menus
from os import system

opc_menu_cli = ""

#instaciamos un menú
menu_cliente = menus.Menu()

#Este bucle es el soporte del menú de los visitantes
while opc_menu_cli != "3":

    system("cls")

    menu_cliente.menu_clientes()
    opc_menu_cli = input("--> ")
    
#En esta opción se muestra el mapa del parque
    if opc_menu_cli == "1":
        ventana = ventanas.Ventana()
        ventana.mapa()

#En esta otra opción se muestra la guía de los dinosaurios para que los visitantes se puedan informar y guiar sobre estos
    elif opc_menu_cli == "2":
        ventana = ventanas.Ventana()
        ventana.vademecum_guias()

    