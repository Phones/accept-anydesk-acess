import os
import psutil
import pyautogui
import subprocess
from time import sleep

def search_and_click(image_name):
    # caminho para a imagem
    image_path = f"images/{image_name}"
    # Get the position of the button
    button_position = pyautogui.locateCenterOnScreen(image_path)

    if button_position is None:
        # Click in anydesk runnung in taskbar
        anydesk_taskbar_image = "images/anydesk_in_taskbar.png"
        button_position = pyautogui.locateCenterOnScreen(anydesk_taskbar_image)

        # Click on the button
        pyautogui.click(button_position)

        sleep(5)
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

def using_images_to_search(program):
    # Program (anydesk or teamviewer or all)
    images_list = os.listdir("images/")
    for image in images_list:
        if program in image:
            search_and_click(image_name=image)

        elif program in "all":
            search_and_click(image_name=image)

while True:
    # Função que usa as imagens para clicarnos botões
    using_images_to_search("anydesk")
    sleep(30)
