from os import system
from sty import fg

class Menu():

    def menu_principal(self):
        '''Menu principal'''
        system("cls")
        print(fg(41) + "\033[4m" + "MENÚ PRINCIPAL" + "\033[0m")
        print(fg(121) + "1. Gestor de empleados")
        print(fg(121) + "2. Gestor de visitantes")
        print(fg(121) + "3. Gestor de las instalaciones")
        print(fg(160) + "4. Salir" + fg.rs)

    def menu_gestor_empleados(self):
        '''Menu gestor de empleados'''
        system("cls")
        print(fg(41) + "\033[4m" + "GESTOR DE EMPLEADOS " + "\033[0m")
        print(fg(121) + "1. Registro de nuevo empleado")
        print(fg(121) + "2. Ver Empleados")
        print(fg(121) + "3. Modificar empleado")
        print(fg(121) + "4. Consultar Empleado")
        print(fg(121) + "5. Eliminar Empleado")
        print(fg(121) + "6. Horario de empleados")
        print(fg(121) + "7. Consultar horario")
        print(fg(160) + "Pulsa ENTER para volver al menú principal" + fg.rs)

    def menu_gestor_visitantes(self):
        '''Menu gestor de visitantes'''
        system("cls")
        print(fg(41) + "\033[4m" + "GESTOR DE VISITANTES" + "\033[0m")
        print(fg(121) + "1. Registro de nuevo cliente")
        print(fg(121) + "2. Consultar clientes")
        print(fg(121) + "3. Informe del día")          
        print(fg(160) + "Pulsa ENTER para volver al menú principal" + fg.rs)

    def menu_gestor_instalaciones(self):
        '''Menu para gestionar las alertas'''
        system("cls")
        print(fg(41) + "\033[4m" + "GESTOR DE INSTALACIONES" + "\033[0m")
        print(fg(121) + "1. Registrar alerta")
        print(fg(121) + "2. Consultar alertas")
        print(fg(121) + "3. Finalizar alertas")
        print(fg(160) + "Pulsa ENTER para volver al menú principal" + fg.rs)
        
    def menu_clientes(self):
        '''Menu para los clientes'''
        system("cls")
        print(fg(41) + "\033[4m" + "BIENVENIDO A JURASSIC PARK" + "\033[0m")
        print(fg(121) + "1. Consultar mapa")
        print(fg(121) + "2. Guía de dinosaurios")
        print(fg(160) + "3. Salir" + fg.rs)


