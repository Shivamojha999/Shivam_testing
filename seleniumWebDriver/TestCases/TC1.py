import unittest

from seleniumWebDriver.Pages.Homepage import HomePage


class FirstTestCase(unittest.TestCase,HomePage):

    def setUp(self):
        self.launchUrl()
        self.maximizeWindow()

    def tearDown(self):
        pass
        #self.driver.quit()

    def test1_VerifySignInPopup(self):
        homepage = HomePage
        self.assertTrue(homepage.verifyHomePageTitle(self,homepage.getTitleOfPage(self)))
        self.assertTrue(homepage.verifyUnwantedPopup(self))
        homepage.closeUnwantedPopup(self)
        self.assertTrue(homepage.verifyUnwantedPopupClosed(self))

    def test2_VerifyAllTabsVisibleOnMainPage(self):
        homepage = HomePage
        #homepage.closeUnwantedPopup(self)
        self.assertTrue(homepage.verifySpecificTravelOptionsDisplayed(self,"Stays"))
        self.assertTrue(homepage.verifySpecificTravelOptionsDisplayed(self,"Flights"))
        self.assertTrue(homepage.verifySpecificTravelOptionsDisplayed(self,"Flight + Hotel"))
        self.assertTrue(homepage.verifySpecificTravelOptionsDisplayed(self,"Car rentals"))
        self.assertTrue(homepage.verifySpecificTravelOptionsDisplayed(self,"Attractions"))
        self.assertTrue(homepage.verifySpecificTravelOptionsDisplayed(self,"Airport taxis"))

    if __name__ == '__main__':
        unittest.main()
