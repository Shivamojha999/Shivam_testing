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

    def test3_VerifyCurrencyScreenFunctionality(self):
        homepage = HomePage
        #homepage.closeUnwantedPopup(self)
        self.assertTrue(homepage.verifySpecificButtonDisplayed(self,"INR"))
        homepage.clickOnSpecificButton(self,"INR")
        self.assertTrue(homepage.verifySpecificAreaLabel(self,"Select your currency","div"))
        self.assertTrue(homepage.verifySpecificCurrencyOnSelectCurrencyPopup(self,"Hong Kong Dollar"))
        self.assertTrue(homepage.verifySpecificCurrencyOnSelectCurrencyPopup(self,"United Arab Emirates Dirham"))
        homepage.clickOnSpecificCurrencyOnSelectCurrencyPopup(self,"United Arab Emirates Dirham")
        self.assertTrue(homepage.verifySpecificAreaLabel(self,"Prices in United Arab Emirates Dirham"))
        homepage.clickOnSpecificButton(self,"AED")
        self.assertTrue(homepage.verifySpecificCurrencyOnSelectCurrencyPopup(self,"Hong Kong Dollar"))
        homepage.clickOnSpecificCurrencyOnSelectCurrencyPopup(self,"New Taiwan Dollar")
        self.assertTrue(homepage.verifySpecificButtonDisplayed(self,"TWD"))

    if __name__ == '__main__':
        unittest.main()
