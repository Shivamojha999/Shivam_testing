from datetime import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from seleniumWebDriver.webDriver.Interface import Interface


class CommonPage(Interface):

    def launchUrl(self):
        self.driver.get("https://www.booking.com/")

    def maximizeWindow(self):
        self.driver.maximize_window()

    '''
    created By: Shivam Ojha
    since: 18 July 2023
    desc: This method is used to wait until element visible
    param: xpathOfElement
    return: none
    '''
    def waitUntilPageReady(self,xpathOfElement):
        self.driver.implicitly_wait(20)
        wait = WebDriverWait(self.driver,20)
        wait.until(expected_conditions.visibility_of(self.driver.find_element(By.XPATH,xpathOfElement)))
        self.driver.implicitly_wait(0)

    '''
    created By: Shivam Ojha
    since: 18 July 2023
    desc: This method is used to hover on any element
    param: element
    return: none
    '''
    def hoverTo(self,element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    '''
    created By: Shivam Ojha
    since: 18 July 2023
    desc: This method is used to wait Until page refreshed OR wait till all the elements of page loaded
    param: none
    return: none
    '''
    def waitUntilPageRefreshed(self):
        # Wait for the page to be refreshed
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, "*")))
        #WebDriverWait(driver, 10).until(lambda driver: driver.refreshed)

    '''
    created By: Shivam Ojha
    since: 18 July 2023
    desc: This method is used to wait Until Frame Load And Switch
    param: xpathOfFrame
    return: none
    '''
    def waitUntilFrameLoadAndSwitch(self,xpathOfFrame):
        wait = WebDriverWait(self.driver,20)
        wait.until(expected_conditions.frame_to_be_available_and_switch_to_it(self.driver.find_element(By.XPATH,xpathOfFrame)))

    '''
    created By: Shivam Ojha
    since: 18 July 2023
    desc: This method is used to get Current Date In Specific Fromat
    return: String
    param: format
    %a: The abbreviated weekday name.
    %A: The full weekday name.
    %b: The abbreviated month name.
    %B: The full month name.
    %c: The complete date and time, in local format.
    %d: The day of the month, as a zero-padded decimal number.
    %e: The day of the month, as a decimal number.
    %f: The microsecond, as a decimal number.
    %H: The hour (24-hour clock), as a zero-padded decimal number.
    %I: The hour (12-hour clock), as a zero-padded decimal number.
    %j: The day of the year, as a zero-padded decimal number.
    %m: The month as a zero-padded decimal number.
    %M: The minute, as a zero-padded decimal number.
    %p: The locale's equivalent of either AM or PM.
    %S: The second, as a zero-padded decimal number.
    %U: The week number of the year, with Sunday as the first day of the week, as a zero-padded decimal number.
    %W: The week number of the year, with Monday as the first day of the week, as a zero-padded decimal number.
    %x: The date, in local format.
    %X: The time, in local format.
    %y: The year, as a zero-padded decimal number without a century.
    %Y: The year, as a four-digit number.
    %Z: The time zone name.
    %%: A literal % character.
    '''
    def getCurrentDate(self,format):
        current_date = datetime.today()
        formatted_date = current_date.strftime(format)
        return formatted_date