import os
import shutil
from variables import *

def change_working_dir(path_to_organize):
    os.chdir(path_to_organize)

def create_folders():
    for i in lista_carpetas:
        os.makedirs(i, exist_ok= True)
    
def move_dirs():
    for i in os.listdir():
        if i.endswith(doc_types):
            shutil.move(i, 'Documentos')
        elif i.endswith(img_types):
            shutil.move(i, 'Imagenes')
        elif i.endswith(software_types):
            shutil.move(i, 'Software')
        elif not os.path.isdir(i): # elif '.' in i
            shutil.move(i, 'Otros')



