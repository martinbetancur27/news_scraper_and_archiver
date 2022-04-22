import requests
from lxml import etree
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions
import time

class Scraper():


    def __connect_browser(self, page):
        #No recibe ningun parametro
        #Hace la conexion con el webdriver de Chrome.
        #No retorna ningun valor

        '''ChromeDriver es un ejecutable separado que Selenium WebDriver usa para controlar Chrome. 
        Lo mantiene el equipo de Chromium con la ayuda de los colaboradores de WebDriver.
        https://chromedriver.chromium.org/getting-started
        
        Selenium admite la automatización de todos los principales navegadores del mercado mediante el uso de WebDriver
        WebDriver es una API y un protocolo que define una interfaz independiente del idioma para controlar el 
        comportamiento de los navegadores web. Cada navegador está respaldado por una implementación específica de WebDriver, 
        llamada controlador. https://www.selenium.dev/documentation/webdriver/getting_started/'''
        try:
            #Ocultar el navegador
            self.options = ChromeOptions()
            self.options.headless = True

            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
            self.driver.get(page)
        except:
            print("Error al conectar el driver del navegador")


    def scraper_dynamic_page(self, page):
        #Recibe Url
        #Ejecutar metodo __connect_browser()
            #Obtener la pagina por medio del driver de Selenium. 
            #Hacer scroll 'infinito' y con tiempo de pausa para
            #permtir que se cargue todo el contenido. 
            #Sincrónicamente ejecuta JavaScript en la ventana/marco actual
            #obtenemos el código html interno del cuerpo. 
            #Enviar el resultado al metodo __beautifulsoup_connect
            #Sale del controlador y cierra todas las ventanas asociadas.
        #No retorna ningun valor
        try:
            self.__connect_browser(page)
            self.__slow_scroll()     
            body = self.driver.execute_script("return document.body")
            page_source = body.get_attribute('innerHTML') 
            self.__beautifulsoup_connect(page_source)
            self.driver.quit() 
        except:
            print("Error al realizar el scraping sobre web dinamica. Revise su URL")

    
    def scraper_static_page(self, page):
        #Recibe Url
        #Obtener pagina por medio de requests. 
            #Enviar el resultado al metodo __beautifulsoup_connect
        #No retorna ningun valor

        try:
            page_source = requests.get(page)
            self.__beautifulsoup_connect(page_source.text)
        except:
            print("Error al realizar el scraping sobre web estatica. \n Revise su URL o intente con el metodo scraper_dynamic_page")


    def __beautifulsoup_connect(self, page_source):
        #Recibe como parametro la pagina obtenida por medio de requests o el driver de Selenium
        #Crea el objeto 'Beautiful Soup' de la pagina recibida
        #No retorna ningun valor.

        '''Ejecutar el documento HTML a través de Beautiful Soup nos da un objeto BeautifulSoup que 
        representa el documento como una estructura de datos anidados. 
        https://beautiful-soup-4.readthedocs.io/en/latest/
        
        (Con self.soup se tendran formas de navegar esa estructura de datos)'''

        try:
            self.soup = BeautifulSoup(page_source, 'html.parser')
        except:
            print("Error al conectar con BeutifulSoup")
        

    def __slow_scroll(self):
        #No recibe parametro
        #Controlar el scroll de la pagina por medio una accion de Javascript y Selenium
        #No retorna ninguno valor
        try:

            #Deslizamiento pausado (1 segundo) para permitir que el contenido se cargue (sitios dinamicos).
            #Permite el scroll "infinito"
            ###### PRUEBAS CON EL SITIO: https://finance.yahoo.com
            # Este resultado trajo mas o menos 3 veces que el realizado con el metodo estatico.
            #TENER EN CUENTA: XPATH del navegador (CARGADO COMPLETAMENTE) trae mas datos sin embargo este metodo 
            #trae una cantidad relativamente cerca.
            
            #FUENTE DEL CODIGO: https://blogvisionarios.com/e-learning/articulos-data/web-scraping-de-paginas-dinamicas-con-selenium-python-y-beautifulsoup-en-azure-data-studio/
            print("Por favor esperar... La pagina puede ser muy extensa")
            self.driver.maximize_window()
            time.sleep(1)
            #We make a slow scroll to the end of the page
            iter=1
            while True:
                scrollHeight = self.driver.execute_script("return document.documentElement.scrollHeight")
                Height=250*iter
                self.driver.execute_script("window.scrollTo(0, " + str(Height) + ");")
                if Height > scrollHeight:
                    print('End of page')
                    break
                time.sleep(1)
                iter+=1
        except:
            print("Error al realizar el scroll dinamico")


#los siguientes metodos son para llamar metodos de BeautifulSoup
    def bs_find_all(self, *args, **kwargs):
        try:
            return self.soup.find_all(*args, **kwargs)
        except:
            print("(bs_find_all) Error al realizar busqueda con el atributo ", args)
        

    def bs_find(self, *args, **kwargs):
        try:
            return self.soup.find(*args, **kwargs)
        except:
            print("(bs_find) Error al realizar busqueda con el atributo ", args)
    

    def bs_find_all_get_text(self, *args, **kwargs):
        try:
            texts = self.soup.find_all(*args, **kwargs)
            list_texts = []
            for text in texts:
                list_texts.append(text.get_text())

            return list_texts
        except:
            print("(bs_find_all_get_text) Error al realizar busqueda con el atributo ", args)

#Los siguientes metodos son para hacer la busqueda mas natural
    def get_all_tag(self, tag):
        #Recibir etiqueta
        #Filtrar por la etiqueta
        #Retornar busqueda
        try:
            return self.soup.find_all(tag)
        except:
            print("Error al realizar scraping con la etiqueta ", tag)


    def get_attribute_by_tag(self, tag, tag_attribute):
        #recibe etiqueta y atributo
        #Busca todas las etiquetas
            #Filtra por el atributo recibido
        #Retorna una lista con los atributos
        try:
            scraping_tag = self.soup.find_all(tag)
            list_attribute = []
            
            for elem in scraping_tag:
                if elem.has_attr(tag_attribute):
                    list_attribute.append(elem[tag_attribute])
            
            return list_attribute
        except:
            print("Error al obtener el atributo ", tag_attribute)
    

    def get_by_xpath(self, var_xpath):
        #Recibe expresion Xpath
        #Utiliza la clase etree para convertir el HTML y poder filtrar por la expresion
        #Retorna la busqueda
        try:
            dom = etree.HTML(str(self.soup))
            return dom.xpath(var_xpath)
        except:
            print("Error al realizar busqueda XPATH ", var_xpath)
    

    def get_content_tag(self, tag):
        #Recibe etiqueta
        #Busca la etiqueta con el metodo de BeautifulSoup.
            #Captura el contenido de la etiqueta
        #Retorna lista con el contenido

        try:
            texts = self.soup.find_all(tag)
            list_texts = []
            for text in texts:
                list_texts.append(text.get_text())

            return list_texts
        except:
            print("Error al realizar busqueda de contenido en la etiqueta ", tag)