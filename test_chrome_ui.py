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

    screenshot_before = os.path.join(os.getcwd(), "screenshot_before_check.png")
    ImageGrab.grab().save(screenshot_before)
    if os.path.exists(screenshot_before):
        print(f"Screenshot before check saved at {screenshot_before}")
    else:
        print("ERROR: Screenshot before check was not created!")

    time.sleep(5)

    omnibox = window.child_window(title="Address and search bar", control_type="Edit")
    if omnibox.exists():
        print("Address bar found")
    else:
        print("Address bar NOT found")
        exit(1)

except ElementNotFoundError:
    print("Chrome UI not found")
    exit(1)

screenshot_after = os.path.join(os.getcwd(), "screenshot.png")
ImageGrab.grab().save(screenshot_after)
if os.path.exists(screenshot_after):
    print(f"Final screenshot saved at {screenshot_after}")
else:
    print("ERROR: Final screenshot was not created!")

app.kill()
