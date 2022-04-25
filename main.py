
from provider import ProviderYahoo


def main():

    provider = ProviderYahoo()

    #codigo opciones la usuario

    choise_provider = provider.choose_provider()
    print("Choice: ", choise_provider)
    xpath_provider = provider.get_links_by_xpath(choise_provider)
    print("Xpath: ", xpath_provider)

    
if __name__ == "__main__":
    
    main()