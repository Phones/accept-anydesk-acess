import os
import psutil
import pyautogui
import subprocess
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Crie um objeto WebDriver
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

dict_period_convert = {
    "1" : "13",
    "2" : "14",
    "3" : "15",
    "4" : "16",
    "5" : "17",
    "6" : "18",
    "7" : "19",
    "8" : "20",
    "9" : "21",
    "10" : "22",
    "11" : "23",
    "12" : "24"
}

def acess_yopemail():
    # Abra o navegador
    driver.get("https://yopmail.com/")
    
    # Pega o elemento de acesso da caixa de inserir email
    input_email_box = wait_element_using_id("login", 10)

    #insere o email
    email = ""
    input_email_box.send_keys(email)

    # Siomula um enter
    input_email_box.send_keys(Keys.ENTER)
  
def wait_element_using_id(id, time_limit=10):
    # Cria um objeto de espera
    wait = WebDriverWait(driver, time_limit)

    # Espera ate que o elemento esteja pronto
    wait.until(EC.presence_of_element_located((By.ID, id)))

    # Esperar até que o elemento com o ID desejado esteja presente
    insert_email_box = wait.until(EC.presence_of_element_located((By.ID, id)))

    return insert_email_box 

def wait_element_using_xpath(xpath, time_limit=10):
    # Espere até que o elemento com o XPath completo seja carregado
    WebDriverWait(driver, time_limit).until(EC.presence_of_element_located((By.XPATH, xpath)))

    # Pegue o texto do elemento
    search_box = driver.find_element(By.XPATH, xpath)

    return search_box

def wait_element_using_class_name(class_name, time_limit=10):
    # Espere até que o elemento com o XPath completo seja carregado
    WebDriverWait(driver, time_limit).until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))

    # Pegue o texto do elemento
    search_box = driver.find_element_by_class_name(class_name)

    return search_box

def get_text_of_last_email():
    element = wait_element_using_id("mail", 10)

    print(element.text)

def get_hour_of_email():
    # Pega o elemento que contem a hora do email
    xpath = "/html/body/header/div[3]/div[3]/span"
    hour_element = wait_element_using_xpath(xpath)

    return hour_element.text
    
def switch_to_iframe_using_xpath(xpath):
    iframe_element = wait_element_using_xpath(xpath, 10)

    driver.switch_to.frame(iframe_element)

def switch_to_iframe_using_id(id):
    iframe_element = wait_element_using_id(id, 15)

    driver.switch_to.frame(iframe_element)

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

        sleep(10)
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

def get_time_and_period_AM_PM():
    hour_list = get_hour_of_email().split(" ")

    # Pega o periodo AM ou PM
    period = hour_list[-1]
    # Pega a hora
    hour = hour_list[-2].split("")
    hour[0] = dict_period_convert[hour[0]]

    if "PM" in period:
        hour = dict_period_convert[int()]
        print(hour)

acess_yopemail()
while True:
    # Função que usa as imagens para clicarnos botões
    try:
        driver.refresh()
        sleep(8)
        switch_to_iframe_using_id("ifmail")

        get_time_and_period_AM_PM()
        get_text_of_last_email()
        
        using_images_to_search("anydesk")
    except Exception as ERRO:
        print(f"ERRO: {ERRO}")
