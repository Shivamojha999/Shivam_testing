from selenium.webdriver.common.by import By

from seleniumWebDriver.Pages.CommonPage import CommonPage


class FlightsPage(CommonPage):

    lblFlights = ".//*[@id='root']"
    lblHeaderOptions = ".//header[contains(@class,'Header-module')]"

    '''
    created By: Shivam Ojha
    since: 05 oct 2023
    desc: This constructor method will set wait for the Flight loads
    param: none
    return: none
    '''
    def __init__(self):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblFlights)
        self.driver.find_element(By.XPATH,self.lblFlights+"//h1[contains(text(),'Compare and book flights with ease')]").is_displayed()

    '''
    created By: Shivam Ojha
    since: 05 oct 2023
    desc: This method is used to verify Specific Header Option Get Selected
    param: optionName
    return: boolean
    '''
    def verifySpecificHeaderOptionGetSelected(self,optionName):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblHeaderOptions)
        return self.driver.find_element(By.XPATH,self.lblHeaderOptions+"//ul//span[contains(text(),'"+optionName+"')]/parent::div/parent::span/parent::a/parent::li").get_attribute("class").__contains__("selected")

    '''
    created By: Shivam Ojha
    since: 15 oct 2023
    desc: This method is used to verify Specific Radio Button
    param: name
    return: boolean
    '''
    def verifySpecificRadioButton(self,name):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblFlights)
        return len(self.driver.find_elements(By.XPATH,self.lblFlights+"//fieldset//label//div[text()='"+name+"']/parent::span/parent::label/preceding-sibling::input[@type='radio']")) == 1

