from abc import ABC, abstractmethod
from selenium import webdriver

class Interface(ABC):

    driver = webdriver.Edge()
    #driver2 = webdriver.Edge()