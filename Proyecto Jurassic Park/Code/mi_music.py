#Importamos los modulos
import pygame
import os


def music(cancion):
    # CANCIONES
    pygame.mixer.init()

    # Ruta relativa al archivo MP3 desde el script Python
    ruta_archivo_mp3 = os.path.join('music', f'{cancion}')

    # Ruta absoluta del directorio donde se encuentra el script Python
    ruta_script = os.path.dirname(os.path.abspath(__file__))

    # Ruta absoluta del archivo MP3
    ruta_absoluta_mp3 = os.path.join(ruta_script, ruta_archivo_mp3)


    #Caargamos y la ejecutamos
    pygame.mixer.music.load(ruta_absoluta_mp3)
    pygame.mixer.music.play()

