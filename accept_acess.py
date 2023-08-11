import pyautogui
from time import sleep

def search_and_click(image_path):
    # Get the position of the button
    button_position = pyautogui.locateCenterOnScreen(image_path)
    # Click on the button
    pyautogui.click(button_position)

while True:
    image_path = "images\\teste.png"
    search_and_click(image_path)
    
    sleep(30)
