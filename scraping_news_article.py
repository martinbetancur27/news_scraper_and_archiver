import requests
import lxml.html as html
import re


class ScraperPageArticle():

    def __init__(self, xpath_title, xpath_time, xpath_author, xpath_body):
        
        self.__xpath_title = xpath_title
        self.__xpath_time = xpath_time
        self.__xpath_author = xpath_author
        self.__xpath_body = xpath_body


    def scrape_notice(self, url_notice):

        self.__url = url_notice
        try:
            response = requests.get(self.__url, allow_redirects = False)
            if response.status_code == 200:
                notice = response.content.decode('utf-8')
                parsed = html.fromstring(notice)
                
                try:
                    self.__title = parsed.xpath(self.__xpath_title)[0]
                    self.__title = self.__delete_characters_strings(self.__title)
                    self.__time_ = parsed.xpath(self.__xpath_time)[0]
                    self.__author = parsed.xpath(self.__xpath_author)[0]
                    self.__body = parsed.xpath(self.__xpath_body)

                    
                except IndexError:
                    print("Error al indexar el documento. Revisar carpeta.")
                    return
                
            else:
                raise ValueError(f'Error: {response.status_code}')
                
        except ValueError as ve:
            print(ve)
    

    def __delete_characters_strings(self, string):
        #using regex
        #This means "substitute every character that is not a number a-z " "(space) $ . , - '
        string = re.sub(r"[^a-zA-Z0-9' '$'-'.',]","",string)
        return string


    def get_news_article(self):

        self.__result = {
            "title" : self.__title,
            "time" : self.__time_,
            "author" : self.__author,
            "body" : self.__body,
            "URL" : self.__url
        }

        return self.__result
        

    def save_news_to_file(self, root_folder):
        try:
            with open(f'{root_folder}/{self.__author}-{self.__title}.txt', 'w', encoding = 'utf-8') as f:
                f.write(self.__title)
                f.write('\n\n')
                f.write(self.__time_)
                f.write('\n')
                f.write(self.__author)
                f.write('\n\n')
                for p in self.__body:
                    f.write(p)
                    f.write('\n\n')
                f.write('\n\n')
                f.write(self.__url)
        except:
            print("Error saving news")