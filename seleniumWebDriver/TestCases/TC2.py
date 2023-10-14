import unittest

from seleniumWebDriver.Pages.FlightsPage import FlightsPage
from seleniumWebDriver.Pages.Homepage import HomePage
from seleniumWebDriver.Pages.SearchResultStaysPage import SearchResultStaysPage


class SecondTestCase(unittest.TestCase,HomePage):

    def setUp(self):
        self.launchUrl()
        self.maximizeWindow()

    def tearDown(self):
        pass
        #self.driver.quit()

    def test1_VerifyFiltersOfSearchResults(self):
        try:
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
            self.assertTrue(searchResultStaysPage.verifySpecificFilterOptionDisplayed("City","Old Goa"))
        finally:
            self.hardRefresh()
            self.navigateToHomePage()


    def test2_VerifyMembersCountChanges(self):
        try:
            homepage = HomePage()
            homepage.clickOnMembersInputBox()
            adultsCount = homepage.getSpecificMemberCount("Adults")
            childrenCount = homepage.getSpecificMemberCount("Children")
            roomsCount = homepage.getSpecificMemberCount("Rooms")
            homepage.clickOnSpecificMemberCountIncreaseDecreaseButtons("Adults","add")
            self.assertTrue(homepage.verifySpecificMemberCount("Adults",adultsCount+1))
            homepage.clickOnSpecificMemberCountIncreaseDecreaseButtons("Children","add")
            self.assertTrue(homepage.verifySpecificMemberCount("Adults",childrenCount+1))
            homepage.clickOnSpecificMemberCountIncreaseDecreaseButtons("Rooms","add")
            self.assertTrue(homepage.verifySpecificMemberCount("Rooms",roomsCount+1))
        finally:
            self.hardRefresh()
            homepage.clickOnMembersInputBox()
            homepage.clickOnSpecificMemberCountIncreaseDecreaseButtons("Adults","sub")
            homepage.clickOnSpecificMemberCountIncreaseDecreaseButtons("Children","sub")
            homepage.clickOnSpecificMemberCountIncreaseDecreaseButtons("Rooms","sub")

    def test3_VerifyUserCanSelectHeaderOptions(self):
        try:
            homepage = HomePage()
            homepage.clickOnSpecificTravelOptionsDisplayed("Flights")
            flightsPage = FlightsPage()
            self.assertTrue(flightsPage.verifySpecificHeaderOptionGetSelected("Flights"))
        finally:
            self.hardRefresh()
            self.navigateToHomePage()

    def test4_VerifyRadioButtonOnFlightsTab(self):
        try:
            homepage = HomePage()
            homepage.clickOnSpecificTravelOptionsDisplayed("Flights")
            flightsPage = FlightsPage()
            self.assertTrue(flightsPage.verifySpecificRadioButton("Round-trip"))
            self.assertTrue(flightsPage.verifySpecificRadioButton("One-way"))
            self.assertTrue(flightsPage.verifySpecificRadioButton("Multi-city"))
        finally:
            self.hardRefresh()
            self.navigateToHomePage()
