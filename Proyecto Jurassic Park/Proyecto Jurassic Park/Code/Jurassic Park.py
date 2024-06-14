#Importamos los módulos que hemos creado
import menus
import empleados 
import tablas
import visitantes

#Importamos algunos módulos de python
import sys
from os import system, name
from datetime import datetime
from prettytable import PrettyTable
import colorama 
import sty
from datetime import datetime


def clear():
    """This function will be used to clear the screen"""
    if name == 'nt':
        # If run on Windows
        system('cls')
    else:
        # If run on Linux
        system('clear')


idn = 1
id_visitante = 0
id_alerta = 0
bd = False
opc_menu_prin = 0
tipo_entrada = "x"



#Instanciamos los objetos
new_gestion_emple = empleados.GestorEmpleado()
new_gestion_visit = visitantes.GestorVisitantes()
el_menu = menus.Menu()
base_datos = tablas.BaseDatos()


#Creamos la base de datos, por si no estuviera creada
base_datos.crea_tabla()


#Bucle del programa principal de los empleados
while True:
    
    clear()
    el_menu.menu_principal()
    opc_menu_prin = input("--> ")

#opciones de empleados
    if opc_menu_prin == "1":

        clear()
        el_menu.menu_gestor_empleados()
        opc_menu_empleados = input("--> ")

        #Registro de empleados
        if opc_menu_empleados == "1":
            clear()

            idn = int(idn) + 1
            idn = str(idn)
            nombre = input("Introduce el nombre del empleado: ")
            apellidos = input("Introduce los apellidos del empleado: ")
            dni = input("Introduce el DNI del empleado: ")
            puesto = input("Introduce el puesto de trabajo del empleado: ")
            salario = input("Introduce el salario del empleado: ")

            
            new_gestion_emple.registra_empleado(idn, nombre, apellidos, dni, puesto, salario)

            base_datos.almacena_info("1", idn, nombre, apellidos, dni, puesto, salario)


        #Consulta de empleados
        elif opc_menu_empleados == "2":

            lista_empleados = new_gestion_emple.empleados
            tabla_empleado = tablas.Tablas()
            tabla_empleado.tabla_empleados(base_datos)

        #Modifica la información de los empleados
        elif opc_menu_empleados == "3":
            busca_empleado = input("Introduce el ID del empleado que quieres modificar: ")
            print("")
            try:
                base_datos.modif_info(int(busca_empleado))
            except:
                print("Lo siento pero el valor que has introducido tiene que ser un número")
                input("Pulsa ENTER para continuar")

        #Busca un empleado concreto
        elif opc_menu_empleados == "4":
            busca_empleado = input("Introduce el ID del empleado que quieres buscar: ")
            print("")
            try:
                base_datos.busca_info(int(busca_empleado))
            except:
                print("Lo siento pero el valor que has introducido tiene que ser un número")
                input("Pulsa ENTER para continuar")


        #Elimina un empleado
        elif opc_menu_empleados == "5":
            busca_empleado = input("Introduce el ID del empleado que quieres eliminar: ")
            print("")
            try:
                base_datos.elimina_info("1", int(busca_empleado))
            except:
                print("Lo siento pero el valor que has introducido tiene que ser un número")
                input("Pulsa ENTER para continuar")

        #Aquí se crea el horario
        elif opc_menu_empleados == "6":

            lista_empleados = new_gestion_emple.empleados
            tabla_horario = tablas.Horario(lista_empleados)
            tabla_horario.crea_horario()

            print("Probando consultar horario")
            tabla_horario.consultar_horario()

        #Se consulta el horario de los trabajadores
        elif opc_menu_empleados == "7":

            tabla_horario.consultar_horario()


        


        


#VISITANTES
    elif opc_menu_prin == "2":


        clear()
        el_menu.menu_gestor_visitantes()
        opc_menu_visit = input("--> ")

        #Registro de visitantes
        if opc_menu_visit == "1":
            clear()

            id_visitante = int(id_visitante) + 1  
            id_visitante = str(id_visitante)
            nombre_visitante = input("Introduce el nombre del visitante: ")
            apellidos_visitante = input("Introduce los apellidos del visitante: ")
            dni_visitante = input("Introduce el DNI del visitante: ")
            edad = input("Introduce la edad del visitante: ")
            tipo_entrada = input("Introduce el tipo de entrada del visitante: ").upper()

            while tipo_entrada != "A" and tipo_entrada != "B" and tipo_entrada != "C":

                clear()
                print("Lo siento, solamente existen los tipos de entradas 'A', 'B' o 'C'")
                print("")
                tipo_entrada = input("Introduce el tipo de entrada del visitante: ").upper()
                
            if tipo_entrada == "A":
                precio = 120

            elif tipo_entrada == "B":
                precio = 180

            elif tipo_entrada == "C":
                precio = 220

                
            new_gestion_visit.registro_visit(id_visitante, nombre_visitante, apellidos_visitante, dni_visitante, edad, tipo_entrada, precio)

            base_datos.almacena_info("2", id_visitante, nombre_visitante, apellidos_visitante, dni_visitante, edad, tipo_entrada, precio)




        #Consulta de visitantes
        elif opc_menu_visit == "2":

            lista_visitantes = new_gestion_visit.visitantes
            tabla_visitantes = tablas.Tablas()
            tabla_visitantes.tabla_visitantes(base_datos)


        elif opc_menu_visit == "3":
            print("INFORME DEL DÍA")
            print("")
            tabla_visitantes = tablas.Tablas()
            tabla_visitantes.informe(base_datos)



#MENU INSTALACIONES
    elif opc_menu_prin == "3":

        el_menu.menu_gestor_instalaciones()
        opc_menu_instalaciones = input("--> ")

    #Registro de instalciones
        if opc_menu_instalaciones == "1":

            id_alerta = int(id_alerta) + 1  
            id_alerta = str(id_alerta)

            zona = input("Introduce la zona (1-4): ")
            factor = input("Introduce el tipo de factor: ")
            estado = input("Introduce el estado del proceso ('OK', 'ALERT', 'En proceso'): ")
            comentario = input("Describe brevemente la situación: ")

            ahora = datetime.now()
            dia_formato = (f"{ahora.day}/{ahora.month}/{ahora.year}")
            hora_formato = (f"{ahora.hour}:{ahora.minute}:{ahora.second}")
            
            fecha = f"Dia: {dia_formato}\n Hora: {hora_formato}"

            base_datos.almacena_info("3", id_alerta, zona, factor, estado, fecha, comentario)



        #Muestra la tabla de las alertas
        elif opc_menu_instalaciones == "2":
            tabla_instalaciones = tablas.Tablas()
            tabla_instalaciones.tabla_instalaciones(base_datos)


        #Elimina una alerta
        elif opc_menu_instalaciones == "3":
            del_alerta = input("Introduce el ID de la alerta que quieres borrar: ")
            try:
                base_datos.elimina_info("3", int(del_alerta))
            except:
                print("Lo siento pero el valor que has introducido tiene que ser un número")
                input("Pulsa ENTER para continuar")


    #Para salir del programa, tiene la opción de guardar cambios en el caso de que se deseé esta opción, no podemos guardar los cabios si no se pasa por aquí
    elif opc_menu_prin == "4":
        print("¿Quieres guardar los cambios realizados (S/N)?").lower()
        save = input("--> ")

        if save == "s":
            base_datos.conn.commit()
            base_datos.conn.close()
            print("")
            input("Los datos se han guardado correctamente")

        sys.exit()




