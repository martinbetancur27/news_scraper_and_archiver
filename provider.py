class ProviderYahoo():

      
    def choose_provider(self):

        #Variable that controls if the user makes a mistake when entering a number
        fail_user = False
        
        provider = {
            1: "Argus Research",
            2: "Barrons",
            3: "Bloomberg",
            4: "Financial Times",
            5: "Fortune",
            6: "Fx Empire",
            7: "Investor's Business Daily",
            8: "MarketWatch",
            9: "Morning Research",
            10: "Quartz",
            11: "Reuters",
            12: "SmartAsset",
            13: "Tech Crunch",
            14: "TipRanks",
            15: "USA TODAY",
            16: "Yahoo",
            17: "Yahoo Money"
        }
        
        while True:
            #Print in a format with good user experience
            print ("{:<5} {:<5}".format('Num', 'Provider'))

            for key, value in provider.items():
                print ("{:<5} {:<5}".format(key, value))
            
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
            if  (choice > 0 and choice <= len(provider)):
                #break the while loop
                break
            else:
                fail_user = True
            
        
        
        return provider.get(choice)

    
    def get_links_by_xpath(self, provider_name):
        
        xpath_provider = '//div[contains(@class,"C(#959595)")]/span[1][starts-with(.,"' + provider_name + '")]/../..//a/@href'
        
        return xpath_provider