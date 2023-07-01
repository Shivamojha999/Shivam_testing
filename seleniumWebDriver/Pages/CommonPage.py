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

    def waitUntilPageReady(self,xpathOfElement):
        self.driver.implicitly_wait(20)
        wait = WebDriverWait(self.driver,20)
        wait.until(expected_conditions.visibility_of(self.driver.find_element(By.XPATH,xpathOfElement)))
        self.driver.implicitly_wait(0)

    def hoverTo(self,element):
        action = ActionChains(self.driver)
        action.move_to_element(element)