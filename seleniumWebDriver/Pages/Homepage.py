from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from seleniumWebDriver.Pages.CommonPage import CommonPage


class HomePage(CommonPage):

    lblPageBody = ".//*[@id='b2indexPage']"
    lblUnwantedPopup = ".//*[@role='dialog']"
    lstSpecificTabs = ".//*[@aria-label='What are you looking for?']"
    lblSelectCurrency = ".//div[@aria-label='Select your currency']"
    lblSelectLanguage = ".//div[@data-testid='selection-modal']"
    lblSearchBoxes = ".//div[@class='hero-banner-searchbox']"
    lblDatePicker = "//div[@data-testid='searchbox-datepicker-calendar']"

    '''
    created By: Shivam Ojha
    since: 05 Sept 2023
    desc: This constructor method will set default filter of home page whenever it is called OR class object created
    return: none
    param: none
    '''
    def __init__(self):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblPageBody)
        #self.closeUnwantedPopup()
        self.driver.find_element(By.XPATH,".//*[@data-testid='header-language-picker-trigger']").click()
        self.clickOnSpecificLanguageOnSelectLanguagePopup("English (US)")
        self.waitUntilPageRefreshed()
        self.driver.find_element(By.XPATH,".//*[@data-testid='header-currency-picker-trigger']").click()
        self.clickOnSpecificCurrencyOnSelectCurrencyPopup("Indian Rupee")
        self.waitUntilPageRefreshed()

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
        wait = WebDriverWait(self.driver,20)
        wait.until(expected_conditions.invisibility_of_element(self.driver.find_element(By.XPATH,self.lblUnwantedPopup)))
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

    '''
      created By: Shivam Ojha
      since: 13 Aug 2023
      desc: This method is used to click On Select Location Input Box
      param: none
      return: none
      '''
    def clickOnSelectLocationInputBox(self):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblSearchBoxes)
        self.driver.find_element(By.XPATH,self.lblSearchBoxes+"//input[@name='ss']").click()

    '''
      created By: Shivam Ojha
      since: 13 Aug 2023
      desc: This method is used to search And Select Location
      param: locationName
      return: none
      '''
    def searchAndSelectLocation(self,locationName):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblSearchBoxes)
        self.driver.find_element(By.XPATH,self.lblSearchBoxes+"//input[@name='ss']").send_keys(locationName)
        self.waitUntilPageReady(self.lblSearchBoxes+"//ul[@data-testid]")
        self.driver.find_element(By.XPATH,self.lblSearchBoxes+"//ul[@data-testid]/li//div[text()='"+locationName+"']").click()

    '''
      created By: Shivam Ojha
      since: 13 Aug 2023
      desc: This method is used to verify Location Selected
      param: nameToVerify
      return: boolean
      '''
    def verifyLocationSelected(self,nameToVerify):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblSearchBoxes)
        return self.driver.find_element(By.XPATH,self.lblSearchBoxes+"//input[@name='ss']").get_attribute('value').__contains__(nameToVerify)

    '''
      created By: Shivam Ojha
      since: 03 Sept 2023
      desc: This method is used to click On select date Input Box
      param: none
      return: none
      '''
    def clickOnSelectDateInputBox(self):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblSearchBoxes)
        self.driver.find_element(By.XPATH,self.lblSearchBoxes+"//div[@data-testid='searchbox-dates-container']").click()

    '''
      created By: Shivam Ojha
      since: 03 Sept 2023
      desc: This method is used to verify calender opens
      param: none
      return: boolean
      '''
    def verifyCalenderOpens(self):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblDatePicker)
        return self.driver.find_element(By.XPATH,self.lblDatePicker).is_displayed()

    '''
      created By: Shivam Ojha
      since: 03 Sept 2023
      desc: This method is used to verify Specific Month Opened On Date Picker
      param: month
      return: boolean
      '''
    def verifySpecificMonthOpenedOnDatePicker(self,month):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblDatePicker)
        return self.driver.find_element(By.XPATH,self.lblDatePicker+"//h3[contains(text(),'"+month+"')]").is_displayed()

    '''
      created By: Shivam Ojha
      since: 17 Sept 2023
      desc: This method is used to select date On Date Picker
      param: month,date
      return: none
      '''
    def selectDateOnDatePicker(self,month,date):
        self.waitUntilPageRefreshed()
        flag = False
        elementDisplayed = False
        self.waitUntilPageReady(self.lblDatePicker)
        while(flag==False):
            try:
                elementDisplayed = self.driver.find_element(By.XPATH, self.lblDatePicker + "//h3[contains(text(),'" + month + "')]").is_displayed()
            except NoSuchElementException:
                elementDisplayed = False
            if(elementDisplayed):
                flag = True
                self.driver.find_element(By.XPATH,self.lblDatePicker+"//h3[contains(text(),'"+month+"')]/parent::div//tr/td/span/span[text()='"+date+"']").click()
            else:
                self.driver.find_element(By.XPATH,self.lblDatePicker+"//button[last()]").click()

    '''
      created By: Shivam Ojha
      since: 17 Sept 2023
      desc: This method is used to verify date selected On Date Picker
      param: dataToVerify
      return: boolean
      '''
    def verifySpecificDateSelected(self,dataToVerify):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblSearchBoxes)
        actualData =  self.driver.find_element(By.XPATH,self.lblSearchBoxes+"//div[@data-testid='searchbox-dates-container']").text
        return actualData.strip().replace("\n","").__contains__(dataToVerify)