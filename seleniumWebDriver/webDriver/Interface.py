from abc import ABC

from selenium.webdriver.remote.webdriver import WebDriver


class Interface(ABC):
    driver: WebDriver

    bookingUrl = "https://www.booking.com/"
    defaultLanguage = "English (US)"
    defaultCurrency = "Indian Rupee"
    defaultTimeout = 20
