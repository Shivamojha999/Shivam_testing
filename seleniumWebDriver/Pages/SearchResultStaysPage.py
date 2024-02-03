from selenium.webdriver.common.by import By

from seleniumWebDriver.Pages.CommonPage import CommonPage


class SearchResultStaysPage(CommonPage):

    lblNavigator = ".//nav[@aria-label='Navigation history menu (breadcrumbs)']"
    lblSearchResults = ".//*[@id='basiclayout']"
    lblFilters = ".//*[@id='basiclayout']/parent::div"


    '''
    created By: Shivam Ojha
    since: 19 Sept 2023
    desc: This constructor method will verify Search results displayed every time when object of the page is created
    param: none
    return: none
    '''
    def __init__(self):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblNavigator)
        self.driver.find_element(By.XPATH,self.lblNavigator+"//div[text()='Search results']").is_displayed()

    '''
    created By: Shivam Ojha
    since: 19 Sept 2023
    desc: This method is used to verify Searched City Displayed
    param: cityName
    return: boolean
    '''
    def verifySearchedCityDisplayed(self,cityName):
        self.waitUntilPageRefreshed()
        return self.driver.find_element(By.XPATH,self.lblSearchResults+"/parent::div//h1[contains(text(),'"+cityName+"')]").is_displayed()

    '''
    created By: Shivam Ojha
    since: 24 Sept 2023
    desc: This method is used to verify Specific Filter Option Displayed
    param: filterName, optionName
    return: boolean
    '''
    def verifySpecificFilterOptionDisplayed(self,filterName,optionName):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblFilters)
        self.scrollUsingJs(self.lblFilters+"//h3[text()='"+filterName+"']/parent::div/parent::div//label//div",optionName)
        return self.driver.find_element(By.XPATH,self.lblFilters+"//h3[text()='"+filterName+"']/parent::div/parent::div//label//div[contains(text(),'"+optionName+"')]").is_displayed()
