#Cremaos los visitantes con sus respectivas propiedades 
class Visitantes:
    def __init__(self, id_visitante, nombre_visitante, apellidos_visitante, dni_visitante, edad, tipo_entrada, precio) -> None:
        self.id_visitante = id_visitante
        self.nombre_visitante = nombre_visitante
        self.apellidos_visitante = apellidos_visitante
        self.dni_visitante = dni_visitante
        self.edad = edad
        self.tipo_entrada = tipo_entrada
        self.precio = precio

class GestorVisitantes():
    '''Gestiaamos los registros y las consultas de los vsitantes, esto se usó al principio pero fue sustituido por las bases de datos que eran más eficientes'''

    def __init__(self) -> None:
        self.visitantes = []

    def registro_visit(self, id_visitante, nombre_visitante, apellidos_visitante, dni_visitante, edad, tipo_entrada, precio):
        new_visitantes = Visitantes(id_visitante, nombre_visitante, apellidos_visitante, dni_visitante, edad, tipo_entrada, precio)
        self.visitantes.append(new_visitantes)

    def consultar_visit(self):
        for visitante in self.visitantes:
            print(visitante)