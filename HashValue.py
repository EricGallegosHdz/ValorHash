# Importacion de modulos
import re
import hashlib
import argparse
import configparser

from configparser import ConfigParser

archivo_config = "config.ini"

# variables para lectura archivo de configuracion
config = ConfigParser()
config.read(archivo_config)

# Se obtiene el contenido del archivo de configuracion
documents = config.get("files", "list")

# Se busca en el archivo de configuracion texto que coincida
# con nombres de archivos
nameFile = "\w+.txt"
list = re.findall(nameFile, documents)
print("La lista de archivos es: ", list)


# Se realiza la obtencion del valor hash para los archivos encontrados
# y se almacenan los resultados en documento txt 
for element in list:
    with open(element, "rb") as f:
        byte = f.read()
        hash_text = hashlib.sha256(byte).hexdigest()
        print(element, " - ", hash_text)
        d = open("documento de resultado.txt", "a")
        d.write(element)
        d.write("-\t")
        d.write(hash_text)
        d.write("\n")

f.close()
