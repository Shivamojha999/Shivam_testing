from selenium.webdriver.common.by import By

from seleniumWebDriver.Pages.CommonPage import CommonPage


class CarRentalPage(CommonPage):

    lblCarRentalPage = ".//*[@id='bodyconstraint']/parent::body"
    lblTravelBar = ".//div[contains(@class,'desktop')]"
    txtFieldPickup = ".//input[@aria-label='Pick-up location']"
    lblBlueTabs = ".//*[@class='bui-tab__nav']"


    '''
    created By: Shivam Ojha
    since: 16 Mar 2024
    desc: This constructor method will set wait for the Car Rental page loads
    param: none
    return: none
    '''
    def __init__(self):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblCarRentalPage)
        self.driver.find_element(By.XPATH,self.lblCarRentalPage).is_displayed()

    '''
    created By: Shivam Ojha
    since: 16 Mar 2024
    desc: This method will verify Specific Date Field On Travel Bar
    param: fieldName
    return: boolean
    '''
    def verifySpecificDateFieldOnTravelBar(self,fieldName):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblTravelBar)
        return self.driver.find_element(By.XPATH,self.lblTravelBar+"//div[contains(@class,'sbc-fl-button__label') and text()='"+fieldName+"']").is_displayed()

    '''
    created By: Shivam Ojha
    since: 16 Mar 2024
    desc: This method will verify Specific Time Field On Travel Bar
    param: fieldName
    return: boolean
    '''
    def verifySpecificTimeFieldOnTravelBar(self,fieldName):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblTravelBar)
        return self.driver.find_element(By.XPATH,self.lblTravelBar+"//select[contains(@name,'"+fieldName+"')]").is_displayed()

    '''
    created By: Shivam Ojha
    since: 16 Mar 2024
    desc: This method will verify pickup location search Field On Travel Bar
    param: none
    return: boolean
    '''
    def verifyPickupLocationSearchField(self):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.txtFieldPickup)
        return self.driver.find_element(By.XPATH,self.txtFieldPickup).is_displayed()

    '''
    created By: Shivam Ojha
    since: 16 Mar 2024
    desc: This method will verify Specific check box On Travel Bar
    param: checkBoxName
    return: boolean
    '''
    def verifySpecificCheckBoxOnTravelBar(self,checkBoxName):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblTravelBar)
        if self.driver.execute_script("return arguments[0].displayed;",self.driver.find_elements(By.XPATH,self.lblTravelBar+"//input[@type='checkbox' and @name='"+checkBoxName+"']")[0]) == None:
            return True
        return False

    '''
    created By: Shivam Ojha
    since: 16 Mar 2024
    desc: This method will select Blue Tabs On Car Rental
    param: tebName
    return: none
    '''
    def selectBlueTabsOnCarRental(self,tebName):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(self.lblBlueTabs)
        self.driver.find_element(By.XPATH,self.lblBlueTabs+"/li//span[contains(text(),'"+tebName+"')]").click()