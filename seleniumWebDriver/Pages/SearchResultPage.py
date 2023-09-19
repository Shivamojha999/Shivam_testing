from selenium.webdriver.common.by import By

from seleniumWebDriver.Pages.CommonPage import CommonPage


class SearchResultPage(CommonPage):

    lblNavigator = "//nav[@aria-label='Navigation history menu (breadcrumbs)']"
    lblSearchResults = "//*[@id='basiclayout']"


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
        self.waitUntilPageReady(self.lblSearchResults)
        return self.driver.find_element(By.XPATH,self.lblSearchResults+"//h1[contains(text(),'"+cityName+"')]").is_displayed()
