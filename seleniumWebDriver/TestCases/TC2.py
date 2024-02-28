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
        except Exception as e:
            self.saveScreenShots("test1_VerifyFiltersOfSearchResults")
            raise e
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
        except Exception as e:
            self.saveScreenShots("test2_VerifyMembersCountChanges")
            raise e
        finally:
            self.hardRefresh()
            homepage = HomePage()
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
        except Exception as e:
            self.saveScreenShots("test3_VerifyUserCanSelectHeaderOptions")
            raise e
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
        except Exception as e:
            self.saveScreenShots("test4_VerifyRadioButtonOnFlightsTab")
            raise e
        finally:
            self.hardRefresh()
            self.navigateToHomePage()

    def test5_VerifyDropdownOptions(self):
        try:
            homepage = HomePage()
            homepage.clickOnSpecificTravelOptionsDisplayed("Flights")
            flightsPage = FlightsPage()
            self.assertTrue(flightsPage.verifySpecificOptionOfClassDropdown("Business"))
            self.assertTrue(flightsPage.verifySpecificOptionOfClassDropdown("Economy"))
            self.assertTrue(flightsPage.verifySpecificOptionOfClassDropdown("Premium economy"))
            self.assertTrue(flightsPage.verifySpecificOptionOfClassDropdown("First-class"))
            flightsPage.selectSpecificOptionInClassDropdown("First-class")
            self.assertTrue(flightsPage.verifySpecificOptionSelectedInClassDropdown("First-class"))
        except Exception as e:
            self.saveScreenShots("test5_VerifyDropdownOptions")
            raise e
        finally:
            self.hardRefresh()
            self.navigateToHomePage()

    def test6_VerifyAdultPopup(self):
        try:
            homepage = HomePage()
            homepage.clickOnSpecificTravelOptionsDisplayed("Flights")
            flightsPage = FlightsPage()
            flightsPage.clickOnSpecificButtonInFlightPage("adult")
            defaludValueOfAdults = int(flightsPage.getValueOfSpecificOptionOnAdultPopup("Adult"))
            flightsPage.clickOnPlusMinusButtonOfSpecificOptionOnAdultPopup("Adult")
            self.assertEquals(flightsPage.getValueOfSpecificOptionOnAdultPopup("Adult"),str(defaludValueOfAdults+1))
            defaludValueOfChildren = int(flightsPage.getValueOfSpecificOptionOnAdultPopup("Children"))
            flightsPage.clickOnPlusMinusButtonOfSpecificOptionOnAdultPopup("Children")
            self.assertEquals(flightsPage.getValueOfSpecificOptionOnAdultPopup("Children"),str(defaludValueOfChildren+1))
        except Exception as e:
            self.saveScreenShots("test6_VerifyAdultPopup")
            raise e
        finally:
            self.hardRefresh()
            self.navigateToHomePage()

    def test7_verifySearchButtonColorOnFlightScreen(self):
        try:
            homepage = HomePage()
            homepage.clickOnSpecificTravelOptionsDisplayed("Flights")
            flightsPage = FlightsPage()
            self.assertTrue(flightsPage.verifyColorOfSpecificButtonInFlightPage("Search","#ffffff"))
        except Exception as e:
            self.saveScreenShots("test7_verifySearchButtonColorOnFlightScreen")
            raise e
        finally:
            self.hardRefresh()
            self.navigateToHomePage()

    def test8_verifySearchFromAndToOnFlightScreen(self):
        try:
            homepage = HomePage()
            homepage.clickOnSpecificTravelOptionsDisplayed("Flights")
            flightsPage = FlightsPage()
            flightsPage.searchAndSelectSpecificLocation("from","AMD")
            flightsPage.searchAndSelectSpecificLocation("to","DEL")
            flightsPage.clickOnSpecificButtonInFlightPage("Search")
            self.assertTrue(flightsPage.verifySearchResultsDsplayed())
        except Exception as e:
            self.saveScreenShots("test8_verifySearchFromAndToOnFlightScreen")
            raise e
        finally:
            self.hardRefresh()
            self.navigateToHomePage()