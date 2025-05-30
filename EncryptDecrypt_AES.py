from cryptography.fernet import Fernet
import json

# Cargar el diccionario desde el archivo JSON
with open("dict.json", "r", encoding="utf-8") as file:
    diccionario = json.load(file)

# Selección del idioma
idioma = input("Choose Language / Seleccione el idioma (en/es): ").strip().lower()
if idioma not in diccionario:
    print("❌ Language not found, changing to English by default.")
    idioma = "en"  # Idioma por defecto

def generar_clave():
    clave = Fernet.generate_key()
    print(diccionario[idioma]["generated_key"] + "-->" + clave.decode())
    return clave

def encriptar(clave, texto):
    cipher = Fernet(clave)
    texto_encriptado = cipher.encrypt(texto.encode()).decode()
    print(diccionario[idioma]["encrypted_text"] + "-->" + texto_encriptado)
    return texto_encriptado

def desencriptar(clave, texto_encriptado):
    try:
        cipher = Fernet(clave)
        texto_desencriptado = cipher.decrypt(texto_encriptado.encode()).decode()
        print(diccionario[idioma]["decrypted_text"] + "-->" + texto_desencriptado)
##        print(f"Texto desencriptado --> {texto_desencriptado}")
    except:
        print("Error: La clave proporcionada no es válida o el texto no puede ser desencriptado.")

def menu():
    while True:
        # Acceder a las traducciones
        print(diccionario[idioma]["menu"])
        print("1. " + diccionario[idioma]["generate_key"])
        print("2. " + diccionario[idioma]["encrypt_text"])
        print("3. " + diccionario[idioma]["decrypt_text"])
        print("4. " + diccionario[idioma]["exit"])
        opcion = input(diccionario[idioma]["choose_option"])
        

        if opcion == "1":
            clave = generar_clave()

        elif opcion == "2":
            clave_usuario = input(diccionario[idioma]["inSecureKey"]).encode()            
            texto = input(diccionario[idioma]["inTextEncrypt"])
            encriptar(clave_usuario, texto)

        elif opcion == "3":
            clave_usuario = input(diccionario[idioma]["inSecureKey"]).encode()
            texto_encriptado = input(diccionario[idioma]["inTextDecrypt"])
            desencriptar(clave_usuario, texto_encriptado)

        elif opcion == "4":
            print(diccionario[idioma]["closing"])
            break

        else:
            print(diccionario[idioma]["noValid"])

menu()
