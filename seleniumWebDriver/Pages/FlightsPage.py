from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from seleniumWebDriver.Pages.CommonPage import CommonPage


class FlightsPage(CommonPage):

    lblFlights = ".//*[@id='root']"
    lblHeaderOptions = ".//header[contains(@class,'Header-module')]"
    lblAdultPopup = ".//*[contains(@data-ui-name,'occupancy')]//label"

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

    '''
    created By: Shivam Ojha
    since: 29 oct 2023
    desc: This method is used to verify Specific option for class dropdown
    param: optionName
    return: boolean
    '''
    def verifySpecificOptionOfClassDropdown(self,optionName):
        self.waitUntilPageRefreshed()
        flag = False
        self.waitUntilPageReady(self.lblFlights)
        select = Select(self.driver.find_element(By.XPATH,self.lblFlights+"//select[@title='Cabin class']"))
        for i in range(len(select.options)):
            if not select.options[i].text.__eq__(optionName):
                flag = False
            else:
                return True
        return flag

    '''
    created By: Shivam Ojha
    since: 29 oct 2023
    desc: This method is used to verify Specific Option Selected In Class Dropdown
    param: selectedOption
    return: boolean
    '''
    def verifySpecificOptionSelectedInClassDropdown(self,selectedOption):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblFlights)
        select = Select(self.driver.find_element(By.XPATH,self.lblFlights+"//select[@title='Cabin class']"))
        return select.first_selected_option.text.__eq__(selectedOption)

    '''
    created By: Shivam Ojha
    since: 29 oct 2023
    desc: This method is used to select Specific Option In Class Dropdown
    param: option
    return: none
    '''
    def selectSpecificOptionInClassDropdown(self,option):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblFlights)
        select = Select(self.driver.find_element(By.XPATH,self.lblFlights+"//select[@title='Cabin class']"))
        select.select_by_visible_text(option)

    '''
    created By: Shivam Ojha
    since: 18 Nov 2023
    desc: This method is used to click On Specific Button In Flight Page
    param: button
    return: none
    '''
    def clickOnSpecificButtonInFlightPage(self,button):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblFlights)
        self.driver.find_element(By.XPATH,self.lblFlights+"//button/span[contains(text(),'"+button+"')]").click()

    '''
    created By: Shivam Ojha
    since: 18 Nov 2023
    desc: This method is used to click On Plus Minus Button Of Specific Option On Adult Popup
    param: optionName,button
    return: none
    '''
    def clickOnPlusMinusButtonOfSpecificOptionOnAdultPopup(self,optionName,button="plus"):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblAdultPopup)
        self.driver.find_element(By.XPATH,self.lblAdultPopup+"[contains(text(),'"+optionName+"')]/parent::div/following-sibling::div/button[contains(@data-ui-name,'"+button+"')]").click()

    '''
    created By: Shivam Ojha
    since: 18 Nov 2023
    desc: This method is used to get Value Of Specific Option On Adult Popup
    param: optionName
    return: string
    '''
    def getValueOfSpecificOptionOnAdultPopup(self,optionName):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblAdultPopup)
        return self.driver.find_element(By.XPATH,self.lblAdultPopup+"[contains(text(),'"+optionName+"')]/parent::div/parent::div//span[contains(@class,'InputStepper')]").text
