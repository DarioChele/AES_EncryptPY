# 🔐 AES Encryptor in Python
### 🌟 Description This Python project uses the AES (Fernet) encryption algorithm to generate keys, encrypt, and decrypt text easily. 🔐

## ⚡ Features
  ✅ AES key generation in base64 format  
  ✅ Text encryption using a provided AES key  
  ✅ Decryption of previously encrypted texts with the same key  
  ✅ Intuitive console interface for smooth interaction  

## 🚀 Installation 
1️⃣ Clone the repository from GitHub 
```bash 
git clone https://github.com/DarioChele/AES_EncryptPY.git cd AES_EncryptPY 
```

2️⃣ Build the Docker image 
```bash 
docker build -t encrypt-aes .
```

3️⃣ Run the Docker container  

🔹 Interactive mode 
```bash 
docker run --rm -it encrypt-aes
```

🔹 Passing an AES key as an environment variable 
```bash 
docker run --rm -it -e AES_KEY="aes_key_base64" encrypt-aes
```

🔹 Mounting a volume to persist files 
```bash 
docker run --rm -it -v "$(pwd)/data:/app/data" encrypt-aes
```

## 🎮 Usage 
Once the program is running, the following menu options will appear: 
  1️⃣ Generate an AES key 🔑  
  2️⃣ Encrypt text 🔏  
  3️⃣ Decrypt text 🔓  
  4️⃣ Exit 🚪

## Example usage: 
```bash 
🔹 Enter the key for encryption: {Generated AES key}
🔹 Enter the text to encrypt: Hello, world!
🔹 Encrypted text: {Encrypted output}
```

```bash 
🔹 Enter the key for decryption: {Same AES key used for encryption}
🔹 Enter the encrypted text: {Encrypted output}  
🔹 Decrypted text: Hello, world!
```

## 📌 Requirements
  🔹 Python 3.10+  
  🔹 Docker (optional for container execution)

## 📜 License 
This project is licensed under MIT, allowing free use, modification, and sharing. 🎉

🚀✨ Ready to securely encrypt and decrypt text using AES! 💡


# 🔐 Encriptador AES en Python
### 🌟 Descripción Este proyecto en Python utiliza el algoritmo de cifrado AES (Fernet) para generar claves, encriptar y desencriptar textos de manera sencilla. 🔐

## ⚡ Características
  ✅ Generación de claves de cifrado AES en base64  
  ✅ Encriptación de textos utilizando una clave AES proporcionada  
  ✅ Desencriptación de textos previamente cifrados con la misma clave  
  ✅ Interfaz de consola intuitiva para interactuar con el sistema de cifrado

## 🚀 Instalación
1️⃣ Clonar el repositorio desde GitHub 
```bash 
git clone https://github.com/DarioChele/AES_EncryptPY.git cd AES_EncryptPY
```

2️⃣ Construcción de la imagen Docker 
```bash 
docker build -t encripta-aes .
```

3️⃣ Ejecutar el contenedor Docker  

🔹 Modo interactivo  
```bash 
docker run --rm -it encripta-aes
```

🔹 Pasando una clave AES como variable de entorno  
```bash
docker run --rm -it -e AES_KEY="clave_aes_base64" encripta-aes 
```

🔹 Montando un volumen para persistir archivos 
```bash 
docker run --rm -it -v "$(pwd)/data:/app/data" encripta-aes
```

## 🎮 Uso 
Una vez ejecutado el programa, se mostrará un menú con las siguientes opciones:  
  1️⃣ Generar una clave AES 🔑  
  2️⃣ Encriptar un texto 🔏  
  3️⃣ Desencriptar un texto 🔓  
  4️⃣ Salir 🚪

## Ejemplo de uso: 
```bash  
🔹 Ingrese la clave para encriptar: {Clave AES generada}
🔹 Ingrese el texto a encriptar: ¡Hola, mundo!
🔹 Texto encriptado: {Texto cifrado}
```

```bash  
🔹 Ingrese la clave para desencriptar: {Misma Clave AES usada en la encriptación}
🔹 Ingrese el texto encriptado: {Texto cifrado}
🔹 Texto desencriptado: ¡Hola, mundo!
```

## 📌 Requisitos  
🔹 Python 3.10+  
🔹 Docker (opcional para ejecución en contenedor)

## 📜 Licencia Este proyecto está distribuido bajo la licencia MIT. Puedes usarlo, modificarlo y compartirlo libremente. 🎉

🚀✨ ¡Listo para cifrar y descifrar textos de manera segura con AES! 💡
