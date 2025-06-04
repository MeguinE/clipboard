from flask import Flask, request
import pyperclip

app = Flask(__name__)
clipboard_data = ""

@app.route("/", methods=["GET"])
def get_clipboard():
    return clipboard_data

@app.route("/", methods=["POST"])
def set_clipboard():
    global clipboard_data
    clipboard_data = request.data.decode("utf-8")
    pyperclip.copy(clipboard_data)
    return "Clipboard updated", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
