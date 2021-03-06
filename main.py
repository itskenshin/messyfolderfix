import os
import shutil
# ruta donde va buscar los archivos
# route download folder
home= os.path.expanduser('~')
# addding route/ agregando ruta
ruta_descarga = ""
if os.path.exists(f'{home}\Downloads\\'):
    ruta_descarga = f'{home}\Downloads\\'
else:
    os.makedir(f'{home}\Downloads\\')
    ruta_descarga = f'{home}\Downloads\\'
# Extensiones
ext_texto = ['.docx','.txt','.doc','.pdf','.pptx']
ext_foto = ['.png','.jpg','.jpeg','.pdf','.gif']
ext_video = ['.mov','.mp4']
ext_musica = ['.mp3']
ext_exe = ['.exe']
ext_zips = ['.zip','.rar']

#*********************************
# este metoddo se encarga de buscar en la ruta los nombre de los archivo siempre y cuando sean archivos (lista)
# This method is responsible for searching the path for the file names as long as they are files (list)
def buscar_arch() -> list:
    return [arch.name for arch in os.scandir(ruta_descarga) if arch.is_file()]

# esta funcion espera 2 argumentos el archivo y la extensione luego va recorrer la lista de archivos
# por cada archivo va dividir el nombre y extension y lo guarda en las variables y luego se evalua si la extension
# se encuentra en la lista que hicimos de extensiones si esta lo mueve a la carpeta deseada

# this function expects 2 arguments for the file and the extension then it will go through the list of files
# for each file it will divide the name and extension and save it in the variables and then evaluate if the extension
# is in the list we made of extensions if it moves it to the desired folder

def ordenar(archivo,ext):
    for archivo in buscar_arch():
        try:
            nombre_arch,ext = os.path.splitext(archivo)
            for i in ext_texto:
                if ext == i:
                    # aqui mueve el archivo de la ruta a la carpeta(Texto) de la ruta NOTA:puedes crear diferentes carpetas
                    # here move the file from the path to the folder (Text) from the path note:you can create different folders
                    if os.path.exists(ruta_descarga+ 'Texto'):
                        shutil.move(ruta_descarga + archivo,ruta_descarga+ 'Texto')
                    else:
                        os.mkdir(ruta_descarga+ 'Texto')
                        shutil.move(ruta_descarga + archivo, ruta_descarga + 'Texto')
            for i in ext_video:
                if ext == i:
                    if os.path.exists(ruta_descarga + 'video'):
                        shutil.move(ruta_descarga + archivo, ruta_descarga + 'video')
                    else:
                        os.mkdir(ruta_descarga + 'video')
                        shutil.move(ruta_descarga + archivo, ruta_descarga + 'video')

            for i in ext_musica:
                if ext == i:
                    if os.path.exists(ruta_descarga + 'musica'):
                        shutil.move(ruta_descarga + archivo, ruta_descarga + 'musica')
                    else:
                        os.mkdir(ruta_descarga + 'musica')
                        shutil.move(ruta_descarga + archivo, ruta_descarga + 'musica')

            for i in ext_exe:
                if ext == i:
                    if os.path.exists(ruta_descarga + 'exe'):
                        shutil.move(ruta_descarga + archivo, ruta_descarga + 'exe')
                    else:
                        os.mkdir(ruta_descarga + 'exe')
                        shutil.move(ruta_descarga + archivo, ruta_descarga + 'exe')

            for i in ext_foto:
                if ext == i:
                    if os.path.exists(ruta_descarga + 'Fotos'):
                        shutil.move(ruta_descarga + archivo, ruta_descarga + 'Fotos')
                    else:
                        os.mkdir(ruta_descarga + 'Fotos')
                        shutil.move(ruta_descarga + archivo, ruta_descarga + 'Fotos')

            for i in ext_zips:
                if ext == i:
                    if os.path.exists(ruta_descarga + 'zip-rar'):
                        shutil.move(ruta_descarga + archivo, ruta_descarga + 'zip-rar')
                    else:
                        os.mkdir(ruta_descarga + 'zip-rar')
                        shutil.move(ruta_descarga + archivo, ruta_descarga + 'zip-rar')
            # si no encuentra ninguna de la extensiones lo guarda en la carpeta others
            # if it does not find any of the extensions it saves it in the others folder
            if ext != "":
                if os.path.exists(ruta_descarga + 'others'):
                    shutil.move(ruta_descarga + archivo, ruta_descarga + 'others')
                else:
                    os.mkdir(ruta_descarga + 'others')
                    shutil.move(ruta_descarga + archivo, ruta_descarga + 'others')
        except Exception as e:
            print(e)

# Esta funci??n recorrer?? la ruta, dividimos cada archivo por su nombre y extensi??n y luego lo pasamos a la funci??n ordenar
# This function will go through the path, we divide each file by its name and extension and then we pass it to the function ordenar
def ejecutar():
    for archivo in os.listdir(ruta_descarga):
        nombre_arch,ext = os.path.splitext(archivo)
        ordenar(nombre_arch,ext)

if __name__ == "__main__":
    ejecutar()
