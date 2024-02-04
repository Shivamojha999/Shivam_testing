import unittest

from seleniumWebDriver.Pages.Homepage import HomePage
from seleniumWebDriver.Pages.SearchResultStaysPage import SearchResultStaysPage


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

    '''def test2_VerifyAllTabsVisibleOnMainPage(self):
        homepage = HomePage()
        self.assertTrue(homepage.verifySpecificTravelOptionsDisplayed("Stays"))
        self.assertTrue(homepage.verifySpecificTravelOptionsDisplayed("Flights"))
        self.assertTrue(homepage.verifySpecificTravelOptionsDisplayed("Flight + Hotel"))
        self.assertTrue(homepage.verifySpecificTravelOptionsDisplayed("Car rentals"))
        self.assertTrue(homepage.verifySpecificTravelOptionsDisplayed("Attractions"))
        self.assertTrue(homepage.verifySpecificTravelOptionsDisplayed("Airport taxis"))

    def test3_VerifyCurrencyScreenFunctionality(self):
        try:
            homepage = HomePage()
            self.assertTrue(homepage.verifySpecificButtonDisplayed("INR"))
            homepage.clickOnSpecificButton("INR")
            self.assertTrue(homepage.verifySpecificAreaLabel("Select your currency","div"))
            self.assertTrue(homepage.verifySpecificCurrencyOnSelectCurrencyPopup("Hong Kong Dollar"))
            self.assertTrue(homepage.verifySpecificCurrencyOnSelectCurrencyPopup("United Arab Emirates Dirham"))
            homepage.clickOnSpecificCurrencyOnSelectCurrencyPopup("United Arab Emirates Dirham")
            self.assertTrue(homepage.verifySpecificAreaLabel("Prices in United Arab Emirates Dirham"))
            homepage.clickOnSpecificButton("AED")
            self.assertTrue(homepage.verifySpecificCurrencyOnSelectCurrencyPopup("Hong Kong Dollar"))
            homepage.clickOnSpecificCurrencyOnSelectCurrencyPopup("New Taiwan Dollar")
            self.assertTrue(homepage.verifySpecificButtonDisplayed("TWD"))
        finally:
            self.hardRefresh()
            HomePage()

    def test4_VerifySelectLanguageScreenFunctionality(self):
        try:
            homepage = HomePage()
            self.assertTrue(homepage.verifySpecificAreaLabel("Language: English (US)"))
            homepage.clickOnSpecificAreaLabel("Language: English (US)")
            self.assertTrue(homepage.verifySpecificAreaLabel("Select your language","div"))
            self.assertTrue(homepage.verifySpecificLanguageOnSelectLanguagePopup("Íslenska"))
            homepage.clickOnSpecificLanguageOnSelectLanguagePopup("Íslenska")
            self.assertTrue(homepage.verifySpecificAreaLabel("Tungumál: Íslenska"))
            homepage.clickOnSpecificAreaLabel("Tungumál: Íslenska")
            self.assertTrue(homepage.verifySpecificLanguageOnSelectLanguagePopup("हिन्दी"))
            homepage.clickOnSpecificLanguageOnSelectLanguagePopup("हिन्दी")
            self.assertTrue(homepage.verifySpecificAreaLabel("भाषा: हिन्दी"))
        finally:
            self.hardRefresh()
            HomePage()

    def test5_VerifyDatesApiWorking(self):
        homepage = HomePage()
        homepage.getCurrentDate("%y/%m/%d")
        homepage.getCurrentDate("%#d")
        homepage.getPastFutureDateByDays("%Y-%m-%d",1,"p")
        homepage.getPastFutureDateByMonths("%Y-%m-%d",1,"f")
        homepage.getPastFutureDateByYears("%Y-%m-%d",1,"p")

    def test6_VerifyFunctionalityOfWhereToGoSearchBox(self):
        homepage = HomePage()
        homepage.clickOnSelectLocationInputBox()
        homepage.searchAndSelectLocation("Lucknow")
        self.assertTrue(homepage.verifyLocationSelected("Lucknow"))

    def test7_VerifyCalenderDesign(self):
        homepage = HomePage()
        currentMonth = homepage.getCurrentDate("%B")
        futureMonth = homepage.getPastFutureDateByMonths("%B",1,"f")
        homepage.clickOnSelectDateInputBox()
        self.assertTrue(homepage.verifyCalenderOpens())
        self.assertTrue(homepage.verifySpecificMonthOpenedOnDatePicker(currentMonth))
        self.assertTrue(homepage.verifySpecificMonthOpenedOnDatePicker(futureMonth))

    def test8_SelectDateVerification(self):
        homepage = HomePage()
        futureMonth = homepage.getPastFutureDateByMonths("%B",3,"f")
        futureDate = homepage.getPastFutureDateByMonths("%#d",3,"f")
        futureDateByDay = homepage.getPastFutureDateByDays("%#d",95,"f")
        homepage.clickOnSelectDateInputBox()
        homepage.selectDateOnDatePicker(futureMonth,futureDate)
        homepage.selectDateOnDatePicker(futureMonth,futureDateByDay)
        futureDateFormatted = homepage.getPastFutureDateByMonths("%b %#d",3,"f")
        self.assertTrue(homepage.verifySpecificDateSelected(futureDateFormatted))

    def test9_VerifySearchFunctionality(self):
        homepage = HomePage()
        homepage.clickOnSelectLocationInputBox()
        homepage.searchAndSelectLocation("Goa")
        futureMonth = homepage.getPastFutureDateByMonths("%B",1,"f")
        futureDate = homepage.getPastFutureDateByMonths("%#d",1,"f")
        futureDateByDay = homepage.getPastFutureDateByDays("%#d",35,"f")
        homepage.selectDateOnDatePicker(futureMonth,futureDate)
        homepage.selectDateOnDatePicker(futureMonth,futureDateByDay)
        homepage.clickOnSearchButton()
        searchResultStaysPage = SearchResultStaysPage()
        self.assertTrue(searchResultStaysPage.verifySearchedCityDisplayed("Goa"))'''
