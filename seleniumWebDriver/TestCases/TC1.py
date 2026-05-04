import pytest

from seleniumWebDriver.Pages.CommonPage import CommonPage
from seleniumWebDriver.Pages.Homepage import HomePage
from seleniumWebDriver.Pages.SearchResultStaysPage import SearchResultStaysPage


@pytest.mark.Stays
class TestStaysPage(CommonPage):

    @pytest.mark.smoke
    def test_VerifySignInPopup(self):
        homePage = HomePage(self.driver, configureDefaults=False, dismissPopup=False)
        homePageTitleDisplayed = homePage.verifyHomePageTitle(homePage.getTitleOfPage())
        assert homePageTitleDisplayed is True, "Home page title didn't appear"
        popupDisplayed = homePage.verifyUnwantedPopup()
        assert popupDisplayed is True, "Sign in popup didn't appear"
        homePage.closeUnwantedPopup()
        popupClosed = homePage.verifyUnwantedPopupClosed()
        assert popupClosed is True, "Sign in popup didn't close"

    @pytest.mark.smoke
    def test_VerifyAllTabsVisibleOnMainPage(self):
        homePage = HomePage(self.driver)
        for tabName in ["Stays", "Flights", "Flight + Hotel", "Car rentals", "Attractions", "Airport taxis"]:
            tabDisplayed = homePage.verifySpecificTravelOptionsDisplayed(tabName)
            assert tabDisplayed is True, f"Travel tab '{tabName}' didn't appear"

    def test_VerifyCurrencyScreenFunctionality(self):
        homePage = HomePage(self.driver)
        currencyDisplayed = homePage.verifySpecificButtonDisplayed("INR")
        assert currencyDisplayed is True, "INR currency button didn't appear"
        homePage.clickOnSpecificButton("INR")
        currencyPopupDisplayed = homePage.verifySpecificAreaLabel("Select your currency", "div")
        assert currencyPopupDisplayed is True, "Currency popup didn't appear"
        assert homePage.verifySpecificCurrencyOnSelectCurrencyPopup("Hong Kong Dollar") is True
        assert homePage.verifySpecificCurrencyOnSelectCurrencyPopup("United Arab Emirates Dirham") is True
        homePage.clickOnSpecificCurrencyOnSelectCurrencyPopup("United Arab Emirates Dirham")
        assert homePage.verifySpecificAreaLabel("Prices in United Arab Emirates Dirham") is True
        homePage.clickOnSpecificButton("AED")
        assert homePage.verifySpecificCurrencyOnSelectCurrencyPopup("Hong Kong Dollar") is True
        homePage.clickOnSpecificCurrencyOnSelectCurrencyPopup("New Taiwan Dollar")
        assert homePage.verifySpecificButtonDisplayed("TWD") is True

    def test_VerifySelectLanguageScreenFunctionality(self):
        homePage = HomePage(self.driver)
        assert homePage.verifySpecificAreaLabel("Language: English (US)") is True
        homePage.clickOnSpecificAreaLabel("Language: English (US)")
        assert homePage.verifySpecificAreaLabel("Select your language", "div") is True
        assert homePage.verifySpecificLanguageOnSelectLanguagePopup("Islenska") is True
        homePage.clickOnSpecificLanguageOnSelectLanguagePopup("Islenska")

    def test_VerifyDatesApiWorking(self):
        homePage = HomePage(self.driver)
        assert homePage.getCurrentDate("%y/%m/%d") is not None
        assert homePage.getCurrentDate("%#d") is not None
        assert homePage.getPastFutureDateByDays("%Y-%m-%d", 1, "p") is not None
        assert homePage.getPastFutureDateByMonths("%Y-%m-%d", 1, "f") is not None
        assert homePage.getPastFutureDateByYears("%Y-%m-%d", 1, "p") is not None

    @pytest.mark.smoke
    def test_VerifyFunctionalityOfWhereToGoSearchBox(self):
        homePage = HomePage(self.driver)
        homePage.clickOnSelectLocationInputBox()
        homePage.searchAndSelectLocation("Lucknow")
        locationSelected = homePage.verifyLocationSelected("Lucknow")
        assert locationSelected is True, "Lucknow was not selected in destination field"

    def test_VerifyCalenderDesign(self):
        homePage = HomePage(self.driver)
        currentMonth = homePage.getCurrentDate("%B")
        futureMonth = homePage.getPastFutureDateByMonths("%B", 1, "f")
        homePage.clickOnSelectDateInputBox()
        assert homePage.verifyCalenderOpens() is True
        assert homePage.verifySpecificMonthOpenedOnDatePicker(currentMonth) is True
        assert homePage.verifySpecificMonthOpenedOnDatePicker(futureMonth) is True

    def test_SelectDateVerification(self):
        homePage = HomePage(self.driver)
        futureMonth = homePage.getPastFutureDateByMonths("%B", 3, "f")
        futureDate = homePage.getPastFutureDateByMonths("%#d", 3, "f")
        futureDateByDay = homePage.getPastFutureDateByDays("%#d", 95, "f")
        homePage.clickOnSelectDateInputBox()
        homePage.selectDateOnDatePicker(futureMonth, futureDate)
        homePage.selectDateOnDatePicker(futureMonth, futureDateByDay)
        futureDateFormatted = homePage.getPastFutureDateByMonths("%b %#d", 3, "f")
        assert homePage.verifySpecificDateSelected(futureDateFormatted) is True

    @pytest.mark.smoke
    def test_VerifySearchFunctionality(self):
        homePage = HomePage(self.driver)
        homePage.clickOnSelectLocationInputBox()
        homePage.searchAndSelectLocation("Goa")
        futureMonth = homePage.getPastFutureDateByMonths("%B", 1, "f")
        futureDate = homePage.getPastFutureDateByMonths("%#d", 1, "f")
        futureDateByDay = homePage.getPastFutureDateByDays("%#d", 35, "f")
        homePage.selectDateOnDatePicker(futureMonth, futureDate)
        homePage.selectDateOnDatePicker(futureMonth, futureDateByDay)
        homePage.clickOnSearchButton()
        searchResultStaysPage = SearchResultStaysPage(self.driver)
        cityDisplayed = searchResultStaysPage.verifySearchedCityDisplayed("Goa")
        assert cityDisplayed is True, "Search result city Goa didn't appear"

    @pytest.mark.smoke
    def test_VerifyFiltersOfSearchResults(self):
        homePage = HomePage(self.driver)
        homePage.clickOnSelectLocationInputBox()
        homePage.searchAndSelectLocation("Goa")
        futureMonth = homePage.getPastFutureDateByMonths("%B", 1, "f")
        futureDate = homePage.getPastFutureDateByMonths("%#d", 1, "f")
        futureDateByDay = homePage.getPastFutureDateByDays("%#d", 35, "f")
        homePage.selectDateOnDatePicker(futureMonth, futureDate)
        homePage.selectDateOnDatePicker(futureMonth, futureDateByDay)
        homePage.clickOnSearchButton()
        searchResultStaysPage = SearchResultStaysPage(self.driver)
        filterDisplayed = searchResultStaysPage.verifySpecificFilterOptionDisplayed("City", "Old Goa")
        assert filterDisplayed is True, "Old Goa city filter didn't appear"

    @pytest.mark.smoke
    def test_VerifyMembersCountChanges(self):
        homePage = HomePage(self.driver)
        homePage.clickOnMembersInputBox()
        adultsCount = homePage.getSpecificMemberCount("Adults")
        childrenCount = homePage.getSpecificMemberCount("Children")
        roomsCount = homePage.getSpecificMemberCount("Rooms")
        homePage.clickOnSpecificMemberCountIncreaseDecreaseButtons("Adults", "add")
        assert homePage.verifySpecificMemberCount("Adults", adultsCount + 1) is True
        homePage.clickOnSpecificMemberCountIncreaseDecreaseButtons("Children", "add")
        assert homePage.verifySpecificMemberCount("Children", childrenCount + 1) is True
        homePage.clickOnSpecificMemberCountIncreaseDecreaseButtons("Rooms", "add")
        assert homePage.verifySpecificMemberCount("Rooms", roomsCount + 1) is True
