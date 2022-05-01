import requests
import lxml.html as html
import re


class ScraperPageArticle():

    def __init__(self, xpath_title, xpath_time, xpath_author, xpath_body):
        
        self.xpath_title = xpath_title
        self.xpath_time = xpath_time
        self.xpath_author = xpath_author
        self.xpath_body = xpath_body


    def scrape_notice(self, url_notice):

        self.url = url_notice
        try:
            response = requests.get(self.url, allow_redirects = False)
            if response.status_code == 200:
                notice = response.content.decode('utf-8')
                parsed = html.fromstring(notice)
                
                try:
                    self.title = parsed.xpath(self.xpath_title)[0]
                    self.title = self.__delete_characters_strings(self.title)
                    self.time_ = parsed.xpath(self.xpath_time)[0]
                    self.author = parsed.xpath(self.xpath_author)[0]
                    self.body = parsed.xpath(self.xpath_body)

                    
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

        self.result = {
            "title" : self.title,
            "time" : self.time_,
            "author" : self.author,
            "body" : self.body,
            "URL" : self.url
        }

        return self.result
        

    def save_news_to_file(self, root_folder):
        try:
            with open(f'{root_folder}/{self.author}-{self.title}.txt', 'w', encoding = 'utf-8') as f:
                f.write(self.title)
                f.write('\n\n')
                f.write(self.time_)
                f.write('\n')
                f.write(self.author)
                f.write('\n\n')
                for p in self.body:
                    f.write(p)
                    f.write('\n\n')
                f.write('\n\n')
                f.write(self.url)
        except:
            print("Error saving news")