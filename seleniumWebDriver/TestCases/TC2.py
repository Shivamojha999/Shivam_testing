import unittest

from seleniumWebDriver.Pages.Homepage import HomePage
from seleniumWebDriver.Pages.SearchResultPage import SearchResultPage


class SecondTestCase(unittest.TestCase,HomePage):

    def setUp(self):
        self.launchUrl()
        self.maximizeWindow()

    def tearDown(self):
        pass
        #self.driver.quit()

    def test1_VerifyFiltersOfSearchResults(self):
        homepage = HomePage()
        homepage.clickOnSelectLocationInputBox()
        homepage.searchAndSelectLocation("Goa")
        futureMonth = homepage.getPastFutureDateByMonths("%B",1,"f")
        futureDate = homepage.getPastFutureDateByMonths("%#d",1,"f")
        futureDateByDay = homepage.getPastFutureDateByDays("%#d",35,"f")
        homepage.selectDateOnDatePicker(futureMonth,futureDate)
        homepage.selectDateOnDatePicker(futureMonth,futureDateByDay)
        homepage.clickOnSearchButton()
        searchResultPage = SearchResultPage()
        self.assertTrue(searchResultPage.verifySpecificFilterOptionDisplayed("City","Old Goa"))
