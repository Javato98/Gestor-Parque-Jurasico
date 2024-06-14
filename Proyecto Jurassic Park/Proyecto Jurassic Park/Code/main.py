#importamos las librerías necesarias
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import subprocess
import mi_music

#Cremaos una ventana principal
root = Tk()

#Les damos unas características
root.geometry("1200x900")
root.title("Jurasic Park Soft")
root.configure(bg="beige")


def abre_menu_empleado():
    # Cerrar la ventana de inicio de sesión
    root.destroy()
    
    # Ejecutar el programa principal
    subprocess.run(['python', 'G:\\Mi unidad\\DAW\\Ejercicios clase\\Programación\\Proyectos\\Proyecto Jurassic Park\\Code\\Jurassic Park.py'])
    


def abre_menu_cliente():
    root.destroy()

    subprocess.run(['python', 'G:\\Mi unidad\\DAW\\Ejercicios clase\\Programación\\Proyectos\\Proyecto Jurassic Park\\Code\\cliente_app.py'])




def login_empleado():
    # Obtener los datos del usuario
    username = entry_nom_trab.get()
    password = entry_cont_trab.get()

    
    # Conectar a la base de datos
    conn = sqlite3.connect('G:\\Mi unidad\\DAW\\Ejercicios clase\\Programación\\Proyectos\\Proyecto Jurassic Park\\Code\\databases\\usuarios.db')
    cursor = conn.cursor()

    cursor.execute('''create table if not exists usuarios(
    usuario char(20),
    contraseña char(20)
    )''')

    cursor.execute("insert into usuarios (usuario, contraseña) values ('Javi', 'javato98')")
    cursor.execute("insert into usuarios (usuario, contraseña) values ('Homero', 'Homero123')")
    cursor.execute("insert into usuarios (usuario, contraseña) values ('Julio', '87644')")

    
    # Verificar si el usuario y la contraseña están en la base de datos
    cursor.execute(f"SELECT * FROM usuarios WHERE usuario = '{username}' AND contraseña = '{password}'")

    if cursor.fetchone():
        # Si las credenciales son válidas, abrir el menú principal
        abre_menu_empleado()

    else:
        # Si las credenciales son incorrectas, mostrar un mensaje de error
        label_error.config(text="Nombre de usuario o contraseña incorrectos")



#Metemos la música
musica = mi_music.music('music_login.mp3')

frame_img = Frame(root, width = 900, height = 800, background = "beige")
frame_img.pack()



# Carga la imagen de fondo
image_path_intro = "G:\\Mi unidad\\DAW\\Ejercicios clase\\Programación\\Proyectos\\Proyecto Jurassic Park\\Code\\images\\fondo_root2.png"  # Cambia esta ruta por la ruta de tu imagen
image_intro = Image.open(image_path_intro)
image_intro = image_intro.resize((900, 800), Image.Resampling.BILINEAR)
photo = ImageTk.PhotoImage(image_intro)  # Usa ImageTk.PhotoImage para convertir la imagen en un formato adecuado para tkinter

# Muestra la imagen en el Label
label_img = Label(frame_img, image=photo, background="beige")
label_img.pack()
label_img = photo

#Creamos un frame para el usuario y la contraseña
frame_formulario = Frame(root, bg="#67604F")
y=(root.winfo_height())
frame_formulario.place(relx=0.5, y=y + 650, anchor='n')

lab_nom_trab = Label(frame_formulario, text="Nombre usuario", bg="#67604F", fg="beige")
lab_cont_trab = Label(frame_formulario, text="Contraseña", bg="#67604F", fg="beige")

entry_nom_trab = Entry(frame_formulario, bg="beige", background="#A5F5D5")
entry_cont_trab = Entry(frame_formulario, bg="beige", show="*", background="#A5F5D5")

lab_nom_trab.pack(anchor="w", padx=10, pady=5)
entry_nom_trab.pack(anchor="w", padx=10, pady=5)
lab_cont_trab.pack(anchor="w", padx=10, pady=5)
entry_cont_trab.pack(anchor="w", padx=10, pady=10)

button_login = Button(frame_formulario, text="Iniciar Sesión", command = login_empleado, background="#9F76B3")
button_login.pack()

# Etiqueta para mostrar mensajes de error
label_error = Label(frame_formulario, fg="red", background="#67604F")
label_error.pack()

frame_client = Frame(root, background="beige")
y=(root.winfo_height())
frame_client.place(relx=0.5, y=y + 850, anchor='n')


button_client = Button(frame_client, text="Pincha aquí si eres cliente del parque", background="#9767B8", command=abre_menu_cliente)
button_client.pack(anchor="w", padx=10, pady=5)

root.mainloop()
