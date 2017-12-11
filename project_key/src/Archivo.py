import os.path as path
import os


def escribir_add(path, data):
    '''Escribe en el archivo path, sin sobreescribir'''
    f = open(path, 'a+')
    f.write(data)
    f.close()
    return


def leer(path):
    '''devuelve una cadena con el contenido de path'''
    f = open(path, 'r')
    data = f.read()
    f.close()
    return data


def leer_and_clean(path):
    '''devuelve una cadena con el contenido de path'''
    f = open(path, 'r+')
    data = f.read()
    f.seek(0)
    f.truncate()
    f.close()
    return data


def sobreescribir(path, data):
    '''abre o crea un archivo path y luego si tiene contenido lo sobreescribe con data'''
    f = open(path, 'w')
    f.write(data)
    f.close()
    return


def is_empty_file(filen):
    '''devuelve verdad si filen esta vacio'''
    f = open(filen, 'r+')
    data = f.read()
    if len(data) == 0:
        return True
    else:
        return False


def is_open_file(file_name):
    if path.exists(file_name):
        try:
            os.rename(file_name, file_name)
            return False
        except:
            return True
    else:
        return False
