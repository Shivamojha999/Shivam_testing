import datetime
import sys

from dateutil.relativedelta import relativedelta

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
    def waitUntilPageReady(self, xpathOfElement):
        self.driver.implicitly_wait(20)
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.visibility_of(self.driver.find_elements(By.XPATH, xpathOfElement)[0]))

    '''
    created By: Shivam Ojha
    since: 18 July 2023
    desc: This method is used to hover on any element
    param: element
    return: none
    '''
    def hoverTo(self, element):
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
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, "*")))
        # WebDriverWait(driver, 10).until(lambda driver: driver.refreshed)

    '''
    created By: Shivam Ojha
    since: 18 July 2023
    desc: This method is used to wait Until Frame Load And Switch
    param: xpathOfFrame
    return: none
    '''
    def waitUntilFrameLoadAndSwitch(self, xpathOfFrame):
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.frame_to_be_available_and_switch_to_it(
            self.driver.find_element(By.XPATH, xpathOfFrame)))

    '''
    created By: Shivam Ojha
    since: 18 July 2023
    desc: This method is used to get Current Date In Specific Fromat
    return: String
    param: format
    '''
    def getCurrentDate(self, format):
        return datetime.date.today().strftime(format)

    '''
    created By: Shivam Ojha
    since: 23 July 2023
    desc: This method is used to get Past Future Date By Days In Specific Fromat
    return: String
    param: format,days,pastFuture
    '''
    def getPastFutureDateByDays(self, format, days, pastFuture):
        if (pastFuture == "f" or pastFuture == "F"):
            futureDate = datetime.date.today() + datetime.timedelta(days=days)
            return futureDate.strftime(format)
        elif (pastFuture == "p" or pastFuture == "P"):
            pastDate = datetime.date.today() - datetime.timedelta(days=days)
            return pastDate.strftime(format)
        else:
            return None

    '''
    created By: Shivam Ojha
    since: 23 July 2023
    desc: This method is used to get Past Future Date By Months In Specific Fromat
    return: String
    param: format,month,pastFuture
    '''
    def getPastFutureDateByMonths(selfformat, format, month, pastFuture):
        if (pastFuture == "f" or pastFuture == "F"):
            futureDate = datetime.date.today() + relativedelta(months=month)
            return futureDate.strftime(format)
        elif (pastFuture == "p" or pastFuture == "P"):
            pastDate = datetime.date.today() - relativedelta(months=month)
            return pastDate.strftime(format)
        else:
            return None

    '''
    created By: Shivam Ojha
    since: 23 July 2023
    desc: This method is used to get Past Future Date By Years In Specific Fromat
    return: String
    param: format,year,pastFuture
    '''
    def getPastFutureDateByYears(selfformat, format, year, pastFuture):
        if (pastFuture == "f" or pastFuture == "F"):
            futureDate = datetime.date.today() + relativedelta(years=year)
            return futureDate.strftime(format)
        elif (pastFuture == "p" or pastFuture == "P"):
            pastDate = datetime.date.today() - relativedelta(years=year)
            return pastDate.strftime(format)
        else:
            return None

    '''
    created By: Shivam Ojha
    since: 05 Sept 2023
    desc: This method is used to hard refresh any page
    return: none
    param: none
    '''
    def hardRefresh(self):
        self.driver.refresh()

    '''
    created By: Shivam Ojha
    since: 24 Sept 2023
    desc: This method is used to scroll Using Java script
    param: xpathOfElements, targetText
    return: webElement
    '''
    def scrollUsingJs(self, xpathOfElements, targetText):
        self.waitUntilPageRefreshed()
        elements = self.driver.find_elements(By.XPATH, xpathOfElements)
        for i in range(len(elements)):
            self.driver.execute_script("arguments[0].scrollIntoView(false);", elements[i])
            if (elements[i].text.__contains__(targetText)):
                return elements[i]
        return None

    '''
      created By: Shivam Ojha
      since: 04 Oct 2023
      desc: This method is used to navigate To HomePage
      param: none
      return: none
      '''
    def navigateToHomePage(self):
        self.waitUntilPageRefreshed()
        self.waitUntilPageReady(".//span[@data-testid='header-logo']")
        self.driver.find_element(By.XPATH,".//span[@data-testid='header-logo']").click()

    '''
      created By: Shivam Ojha
      since: 15 Feb 2024
      desc: This method is used to save Screen Shots
      param: none
      return: none
      '''
    def saveScreenShots(self,nameOfTestCase):
        screenshot_path = "ScreenShots/"+nameOfTestCase+".png"
        self.driver.save_screenshot(screenshot_path)

