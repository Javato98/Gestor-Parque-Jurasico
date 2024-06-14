from os import system


def clear():
    """This function will be used to clear the screen"""
    if name == 'nt':
        # If run on Windows
        system('cls')
    else:
        # If run on MacOS or Linux
        system('clear')


#Cremaos los empleados con sus respectivas propiedades 
class Empleados:
    def __init__(self, idn, nombre, apellidos, dni, puesto, salario) -> None:
        self.idn = idn
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.puesto = puesto
        self.salario = salario


class GestorEmpleado:
    def __init__(self) -> None:
        self.empleados = []

    def registra_empleado(self, idn, nombre, apellidos, dni, puesto, salario):
        '''Registramos los empleados'''
        nuevo_empleado = Empleados(idn, nombre, apellidos, dni, puesto, salario)
        self.empleados.append(nuevo_empleado)


    def modifica_empleado(self):
        '''modificamos la información de los empleados'''
        
        print("Introduce el ID del empleado que quieres modificar.")
        print("Si no recuerdas el ID, siempre puedes consultarlo en el menú 'GESTOR DE EMPLEADOS'")
        modif_empleado = input("--> ")

        for empleado in self.empleados:
            if modif_empleado == empleado.idn:

                for atributo, valor in vars(empleado).items():
                    print(f"{atributo}: {valor}")


                input("Pulsa ENTER para continuar")

                print("¿Qué es lo que quieres modificar del empleado?")
                print("1. Nombre")
                print("2. Apellidos")
                print("3. DNI")
                print("4. Puesto")
                print("5. Salario")
                modif_empleado = input("--> ")

                #Hay que cambiar el indice por el nombre
                if modif_empleado == "1":
                    modif = input("Introduce el nuevo nombre del empleado: ")
                    empleado.nombre = modif
                    

                elif modif_empleado == "2":
                    modif = input("Introduce el nuevo apellido del empleado: ")
                    empleado.apellidos = modif
                    
                
                elif modif_empleado == "3":
                    modif = input("Introduce el nuevo DNI del empleado: ")
                    empleado.dni = modif

                    
                elif modif_empleado == "4":
                    modif = input("Introduce el nuevo puesto del empleado: ")
                    empleado.puesto = modif
                    

                elif modif_empleado == "5":
                    modif = input("Introduce el nuevo salario del empleado: ")
                    empleado.salario = modif

