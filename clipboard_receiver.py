import pyperclip
import requests
import time

NGROK_URL = "https://ae33-187-146-168-71.ngrok-free.app"  # Usa la misma URL

last_received = ""

while True:
    try:
        response = requests.get(NGROK_URL)
        text = response.text
        if text != last_received:
            pyperclip.copy(text)
            print("📥 Recibido y copiado:", text)
            last_received = text
    except Exception as e:
        print("Error:", e)
    time.sleep(1)
