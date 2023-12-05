import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from matplotlib.colors import to_hex

from seleniumWebDriver.Pages.CommonPage import CommonPage


class FlightsPage(CommonPage):

    lblFlights = ".//*[@id='root']"
    lblHeaderOptions = ".//header[contains(@class,'Header-module')]"
    lblAdultPopup = ".//*[contains(@data-ui-name,'occupancy')]//label"
    lstItems = ".//div[@data-ui-name='segments_list_item']"
    txtSearchLocation = ".//input[@placeholder='Airport or city']"
    lstSearchOptions = ".//*[@id='flights-searchbox_suggestions']"
    lblSearchResults = ".//div[@data-testid='searchresults_list']"

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

    '''
    created By: Shivam Ojha
    since: 20 Nov 2023
    desc: This method is used to verify Color Of Specific Button In Flight Page
    param: button,color
    return: boolean
    '''
    def verifyColorOfSpecificButtonInFlightPage(self,button,color):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblFlights)
        rgba_string = self.driver.find_element(By.XPATH,self.lblFlights+"//button/span[contains(text(),'"+button+"')]").value_of_css_property('color')
        rgba_values=[]
        for value in re.findall(r'\d+\.\d+|\d+', rgba_string):
            rgba_values.append(float(value)/255.0)
        return to_hex(rgba_values[:-1]).__eq__(color)

    '''
    created By: Shivam Ojha
    since: 05 Dec 2023
    desc: This method is used to click On Specific From To Text Box
    param: optionFromTo
    return: none
    '''
    def clickOnSpecificFromToTextBox(self,optionFromTo):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lstItems)
        self.driver.find_element(By.XPATH,self.lstItems+"//button[contains(@data-ui-name,'input_location_"+optionFromTo.lower()+"_segment')]").click()

    '''
    created By: Shivam Ojha
    since: 05 Dec 2023
    desc: This method is used to click On Cross Icon For Specific Location
    param: locationName
    return: none
    '''
    def clickOnCrossIconForSpecificLocation(self,locationName):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.txtSearchLocation+"/parent::div")
        self.driver.find_element(By.XPATH,self.txtSearchLocation+"/parent::div/span/span[contains(text(),"+locationName+")]/following-sibling::span").click()

    '''
    created By: Shivam Ojha
    since: 05 Dec 2023
    desc: This method is used to search Location
    param: searchOption
    return: none
    '''
    def searchLocation(self,searchOption):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.txtSearchLocation+"/parent::div")
        self.driver.find_element(By.XPATH,self.txtSearchLocation).send_keys(searchOption)

    '''
    created By: Shivam Ojha
    since: 05 Dec 2023
    desc: This method is used to select Location
    param: locationName
    return: none
    '''
    def selectLocation(self,locationName):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lstSearchOptions)
        self.driver.find_element(By.XPATH,self.lstSearchOptions+"//li//b[text()='"+locationName+"']").click()

    '''
    created By: Shivam Ojha
    since: 05 Dec 2023
    desc: This method is used to search and select Location
    param: optionFromTo,searchOption
    return: none
    '''
    def searchAndSelectSpecificLocation(self,optionFromTo,searchOption):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lstItems)
        self.clickOnSpecificFromToTextBox(optionFromTo)
        if len(self.driver.find_elements(By.XPATH,self.txtSearchLocation+"/parent::div/span")) > 0:
            for i in range(len(self.driver.find_elements(By.XPATH,self.txtSearchLocation+"/parent::div/span"))):
                location = self.driver.find_element(By.XPATH,self.txtSearchLocation+"/parent::div/span["+str(i+1)+"]/span/b").text
                self.clickOnCrossIconForSpecificLocation(location)
        self.searchLocation(searchOption)
        self.selectLocation(searchOption)

    '''
    created By: Shivam Ojha
    since: 05 Dec 2023
    desc: This method is used to verify search results displayed
    param: none
    return: boolean
    '''
    def verifySearchResultsDsplayed(self):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblSearchResults)
        return self.driver.find_element(By.XPATH,self.lblSearchResults).is_displayed()