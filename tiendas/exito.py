import  requests
from bs4 import BeautifulSoup

from selenium import webdriver
# from selenium.webdriver.common.by import By
# dependencia para firefox
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
# Opciones navegadores
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import TimeoutException,NoAlertPresentException, NoSuchWindowException, WebDriverException
import os, sys, shutil, requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


def iniciar_chrome():
    options = Options()
    options.headless = False
    chromeOptions = webdriver.ChromeOptions()
    prefs = {
        "safebrowsing.enabled": "false",
        'profile.default_content_setting_values.automatic_downloads': 1,
    }
    options.add_experimental_option("prefs",prefs)
    navegador = webdriver.Chrome(chrome_options=options)
    # navegador = webdriver.Chrome(chrome_options=options)
    # time.sleep(10)
    navegador.implicitly_wait(30)
    navegador.maximize_window()

    return navegador


def iniciar_firefox():
    # Crear una sesión de Firefox
    options = Options()
    options.headless = True
    navegador = webdriver.Firefox(options=options)
    navegador.implicitly_wait(30)
    # print ("Headless Firefox Initialized")
    # navegador.maximize_window()
    return navegador


def __paginacarga(navegador, elementById):
    timeout = 2
    try:
        element_present = EC.presence_of_element_located((By.ID,elementById))
        WebDriverWait(navegador, timeout).until(element_present)
        # print("La pagina ya cargo")
        return True
    except:
        # print("no cargado")
        return False

def abrir_pagina(navegador, pagina, elementoById):

    """
    Esta funcion se encarga de abrir una pagina, realizara 3 intentos en caso de que esta falle al cargar.

    se requieren los siguientes parametros:
    - Navegador
    - link de la pagina
    - id de un elemento del html

    """
    html = navegador.get(pagina)
    # print(f"Tipo de objeto: {html}")
    # print(f"Tipo de objeto: {navegador.get(pagina)}")
    if __paginacarga(navegador, elementoById):
        return html
    else:
        return " "
    

def transformar_texto(articulo):
    nombre_articulo = ""
    nombre_articulo = articulo.replace(' ','%20')

    return nombre_articulo


def get_html(navegador, url):
    navegador.get(url)
    __paginacarga(navegador, "imagen")
    return navegador.page_source

def buscar_producto(articulo):

    listado_articulos = []


    url = f"https://www.exito.com/search?_query={transformar_texto(articulo)}"
    print(f"link de consulta: {url}")
    navegador = iniciar_firefox()
    html = get_html(navegador, url)
    soup = BeautifulSoup(html,'html.parser')
    # print(f"formado de html es: {type(html)}")
    # sleep(3)
    articulos = soup.find_all('div', class_ ='vtex-search-result-3-x-galleryItem vtex-search-result-3-x-galleryItem--normal pa4')
    # print(articulos)
    for articulo in articulos:
        nombre = articulo.find('div', class_='exito-product-details-3-x-stylePlp').text
        # precioreal = articulo.find('span', class_='price-tag-fraction').text
        precio = articulo.find('div', class_='flex f5 fw5 pa0 flex items-center justify-start w-100 search-result-exito-vtex-components-selling-price exito-vtex-components-4-x-alliedDiscountPrice').text
        precio = precio.replace("$",' ')
        print(f"Nombre: {nombre.strip()} \tprecio: {precio.strip()}")
        listado_articulos.append([nombre.strip(), precio.strip()])
    navegador.close()
    # print("IMPRESION DE LISTA")
    # leerlista(listado_articulos)

    return listado_articulos



def leerlista(lista):
    for item in lista:
        print(item)

# buscar_producto("DELL 3400")