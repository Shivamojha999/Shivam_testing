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
        action.move_to_element(element).perform()

    def waitUntilPageRefreshed(self):
        # Wait for the page to be refreshed
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, "*")))
        #WebDriverWait(driver, 10).until(lambda driver: driver.refreshed)

    def waitUntilFrameLoadAndSwitch(self,xpathOfFrame):
        wait = WebDriverWait(self.driver,20)
        wait.until(expected_conditions.frame_to_be_available_and_switch_to_it(self.driver.find_element(By.XPATH,xpathOfFrame)))