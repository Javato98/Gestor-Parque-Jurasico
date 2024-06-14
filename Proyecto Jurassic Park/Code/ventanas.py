#Importamos los modulos
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
import mi_music
import os

class Ventana:



    def ruta_absoluta(self, foto, tipo_imagen='dinosaurios'):


        # Ruta relativa al archivo MP3 desde el script Python
        ruta_archivo = os.path.join(f'images\\{tipo_imagen}\\{foto}')

        # Ruta absoluta del directorio donde se encuentra el script Python
        ruta_script = os.path.dirname(os.path.abspath(__file__))

        # Ruta absoluta del archivo jpg
        ruta_absoluta = os.path.join(ruta_script, ruta_archivo)

        return ruta_absoluta




    def mapa(self):
        '''Mapa para los visitantes'''

        self.root = Tk()
        self.root.config(width = 900, height = 600, background = "beige")
        self.miframe = Frame(self.root, width=300, height=200, background="beige")
        self.miframe.pack()

        

        #Metemos la música
        musica = mi_music

        cancion = musica.music('music_mapa.mp3')

        fuente_mapa = font.Font(family="Sitka Display", size=36)

        image_path_mapa = self.ruta_absoluta('mapa_guia.jpg', 'mapas')

        image_mapa = Image.open(image_path_mapa)
        image_mapa = image_mapa.resize((450, 600), Image.Resampling.BILINEAR)
        photo = ImageTk.PhotoImage(image_mapa)  # Usa ImageTk.PhotoImage para convertir la imagen en un formato adecuado para tkinter

        image_path_leyenda = self.ruta_absoluta('leyenda_mapa.jpg', 'mapas')

        image_leyenda = Image.open(image_path_leyenda)
        image_leyenda = ImageTk.PhotoImage(image_leyenda)

        
        # Crea un Label para mostrar la imagen
        label_mapa = Label(self.miframe, image=photo)
        label_mapa.grid(row = 1, column=1, sticky='nsew') #Posicionamos el label
        label_mapa.image = photo  # Guarda una referencia a la imagen para evitar que se recoja 


        label_leyenda = Label(self.miframe, image=image_leyenda)
        label_leyenda.grid(row=0, rowspan=2, column=0, sticky='nsew')
        label_leyenda.image = image_leyenda

        label_titulo = Label(self.miframe, text="Mapa Parque Jurásico", font=fuente_mapa, fg="red", background="beige")
        label_titulo.grid(row=0, column=1)

        label_mapa.config(background="beige")
        self.root.mainloop()

        musica.pygame.mixer.music.stop()

    
    def vademecum_guias(self):
        '''Guia de los dinosaurios para los visitantes'''

        self.root = Tk()
        self.root.config(width = 900, height = 600, background = "beige")
        self.miframe = Frame(self.root, width=300, height=200, background="beige")
        self.miframe.pack()

        #Metemos la música
        musica = mi_music

        cancion = musica.music('music_guia.mp3')


        def crea_imagen(image_path):
            var_image = Image.open(image_path)
            var_image = var_image.resize((275, 275), Image.Resampling.BILINEAR)
            photo = ImageTk.PhotoImage(var_image)
            return photo
        


        image_path_brachio = self.ruta_absoluta('brachiosaurus.jpeg')

        image_path_galli = self.ruta_absoluta('Gallimimus.jpeg')

        image_path_trice = self.ruta_absoluta('Triceratops.jpg')

        image_path_tyra = self.ruta_absoluta('Tyrannosaurus.jpeg')

        image_path_velo = self.ruta_absoluta('Velociraptor.jpeg')

        image_path_ptera = self.ruta_absoluta('Pteranodon.jpeg')

        photo_brachio = crea_imagen(image_path_brachio)

        photo_galli = crea_imagen(image_path_galli)

        photo_trice = crea_imagen(image_path_trice)

        photo_tyra = crea_imagen(image_path_tyra)

        photo_velo = crea_imagen(image_path_velo)

        photo_ptera = crea_imagen(image_path_ptera)


#brachiosaurus
        label_img_brachio = Label(self.miframe, image=photo_brachio)
        label_img_brachio.grid(row=0, column=1)

        label_text_brachio = Label(self.miframe, text="BRACHIOSAURUS \n\nEra:\n Jurásico tardío, hace 156 millones de años \n\n ¿Dónde vivió?\nUSA(Colorado) , África(Tanzania), y Europa(Portugal)\n\n Descripción: \nSu nombre significa lagarto brazo de tórax profundo. \nFue uno de los dinosaurios más altos y más grandes. \nCon sus enormes patas delanteras y su larguísimo cuello,\n podía alimentarse a mayor altura que casi todos los demás dinosaurios. \nTenía un cráneo grande del que sobresalía un gran bulto. \nEsta característica barra ósea en medio de la frente \nservía para separar los dos orificios nasales.", background= "beige")
        label_text_brachio.grid(row=0, column=0)



#Gallimimus
        label_img_galli = Label(self.miframe, image=photo_galli)
        label_img_galli.grid(row=1, column=1)

        label_text_galli = Label(self.miframe, text="GALLIMIMUS\n\nEra:\n Cretácico superior, hace entre 145 y 66 millones de años  \n\n ¿Dónde vivió?\nMongolia  \n\n Descripción:\n Su nombre significa imitadores de gallina. \n Debido a su constitución ligera y sus largas patas traseras, \nestaba adaptado para la carrera, ¡era su gran baza para escapar de los depredadores! \nSu aspecto recuerda al de un avestruz dado su largo cuello y su pico sin dientes. \nContaba con pequeñas manos con tres garras curvas, \nlas cuales le servían para rastrillar el suelo en busca de comida.\n", background= "beige")
        label_text_galli.grid(row=1, column=0)


#Triceratops
        label_img_trice = Label(self.miframe, image=photo_trice)
        label_img_trice.grid(row=2, column=1)

        label_text_trice = Label(self.miframe, text="TRICERATOPS\n\nEra:\n Cretácico tardío, hace 65 millones de años \n\n ¿Dónde vivió?\n Colorado, Montana, Dakota del Sur,\n Wyoming, Alberta, Saskatchewan (America del Norte) \n\n Descripción: \nSu nombre significa cara de tres cuernos. \nA pesar de las apariencias, el Triceratops no era un gigante amable \nque se alimentaba de plantas. Muchos registros fósiles muestran daños en los huesos \ndebido a combates con rivales o depredadores. La gola del cuello le ofrecía cierta \nprotección contra las mordeduras de depredadores (como la del Tyrannosaurus Rex) \ny le ayudaba a regular la temperatura corporal.", background= "beige")
        label_text_trice.grid(row=2, column=0)





#Tirannosaurus
        label_img_tyra = Label(self.miframe, image=photo_tyra)
        label_img_tyra.grid(row=0, column=3)

        label_text_tyra = Label(self.miframe, text="TYRANNOSAURUS REX\n\nEra:\n Cretácico tardío, hace 65 millones de años  \n\n ¿Dónde vivió?\n Colorado, Montana, Nuevo México, Wyoming, Alberta \n\n Descripción: \nSu nombre significa rey de los lagartos tiranos. Siendo uno de los mayores \ncarnívoros terrestres que ha existido, era un depredador ágil y feroz, con un olfato muy \ndesarrollado, un oído agudo, un cerebro grande y una mordida extraordinariamente \npotente (contaba con la potencia necesaria para aplastar un coche). \nPodía astillar huesos y aplastar con su mandíbula tanto a la presa como a \ncombatientes de su propia especie.", background= "beige")
        label_text_tyra.grid(row=0, column=4)


#Velociraptor

        label_img_velo = Label(self.miframe, image=photo_velo)
        label_img_velo.grid(row=1, column=3)

        label_text_velo = Label(self.miframe, text="VELOCIRAPTOR\n\nEra:\n Cretácico superior, hace 75 millones de años \n\n ¿Dónde vivió?\n Mongolia \n\n Descripción: \nSu nombre significa ladrón veloz. \nEl Velociraptor era más pequeño que su representación en la cultura popular, \npero aún así era un cazador temible y veloz. Las protuberancias típicas de la inserción \nde plumas presentes en huesos del brazo confirman que las tenía. Probablemente era \nde sangre caliente, y tenía un pelaje suave para retener el calor y \nproporcionar energía para cazar.", background= "beige")
        label_text_velo.grid(row=1, column=4)


#Pteranodon

        label_img_ptera = Label(self.miframe, image=photo_ptera)
        label_img_ptera.grid(row=2, column=3)

        label_text_ptera = Label(self.miframe, text="PETERANODON\n\nEra:\n Cretácico tardío, hace 60 millones de años \n\n ¿Dónde vivió?\n Kansas e Inglaterra \n\n Descripción: \nSu nombre significa alado y desdentado.\n Sobrevoló los mares poco profundos de América del Norte. \nEra un reptil volador que vivió durante la época de los dinosaurios. No era un dinosaurio, \nsino un pariente cercano. Pudo planear sobre el océano en grandes bandadas, \nbuscando peces en aguas superficiales. Su cresta pudo servirle para atraer pareja \no como timón para maniobrar en vuelo.", background= "beige")
        label_text_ptera.grid(row=2, column=4)





        self.root.mainloop()

        musica.pygame.mixer.music.stop()



ventana = Ventana()


