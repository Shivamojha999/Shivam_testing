from selenium.webdriver.common.by import By

from seleniumWebDriver.Pages.CommonPage import CommonPage


class HomePage(CommonPage):

    lblPageBody = ".//*[@id='b2indexPage']"
    lblUnwantedPopup = ".//*[@role='dialog']"
    lstSpecificTabs = ".//*[@aria-label='What are you looking for?']"
    lblSelectCurrency = ".//div[@aria-label='Select your currency']"
    lblSelectLanguage = ".//div[@data-testid='selection-modal']"

    '''
    created By: Shivam Ojha
    since: 01 July 2023
    desc: This method is used to get title of the page
    param: none
    return: string
    '''
    def getTitleOfPage(self):
        self.waitUntilPageRefreshed()
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
        self.waitUntilPageRefreshed()
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
        self.waitUntilPageRefreshed()
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
        self.waitUntilPageRefreshed()
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
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblPageBody)
        return len(self.driver.find_elements(By.XPATH,self.lblUnwantedPopup)) == 0

    '''
    created By: Shivam Ojha
    since: 01 July 2023
    desc: This method is used to verify Specific Travel Option Displayed
    param: tabName
    return: boolean
    '''
    def verifySpecificTravelOptionsDisplayed(self,tabName):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lstSpecificTabs)
        element = self.driver.find_element(By.XPATH,self.lstSpecificTabs+"//div/span[contains(text(),'"+tabName+"')]")
        self.hoverTo(element)
        return element.is_displayed()

    '''
    created By: Shivam Ojha
    since: 03 July 2023
    desc: This method is used to verify Specific Button Displayed
    param: buttonName
    return: boolean
    '''
    def verifySpecificButtonDisplayed(self,buttonName):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblPageBody)
        return self.driver.find_element(By.XPATH,self.lblPageBody+"//button/span[contains(text(),'"+buttonName+"')]").is_displayed()

    '''
    created By: Shivam Ojha
    since: 03 July 2023
    desc: This method is used to click on Specific Button
    param: buttonName
    return: none
    '''
    def clickOnSpecificButton(self,buttonName):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblPageBody)
        self.driver.find_element(By.XPATH,self.lblPageBody+"//button/span[contains(text(),'"+buttonName+"')]").click()

    '''
    created By: Shivam Ojha
    since: 03 July 2023
    desc: This method is used to verify Specific Area Label
    param: labelName
    return: boolean
    '''
    def verifySpecificAreaLabel(self,labelName,tagName="button"):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblPageBody)
        return self.driver.find_element(By.XPATH,self.lblPageBody+"//"+tagName+"[@aria-label='"+labelName+"']").is_displayed()

    '''
    created By: Shivam Ojha
    since: 03 July 2023
    desc: This method is used to click on Specific Area Label
    param: labelName
    return: none
    '''
    def clickOnSpecificAreaLabel(self,labelName,tagName="button"):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblPageBody)
        self.driver.find_element(By.XPATH,self.lblPageBody+"//"+tagName+"[@aria-label='"+labelName+"']").click()

    '''
   created By: Shivam Ojha
   since: 03 July 2023
   desc: This method is used to verify Specific Currency On Select Currency Popup
   param: currencyName
   return: boolean
   '''
    def verifySpecificCurrencyOnSelectCurrencyPopup(self,currencyName):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblSelectCurrency)
        elements = len(self.driver.find_elements(By.XPATH,self.lblSelectCurrency+"//ul/li//span"))
        for i in range(elements):
            self.hoverTo(self.driver.find_elements(By.XPATH,self.lblSelectCurrency+"//ul/li//span")[i])
            if(self.driver.find_elements(By.XPATH,self.lblSelectCurrency+"//ul/li//span")[i].text.__contains__(currencyName)):
                return self.driver.find_element(By.XPATH,self.lblSelectCurrency+"//ul/li//span[contains(text(),'"+currencyName+"')]").is_displayed()
        return False

    '''
      created By: Shivam Ojha
      since: 03 July 2023
      desc: This method is used to click on Specific Currency On Select Currency Popup
      param: currencyName
      return: none
      '''
    def clickOnSpecificCurrencyOnSelectCurrencyPopup(self,currencyName):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblSelectCurrency)
        elements = len(self.driver.find_elements(By.XPATH,self.lblSelectCurrency+"//ul/li//span"))
        for i in range(elements):
            self.hoverTo(self.driver.find_elements(By.XPATH,self.lblSelectCurrency+"//ul/li//span")[i])
            if(self.driver.find_elements(By.XPATH,self.lblSelectCurrency+"//ul/li//span")[i].text.__contains__(currencyName)):
                self.driver.find_element(By.XPATH,self.lblSelectCurrency+"//ul/li//span[contains(text(),'"+currencyName+"')]").click()
                break
        self.waitUntilPageRefreshed()

    '''
      created By: Shivam Ojha
      since: 10 July 2023
      desc: This method is used to verify Specific language On Select language Popup
      param: languageName
      return: boolean
      '''
    def verifySpecificLanguageOnSelectLanguagePopup(self,languageName):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblSelectLanguage)
        elements = len(self.driver.find_elements(By.XPATH,self.lblSelectLanguage+"//ul/li//span"))
        for i in range(elements):
            self.hoverTo(self.driver.find_elements(By.XPATH,self.lblSelectLanguage+"//ul/li//span")[i])
            if(self.driver.find_elements(By.XPATH,self.lblSelectLanguage+"//ul/li//span")[i].text.__contains__(languageName)):
                return self.driver.find_element(By.XPATH,self.lblSelectLanguage+"//ul/li//span[contains(text(),'"+languageName+"')]").is_displayed()
        return False

    '''
      created By: Shivam Ojha
      since: 10 July 2023
      desc: This method is used to click on Specific language On Select language Popup
      param: languageName
      return: none
      '''
    def clickOnSpecificLanguageOnSelectLanguagePopup(self,languageName):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblSelectLanguage)
        elements = len(self.driver.find_elements(By.XPATH,self.lblSelectLanguage+"//ul/li//span"))
        for i in range(elements):
            self.hoverTo(self.driver.find_elements(By.XPATH,self.lblSelectLanguage+"//ul/li//span")[i])
            if(self.driver.find_elements(By.XPATH,self.lblSelectLanguage+"//ul/li//span")[i].text.__contains__(languageName)):
                self.driver.find_element(By.XPATH,self.lblSelectLanguage+"//ul/li//span[contains(text(),'"+languageName+"')]").click()
                break
        self.waitUntilPageRefreshed()