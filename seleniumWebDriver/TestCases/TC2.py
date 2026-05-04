import pytest

from seleniumWebDriver.Pages.CarRentalPage import CarRentalPage
from seleniumWebDriver.Pages.CommonPage import CommonPage
from seleniumWebDriver.Pages.FlightsPage import FlightsPage
from seleniumWebDriver.Pages.Homepage import HomePage


@pytest.mark.Flights
class TestFlightsPage(CommonPage):

    @pytest.mark.smoke
    def test_VerifyUserCanSelectHeaderOptions(self):
        homePage = HomePage(self.driver)
        homePage.clickOnSpecificTravelOptionsDisplayed("Flights")
        flightsPage = FlightsPage(self.driver)
        headerSelected = flightsPage.verifySpecificHeaderOptionGetSelected("Flights")
        assert headerSelected is True, "Flights header option was not selected"

    def test_VerifyRadioButtonOnFlightsTab(self):
        homePage = HomePage(self.driver)
        homePage.clickOnSpecificTravelOptionsDisplayed("Flights")
        flightsPage = FlightsPage(self.driver)
        assert flightsPage.verifySpecificRadioButton("Round-trip") is True
        assert flightsPage.verifySpecificRadioButton("One-way") is True
        assert flightsPage.verifySpecificRadioButton("Multi-city") is True

    def test_VerifyDropdownOptions(self):
        homePage = HomePage(self.driver)
        homePage.clickOnSpecificTravelOptionsDisplayed("Flights")
        flightsPage = FlightsPage(self.driver)
        assert flightsPage.verifySpecificOptionOfClassDropdown("Business") is True
        assert flightsPage.verifySpecificOptionOfClassDropdown("Economy") is True
        assert flightsPage.verifySpecificOptionOfClassDropdown("Premium economy") is True
        assert flightsPage.verifySpecificOptionOfClassDropdown("First-class") is True
        flightsPage.selectSpecificOptionInClassDropdown("First-class")
        assert flightsPage.verifySpecificOptionSelectedInClassDropdown("First-class") is True

    def test_VerifyAdultPopup(self):
        homePage = HomePage(self.driver)
        homePage.clickOnSpecificTravelOptionsDisplayed("Flights")
        flightsPage = FlightsPage(self.driver)
        flightsPage.clickOnSpecificButtonInFlightPage("adult")
        defaultValueOfAdults = int(flightsPage.getValueOfSpecificOptionOnAdultPopup("Adult"))
        flightsPage.clickOnPlusMinusButtonOfSpecificOptionOnAdultPopup("Adult")
        assert flightsPage.getValueOfSpecificOptionOnAdultPopup("Adult") == str(defaultValueOfAdults + 1)
        defaultValueOfChildren = int(flightsPage.getValueOfSpecificOptionOnAdultPopup("Children"))
        flightsPage.clickOnPlusMinusButtonOfSpecificOptionOnAdultPopup("Children")
        assert flightsPage.getValueOfSpecificOptionOnAdultPopup("Children") == str(defaultValueOfChildren + 1)

    def test_VerifySearchButtonColorOnFlightScreen(self):
        homePage = HomePage(self.driver)
        homePage.clickOnSpecificTravelOptionsDisplayed("Flights")
        flightsPage = FlightsPage(self.driver)
        assert flightsPage.verifyColorOfSpecificButtonInFlightPage("Search", "#ffffff") is True

    def test_VerifySearchFromAndToOnFlightScreen(self):
        homePage = HomePage(self.driver)
        homePage.clickOnSpecificTravelOptionsDisplayed("Flights")
        flightsPage = FlightsPage(self.driver)
        flightsPage.searchAndSelectSpecificLocation("from", "AMD")
        flightsPage.searchAndSelectSpecificLocation("to", "DEL")
        flightsPage.clickOnSpecificButtonInFlightPage("Search")
        assert flightsPage.verifySearchResultsDsplayed() is True


@pytest.mark.CarRental
class TestCarRentalPage(CommonPage):

    @pytest.mark.smoke
    def test_VerifyUIFieldsOfCarRentalScreen(self):
        homePage = HomePage(self.driver)
        homePage.clickOnSpecificTravelOptionsDisplayed("Car rentals")
        carRentalPage = CarRentalPage(self.driver)
        assert carRentalPage.verifyPickupLocationSearchField() is True
        assert carRentalPage.verifySpecificDateFieldOnTravelBar("Pick-up date") is True
        assert carRentalPage.verifySpecificDateFieldOnTravelBar("Drop-off date") is True
        assert carRentalPage.verifySpecificTimeFieldOnTravelBar("pickup-time") is True
        assert carRentalPage.verifySpecificTimeFieldOnTravelBar("dropoff-time") is True
        assert carRentalPage.verifySpecificCheckBoxOnTravelBar("Drop car off at different location") is True
        assert carRentalPage.verifySpecificCheckBoxOnTravelBar("Driver aged 30 - 65?") is True
