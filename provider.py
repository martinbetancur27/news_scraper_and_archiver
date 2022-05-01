from scraping_news_article import ScraperPageArticle


class ProviderYahoo(ScraperPageArticle):
    #Inherit from class 'ScraperPageArticle'

    #XPATH to extract the information from each news page. class attributes
    XPATH_TITLE = '//header[@class="caas-title-wrapper"]//text()'
    XPATH_TIME = '//time[@class]/text()'
    XPATH_AUTHOR = '//span[@class="caas-attr-provider"]/text()'
    XPATH_BODY = '//div[@class="caas-body"]/descendant::*/text()'
    
    #Yahoo Top Providers List
    PROVIDERS = {
            1: "Argus Research",
            2: "Barrons.com",
            3: "Bloomberg",
            4: "Financial Times",
            5: "Fortune",
            6: "FX Empire",
            7: "Investor's Business Daily",
            8: "MarketWatch",
            9: "Morningstar Research",
            10: "Quartz",
            11: "Reuters",
            12: "SmartAsset",
            13: "TechCrunch",
            14: "TipRanks",
            15: "USA TODAY",
            16: "Yahoo Finance",
            17: "Yahoo Money"
        }

    def __init__(self):

        super().__init__(ProviderYahoo.XPATH_TITLE, ProviderYahoo.XPATH_TIME, ProviderYahoo.XPATH_AUTHOR, ProviderYahoo.XPATH_BODY)
        ##Initialize the constructor of the superclass. XPATH to extract the information are sent as parameters

        #When the class is called a provider is chosen
        self.provider_name = self.choose_provider()


    #Overload print method. print(this object) will print the provider name
    def __str__(self):

        return str(self.provider_name)


    def choose_provider(self):

        #Variable that controls if the user makes a mistake when entering a number
        fail_user = False
        #Print in a format with good user experience
        print ("{:<5} {:<5}".format('Num', 'Provider'))

        for key, value in ProviderYahoo.PROVIDERS.items():

            print ("{:<5} {:<5}".format(key, value))
            
        while True:
            
            if(fail_user):
                print("\n(Select an available number)")

            #Validate the value entered by the user
            try:
                choice = float(input("\nSelect provider number: "))
            except ValueError:
                fail_user = True
                #Continue with program logic
                continue
                
            #Validate the value entered by the user
            if  (choice > 0 and choice <= len(ProviderYahoo.PROVIDERS)):
                #break the while loop
                break
            else:
                fail_user = True
            
        return ProviderYahoo.PROVIDERS.get(choice)


    def get_xpath_provider_home_struc1(self):
        #Return the XPATH of your structure on the home page
        return '//a[./div/div[2]/text()="' + self.provider_name + '"]/@href'

    
    def get_xpath_provider_home_struc2(self):
        #Return the XPATH of your structure on the home page
        return '//div[contains(@class,"C(#959595)") and ./span[1][text()="' + self.provider_name + '"]]/../h3//a/@href'