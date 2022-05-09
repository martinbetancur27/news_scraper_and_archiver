from bs4 import BeautifulSoup
from lxml import etree

class BeautifulSoupPersonalized():

    def __init__(self, page_source):
        #receives an http response. Content of a page
        self.__soup = self.__beautifulsoup_connect(page_source)
        

    def __beautifulsoup_connect(self, page_source):
        # Receive as parameter the page obtained through requests or the Selenium driver
        #Create the 'Beautiful Soup' object from the received page
        #Does not return any value.

        '''Running the HTML document through BeautifulSoup gives us a BeautifulSoup object that 
        represents the document as a nested data structure.
        https://beautiful-soup-4.readthedocs.io/en/latest/
        
        (With self.soup you will have ways to navigate that data structure)'''

        try:
            soup = BeautifulSoup(page_source, 'html.parser')
            return soup
        except:
            print("Error connecting to BeautifulSoup")


    #the following methods are for calling BeautifulSoup methods
    def bs_find_all(self, *args, **kwargs):
        try:
            return self.__soup.find_all(*args, **kwargs)
        except:
            print("(bs_find_all) Error performing search ", args)
        

    def bs_find(self, *args, **kwargs):
        try:
            return self.__soup.find(*args, **kwargs)
        except:
            print("(bs_find) Error performing search ", args)
    

    def bs_find_all_get_text(self, *args, **kwargs):
        try:
            texts = self.__soup.find_all(*args, **kwargs)
            list_texts = []
            for text in texts:
                list_texts.append(text.get_text())

            return list_texts
        except:
            print("(bs_find_all_get_text) Error performing search ", args)


    #The following methods are to make the search more natural
    def get_all_tag(self, tag):
        #Receive label
        #Filter by tag
        #return search
        try:
            return self.__soup.find_all(tag)
        except:
            print("Error when scraping with the tag ", tag)


    def get_attribute_by_tag(self, search):
        #receive tag and attribute: tag-attribute
        #find all tags
            #Filter by received attribute
        #Return a list with the attributes        
        try:
            #The logic of this program is to receive two parameters.
                #The user enters them with this logic: parameter1-parameter2
            search = search.split("-")
            tag = search[0]
            tag_attribute = search[1]

            scraping_tag = self.__soup.find_all(tag)
            list_attribute = []
            
            for elem in scraping_tag:
                if elem.has_attr(tag_attribute):
                    list_attribute.append(elem[tag_attribute])
            
            return list_attribute
        except:
            print("Error performing search ", search)
    

    def get_by_xpath(self, var_xpath):
        #Recibe expresion Xpath
        #Utiliza la clase etree para convertir el HTML y poder filtrar por la expresion
        #Retorna la busqueda
        try:
            dom = etree.HTML(str(self.__soup))
            return dom.xpath(var_xpath)
        except:
            print("Error performing XPATH lookup ", var_xpath)
    

    def get_content_tag(self, tag):
        #Receive tag
        #Find the tag with the BeautifulSoup method.
            #Fetch the content of the tag
        #Return list with content

        try:
            texts = self.__soup.find_all(tag)
            list_texts = []
            for text in texts:
                list_texts.append(text.get_text())

            return list_texts
        except:
            print("Error performing content search on tag ", tag)