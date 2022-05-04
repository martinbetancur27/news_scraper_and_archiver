#beautiful_soup program module
from beautiful_soup import BeautifulSoupPersonalized

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions
import time

class ScraperDynamicPage(BeautifulSoupPersonalized):

    #This class inherits the methods of the BeautifulSoupPersonalized class.
            #Inherit methods for lookup

    def __init__(self, page_url):

        #connect: connection validation
        self.__connect = False
        __page_result = self.__scraper_dynamic_page(page_url)

        if(self.__connect):
            #super().__init__ Initialize the constructor of the superclass
            super().__init__(__page_result)
        
    
    def __connect_browser(self, page):
        
        #It makes the connection with the Chrome webdriver.
        #Does not return any value

        '''ChromeDriver is a separate executable that Selenium WebDriver uses to control Chrome.
        It is maintained by the Chromium team with the help of WebDriver contributors.
        https://chromedriver.chromium.org/getting-started
        
        Selenium supports automation of all major browsers on the market by using WebDriver.
        WebDriver is an API and protocol that defines a language-independent interface for controlling the behavior of web browsers. 
        Each browser is backed by a specific implementation of WebDriver, called controller. 
        https://www.selenium.dev/documentation/webdriver/getting_started/'''

        try:
            #Hide the browser
            self.__options = ChromeOptions()
            self.__options.headless = True
            #Hide unnecessary logs from the user
            self.__options.add_argument("--log-level=3")

            self.__driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.__options)
            self.__driver.get(page)
            #if the above piece of code doesn't break set the connection to true
            self.__connect = True
        except:
            print("Error connecting browser driver. Check the url\n")
            self.__connect = False


    def __scraper_dynamic_page(self, page):
        #Receive Url
        #execute method __connect_browser()
            #Get the page through the Selenium driver.
            #Make scroll 'infinite' and with pause time for
            #allow all content to be loaded.
            #Synchronously run JavaScript in the current window/frame
            # get the internal html code of the body.
            #Send the result to the __beautifulsoup_connect method
            #Exit the controller and close all associated windows.
         #Does not return any value
        try:
            self.__connect_browser(page)

            if (self.__connect):
                self.__slow_scroll()     
                body = self.__driver.execute_script("return document.body")
                page_source = body.get_attribute('innerHTML') 
                self.__driver.quit()
                return page_source
        except:
            print("Error when performing scraping on dynamic web")

    
    def __slow_scroll(self):
        #Does not receive parameter
        #Control page scrolling through a Javascript and Selenium action
        #Does not return any value
        try:

            #Scroll paused (1 second) to allow content to load (dynamic sites).
            #Allow "infinite" scroll
            ###### TESTS WITH THE SITE: https://finance.yahoo.com
            # This result brought more or less 3 times than the one obtained with the static method.
            #PLEASE NOTE: Browser XPATH (FULLY LOADED) brings more data however this method
            #brings a relatively close amount.
            
            #CODE SOURCE: https://blogvisionarios.com/e-learning/articulos-data/web-scraping-de-paginas-dinamicas-con-selenium-python-y-beautifulsoup-en-azure-data-studio/
            print("Please wait... The page can be very long")
            self.__driver.maximize_window()
            time.sleep(1)
            #We make a slow scroll to the end of the page
            iter=1
            while True:
                scrollHeight = self.__driver.execute_script("return document.documentElement.scrollHeight")
                Height=250*iter
                self.__driver.execute_script("window.scrollTo(0, " + str(Height) + ");")
                if Height > scrollHeight:
                    print("Scroll finished, please wait")
                    break
                time.sleep(1)
                iter+=1
        except:
            print("Error when performing dynamic scroll")


    def getConnect(self):
        return self.__connect