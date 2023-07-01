from selenium.webdriver.common.by import By

from seleniumWebDriver.Pages.CommonPage import CommonPage


class HomePage(CommonPage):

    lblPageBody = ".//*[@id='b2indexPage']"
    lblUnwantedPopup = ".//*[@role='dialog']"
    lstSpecificTabs = "//*[@aria-label='What are you looking for?']"

    '''
    created By: Shivam Ojha
    since: 01 July 2023
    desc: This method is used to get title of the page
    param: none
    return: string
    '''
    def getTitleOfPage(self):
        self.waitUntilPageReady(self.lblPageBody)
        return self.driver.title

    '''
    @created By: Shivam Ojha
    @since: 01 July 2023
    @desc: This method is used to verify title of the page
    @param: pageTitle
    @return: boolean
    '''
    def verifyHomePageTitle(self,pageTitle):
        self.waitUntilPageReady(self.lblPageBody)
        title = self.driver.title
        return title.__contains__(pageTitle)

    '''
    created By: Shivam Ojha
    since: 01 July 2023
    desc: This method is used to close Unwanted Popup
    param: elementTag
    return: none
    '''
    def closeUnwantedPopup(self,elementTag="button"):
        self.waitUntilPageReady(self.lblUnwantedPopup)
        self.driver.find_element(By.XPATH,self.lblUnwantedPopup+"//"+elementTag).click()

    '''
    created By: Shivam Ojha
    since: 01 July 2023
    desc: This method is used to verify Unwanted Popup displayed
    param: elementTag
    return: boolean
    '''
    def verifyUnwantedPopup(self):
        self.waitUntilPageReady(self.lblUnwantedPopup)
        return self.driver.find_element(By.XPATH,self.lblUnwantedPopup).is_displayed()

    '''
    created By: Shivam Ojha
    since: 01 July 2023
    desc: This method is used to verify Unwanted Popup closed
    param: none
    return: boolean
    '''
    def verifyUnwantedPopupClosed(self):
        self.waitUntilPageReady(self.lblPageBody)
        return self.driver.find_element(By.XPATH,self.lblUnwantedPopup).is_displayed()

    '''
    created By: Shivam Ojha
    since: 01 July 2023
    desc: This method is used to verify Specific Travel Option Displayed
    param: tabName
    return: boolean
    '''
    def verifySpecificTravelOptionsDisplayed(self,tabName):
        self.waitUntilPageReady(self.lstSpecificTabs)
        element = self.driver.find_element(By.XPATH,self.lstSpecificTabs+"//div/span[contains(text(),'"+tabName+"')]")
        self.hoverTo(element)
        return element.is_displayed()