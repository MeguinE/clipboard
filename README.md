# 📋 Clipboard Sync with Python & ngrok

Este proyecto permite **compartir el contenido del portapapeles entre dos dispositivos** a través de una conexión HTTP utilizando **Python** y **ngrok**. Ideal para quienes buscan una solución casera y personalizable para copiar y pegar texto entre máquinas sin depender de servicios externos.

## 🚀 Características

- Lee el contenido del portapapeles en una máquina.
- Lo envía a través de ngrok como una API accesible desde cualquier dispositivo.
- Permite recibir y pegar ese contenido en otra máquina remota.
- Totalmente hecho con Python 🐍.

## 📦 Requisitos

- Python 3.x
- [ngrok](https://ngrok.com/)
- Paquetes Python:
  - `flask`
  - `pyperclip`
  - `requests`

Puedes instalar los requisitos con:

```bash
pip install flask pyperclip requests
```
## ⚙️ Cómo usar
- Iniciar el servidor
 ```bash
clipboard_server.py
 ```
- Abrir túnel con ngrok
```bash
ngrok http 5000
 ```
Copia la URL pública generada por ngrok, como https://abc123.ngrok.io.
- En la otra máquina (cliente) asi como el la que actuara como servidor `clipboard_sender.py`
   - Edita la URL en el script client.py para apuntar a tu endpoint de ngrok:
  ```bash
  url = 'https://abc123.ngrok.io'
   ```
    - luego ejecuta:
      ```bash
      python clipboard_sender.py
       ```
      ```bash
      python clipboard_receiver.py
       ```
      Este script recuperará el contenido del portapapeles remoto y lo pegará en el portapapeles local.

## 🔐 Consideraciones de seguridad
Este proyecto es para uso personal, educativo o local. Compartir el portapapeles a través de la web no es seguro sin autenticación ni cifrado adicional. Usa con precaución.

## 🤓 ¿Por qué hacer esto?

- Aprender sobre servidores HTTP con Flask.
- Entender cómo funciona ngrok.
- Manejar el portapapeles con Python.
- Explorar automatización entre dispositivos.
