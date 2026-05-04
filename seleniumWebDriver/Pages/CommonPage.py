import datetime
import os

from dateutil.relativedelta import relativedelta
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from seleniumWebDriver.webDriver.Interface import Interface


class CommonPage(Interface):

    def applyHeadlessViewport(self):
        if os.getenv("HEADLESS") == "true":
            self.driver.set_window_size(1920, 1080)
            self.driver.execute_cdp_cmd(
                "Emulation.setDeviceMetricsOverride",
                {
                    "width": 1920,
                    "height": 1080,
                    "deviceScaleFactor": 1,
                    "mobile": False,
                },
            )

    def launchUrl(self):
        self.applyHeadlessViewport()
        self.driver.get(self.bookingUrl)

    def maximizeWindow(self):
        if os.getenv("HEADLESS") != "true":
            self.driver.maximize_window()

    def waitUntilPageReady(self, xpathOfElement, timeout=None):
        wait = WebDriverWait(self.driver, timeout or self.defaultTimeout)
        return wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpathOfElement)))

    def waitUntilElementClickable(self, xpathOfElement, timeout=None):
        wait = WebDriverWait(self.driver, timeout or self.defaultTimeout)
        return wait.until(expected_conditions.element_to_be_clickable((By.XPATH, xpathOfElement)))

    def hoverTo(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def waitUntilPageRefreshed(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, "*"))
        )

    def waitUntilFrameLoadAndSwitch(self, xpathOfFrame):
        wait = WebDriverWait(self.driver, self.defaultTimeout)
        wait.until(expected_conditions.frame_to_be_available_and_switch_to_it((By.XPATH, xpathOfFrame)))

    def getCurrentDate(self, format):
        return datetime.date.today().strftime(format)

    def getPastFutureDateByDays(self, format, days, pastFuture):
        if pastFuture.lower() == "f":
            futureDate = datetime.date.today() + datetime.timedelta(days=days)
            return futureDate.strftime(format)
        if pastFuture.lower() == "p":
            pastDate = datetime.date.today() - datetime.timedelta(days=days)
            return pastDate.strftime(format)
        return None

    def getPastFutureDateByMonths(self, format, month, pastFuture):
        if pastFuture.lower() == "f":
            futureDate = datetime.date.today() + relativedelta(months=month)
            return futureDate.strftime(format)
        if pastFuture.lower() == "p":
            pastDate = datetime.date.today() - relativedelta(months=month)
            return pastDate.strftime(format)
        return None

    def getPastFutureDateByYears(self, format, year, pastFuture):
        if pastFuture.lower() == "f":
            futureDate = datetime.date.today() + relativedelta(years=year)
            return futureDate.strftime(format)
        if pastFuture.lower() == "p":
            pastDate = datetime.date.today() - relativedelta(years=year)
            return pastDate.strftime(format)
        return None

    def hardRefresh(self):
        self.driver.refresh()

    def scrollUsingJs(self, xpathOfElements, targetText):
        self.waitUntilPageRefreshed()
        elements = self.driver.find_elements(By.XPATH, xpathOfElements)
        for element in elements:
            self.driver.execute_script("arguments[0].scrollIntoView(false);", element)
            if targetText in element.text:
                return element
        return None

    def navigateToHomePage(self):
        self.waitUntilPageRefreshed()
        self.waitUntilElementClickable(".//span[@data-testid='header-logo']").click()

    def saveScreenShots(self, nameOfTestCase):
        projectPath = os.getcwd()
        screenShotsDir = os.path.join(projectPath, "ScreenShots")
        os.makedirs(screenShotsDir, exist_ok=True)
        screenshotPath = os.path.join(screenShotsDir, f"{nameOfTestCase}.png")
        self.driver.save_screenshot(screenshotPath)
        return screenshotPath

    def saveScreenShotsOnCleanUp(self, nameOfTestCase):
        return self.saveScreenShots(nameOfTestCase)
