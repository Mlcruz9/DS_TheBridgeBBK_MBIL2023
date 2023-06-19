from funciones import *
from time import sleep

print('Vamos a organizar sus carpetas')

from tkinter import Tk
from tkinter.filedialog import askdirectory

# Crear una instancia de Tkinter
root = Tk()
root.withdraw()  # Ocultar la ventana principal de Tkinter

# Mostrar el cuadro de diálogo para seleccionar un directorio
path_to_organize = askdirectory()


change_working_dir(path_to_organize=path_to_organize)
create_folders()
move_dirs()

print('Las carpetas han sido organiazdas')
sleep(3)