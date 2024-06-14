#Importamos los modulos
from prettytable import PrettyTable
import sqlite3
import os

class BaseDatos:

    def __init__(self) -> None:
        '''Conectamos con la ase de datos'''
        
        self.conn = sqlite3.connect("G:\\Mi unidad\\DAW\\Ejercicios clase\\Programación\\Proyectos\\Proyecto Jurassic Park\\Code\\databases\\tablas.db")

        # Ruta relativa al archivo MP3 desde el script Python
        ruta_archivo = os.path.join('databases\\tablas.db')

        # Ruta absoluta del directorio donde se encuentra el script Python
        ruta_script = os.path.dirname(os.path.abspath(__file__))

        # Ruta absoluta del archivo MP3
        ruta_absoluta = os.path.join(ruta_script, ruta_archivo)

        self.conn = sqlite3.connect(ruta_absoluta)

        self.cursor = self.conn.cursor()


    def crea_tabla(self):
        '''Creamos la tabla'''

        sql_empleados = '''create table if not exists empleados(
        idn int, 
        nombre char(20), 
        apellidos char(40), 
        dni char(9), 
        puesto char(20), 
        salario int
        )'''

        sql_visitantes = '''create table if not exists visitantes(
        ID_visitante int, 
        nombre char(20), 
        apellidos char(40), 
        DNI char(20), 
        edad int, 
        tipo_entrada char(1), 
        precio int
        )'''

        sql_instalaciones = '''create table if not exists instalaciones(
        ID_alerta int,
        Zona int,
        Factor char(40),
        Estado char (20),
        Fecha char(20),
        Comentario char (100)
        )'''


        self.cursor.execute(sql_empleados)
        self.cursor.execute(sql_visitantes)
        self.cursor.execute(sql_instalaciones)

        self.conn.commit()




    def almacena_info(self, opc_menu, *atributos):
        '''Guardamos la información en la base de datos'''

        nuevo_registro  = (atributos)

        if opc_menu == "1":
            self.cursor.execute("insert into empleados (ID_empleado, nombre, apellidos, DNI, puesto, salario) values (?, ?, ?, ?, ?, ?)", nuevo_registro)
        
        elif opc_menu == "2":
            self.cursor.execute("insert into visitantes (ID_visitante, nombre, apellidos, DNI, edad, tipo_entrada, precio) values (?, ?, ?, ?, ?, ?, ?)", nuevo_registro)

        elif opc_menu == "3":
            self.cursor.execute("insert into instalaciones (ID_alerta, Zona, Factor, Estado, Fecha, Comentario) values (?, ?, ?, ?, ?, ?)", nuevo_registro)




    def busca_info(self,id):
        '''busca la información'''

        self.cursor.execute(f"select * from empleados where ID_empleado = {id}")
        muestra_busqueda = self.cursor.fetchone()
        for datos in muestra_busqueda:
            print(datos, end= "  |  ")
        print("")
        input("Pulsa Enter para continuar")




    def elimina_info(self, opc_menu, id):
        '''elimina la información'''

        try: 
            if opc_menu == "1":
                self.cursor.execute(f"delete from empleados where ID_empleado = {id}")

                #En el caso de que no haya ningun registro
                if self.cursor.rowcount == 0:
                    print("Este registro no existe")
                    input("Pulsa Enter para continuar")

                else:
                    print("¡Genial!, se ha eliminado correctamente el registro")
                    input("Pulsa Enter para continuar")
            
            elif opc_menu == "3":
                self.cursor.execute(f"delete from instalaciones where ID_alerta = {id}")
                print("¡Genial!, se ha eliminado correctamente el registro")
                input("Pulsa Enter para continuar")

        except:
            print("Lo siento pero la información que deseas eliminar no está registrada")
            input("Pulsa Enter para continuar")        




    def modif_info(self, id):
        '''Modifica la información'''


        self.cursor.execute(f"select * from empleados where ID_empleado = {id}")
        print("Introduce que es lo que quieres cambiar:")
        print("1. Nombre")
        print("2. Apellidos")
        print("3. DNI")
        print("4. Puesto")
        print("5. Salario")
        atributos = ("ID_empleado", "Nombre", "Apellidos", "DNI", "Puesto, Salario")
        atributo = input("--> ")
        nuevo_valor = input(f"Introduce el nuevo {atributos[int(atributo)]} del empleado: ")
        nuevo_valor = nuevo_valor
        self.cursor.execute(f"update empleados set {atributos[int(atributo)]} = '{nuevo_valor}' where ID_empleado = {id}")
        print("¡Genial!, se ha modificado correctamente el registro")
        input("Pulsa Enter para continuar")


        





class Tablas:

    def __init__(self) -> None:
        '''Creamos una tabla en la interfaz de pyhton para dar una interfaz más amigable al usuario'''

        #En el constructor creamos la tabla 
        self.tabla = PrettyTable()
        self.tabla.clear_rows()

    def muestra_tabla(self, base_datos, campo):
        '''Mostramos la tabla'''
        base_datos.cursor.execute(f"select * from {campo}")
        rows = base_datos.cursor.fetchall()


        for row in rows:
            self.tabla.add_row(row)

        print(self.tabla)
        input()




    def tabla_empleados(self, base_datos):
        '''Tabla de empleados'''


        #Definimos el nombre de las columnas
        self.tabla.field_names = ["ID Empleado", "Nombre", "Apellidos", "DNI", "Puesto", "Salario"]

        self.muestra_tabla(base_datos, "empleados")




    def tabla_visitantes(self, base_datos):
        '''Tabla de visitantes o clientes'''


        self.tabla.field_names = ["ID Visitante", "Nombre", "Apellidos", "DNI", "Edad", "Tipo de entrada", "precio"]


        self.muestra_tabla(base_datos, "visitantes")




    def tabla_instalaciones(self, base_datos):
        '''Tabla de las instalaciones para guardar las alertas'''


        self.tabla.field_names = ["ID Alerta", "Zona", "Factor", "Estado", "Ultima actualización", "Comentario"]

        self.muestra_tabla(base_datos, "instalaciones")



    def informe(self, base_datos):
        '''Informe que informa sobre la cantidad de entradas que se han vendido de cada tipo en función de los números de visitantes que ha tenido el parque ese día y la cantidad de ingresos que se han generado'''

        self.tabla.field_names = ["Tipo de entrada", "Número Visitantes", "Ingresos"]

        base_datos.cursor.execute("select tipo_entrada, count(ID_visitante) as numero_clientes, sum(precio) as ingresos from visitantes group by tipo_entrada")
        rows = base_datos.cursor.fetchall()


        for row in rows:
            self.tabla.add_row(row)

        print(self.tabla)

        base_datos.cursor.execute("select count(ID_visitante) from visitantes")
        total_clientes = base_datos.cursor.fetchone()
        for row in total_clientes:
            total_clientes = row
        
        base_datos.cursor.execute("select sum(precio) from visitantes")
        total_ingresos = base_datos.cursor.fetchone()
        for row in total_ingresos:
            total_ingresos = row



        print("El número de clientes que ham visitando hoy el parque ha sido:", total_clientes, "clientes")
        print("El ingreso total de hoy ha sido:", total_ingresos, "€")
        input()








class Horario(Tablas):
    '''Esta es una base de datos 100% casera'''
    def __init__(self, lista_empleados) -> None:
        
        super().__init__()
        print("HORARIO")
        print("")

        #filas
        self.horas = [10, 12, 14, 16, 18, 20, 22]

        #columnas
        self.lista_empleados = lista_empleados

        #Tabla horario
        self.tabla_horario = []

        #Rellenamos la fila principal (Nombres de los empleados)
        self.fila_nom_emple = ["Horas"]

        #Donde se van a guardar las tareas
        self.matriz_tareas = []

        def crea_tabla_horario():

            for empleado in self.lista_empleados:
                self.fila_nom_emple.append(empleado.nombre)
            
            self.tabla.field_names = self.fila_nom_emple


            #Rellenamos la columnna principal (Horas)
            for i in range(len(self.horas)):
                franja = f"{str(self.horas[i-1])}:00 - {str(self.horas[i])}:00"
                self.tabla.add_row([franja])


        self.tabla_vacia = crea_tabla_horario





    def crea_horario(self):

        self.matriz_tareas = []
        
#esto se puede poner solo una vez arriba
        for empleado in self.lista_empleados:
            self.fila_nom_emple.append(empleado.nombre)

        self.tabla.field_names = self.fila_nom_emple


        for i in range(1, len(self.horas)):
            lista_tareas = []
            franja = f"{str(self.horas[i-1])}:00 - {str(self.horas[i])}:00"
            lista_tareas.append(franja)

            for empleado in self.lista_empleados:
                
                print(f"Escribe la tarea de {empleado.nombre} en la franja de {franja}")
                tarea = input("--> ")
                lista_tareas.append(tarea)

            self.tabla.add_row(lista_tareas)
            self.matriz_tareas.append(lista_tareas)
                
        


    def consultar_horario(self):

        print(self.tabla)
        input()

