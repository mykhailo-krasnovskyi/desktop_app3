import os
import time
import requests
from pywinauto import Application
from pywinauto.findwindows import ElementNotFoundError
from PIL import ImageGrab

chrome_installer = "chrome_installer.exe"
chrome_url = "https://dl.google.com/chrome/install/latest/chrome_installer.exe"

if not os.path.exists(chrome_installer):
    response = requests.get(chrome_url, stream=True)
    with open(chrome_installer, "wb") as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)

os.system(f"{chrome_installer} /silent /install")

time.sleep(10)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
app = Application().start(chrome_path)

time.sleep(3)

try:
    window = app.window(title_re=".*Google Chrome.*")
    window.wait("ready", timeout=10)
    print("Chrome UI loaded successfully")
except ElementNotFoundError:
    print("Chrome UI not found")
    exit(1)

ImageGrab.grab().save("screenshot.png")

app.kill()
