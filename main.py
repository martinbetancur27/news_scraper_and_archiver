from provider import ProviderYahoo
from scraper_dynamic_page import ScraperDynamicPage
import os
import datetime


def create_folder(name_provider):
    #Create folder and subfolder. Current date --> provider name.
    #Return root folder

    today = datetime.date.today().strftime('%d-%m-%Y')
    if not os.path.isdir(today):
        os.mkdir(today)
    
    root_folder = today + "/" + str(name_provider)

    if not os.path.isdir(f'{today}/{name_provider}'):
        os.mkdir(f'{root_folder}')

    return root_folder

        
def main():

    HOME_URL = "https://finance.yahoo.com"
    scraper_yahoo = ScraperDynamicPage(HOME_URL)
    #Scrape page home. Dynamic Page
    
    if scraper_yahoo.getConnect():
        while(True):
            #User logic
            #choose provider
            provider_yahoo = ProviderYahoo()
            
            print("Choice: ", provider_yahoo)
            enable_folder_creation = True

            #The logic of the yahoo home page is to have two structures to get the provider.
                #Result 1
            xpath_provider = provider_yahoo.get_xpath_provider_home_struc1()
            result_scrape = scraper_yahoo.get_by_xpath(xpath_provider)
                #Result 2
            xpath_provider = provider_yahoo.get_xpath_provider_home_struc2()
            result_scrape += scraper_yahoo.get_by_xpath(xpath_provider)
            #get_by_xpath return list. Concatenate with the list of the result of structure 1
            
            for url in result_scrape:

                if(url[0:6] != "https:" and url[0:3] != "/m/" and url != '/news/'):
                    #Prohibit non-news structures (https and /news/)
                    #Ban those that do not allow scraping (/m/)
                    
                    #Structure in this position to avoid creating empty folders
                    if enable_folder_creation:
                        root_folder = create_folder(provider_yahoo)
                        enable_folder_creation = False

                    url_full = HOME_URL + url
                    #The href does not have the initial extension (HOME_URL)

                    #print(f'\n {url_full}') 
                    #Test: print link in console

                    provider_yahoo.scrape_notice(url_full)
                    #scrape news
                    provider_yahoo.save_news_to_file(root_folder)
                    #save news
            
            #print name provider
            print(f"\n{provider_yahoo}... Search finished")
            
            option_final = input("1. choose another provider\n2. Exit\n--> ")

            if option_final == "1":
                continue
            else:
                break

    else:
        print("Failed to connect to https://finance.yahoo.com")

if __name__ == "__main__":
    
    main()