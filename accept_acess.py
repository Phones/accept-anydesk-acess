import psutil
import pyautogui
import subprocess
from time import sleep

def search_and_click(image_name):
    # caminho para a imagem
    image_path = f"images/{image_name}"
    # Get the position of the button
    button_position = pyautogui.locateCenterOnScreen(image_path)
    # Click on the button
    pyautogui.click(button_position)

def is_program_running(program):
    for proc in psutil.process_iter(['pid', 'name']):
        if program in proc.info['name']:
            return True
        
    return False

def is_anydesk_running_and_start():
    if not is_program_running("anydesk"):
        subprocess.Popen("anydesk", shell=True)
        print("O AnyDesk não está em execução.")
