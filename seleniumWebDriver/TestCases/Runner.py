import unittest
from xmlrunner import XMLTestRunner
from seleniumWebDriver.TestCases.TC2 import SecondTestCase
from seleniumWebDriver.TestCases.TC1 import FirstTestCase

if __name__ == '__main__':
    # Define the test suite for multiple test cases
    TC1 = unittest.TestLoader().loadTestsFromTestCase(FirstTestCase)
    TC2 = unittest.TestLoader().loadTestsFromTestCase(SecondTestCase)

    # Define the test suite for single test cases
    smoke = unittest.TestSuite()
    smoke.addTest(SecondTestCase("test3_VerifyUserCanSelectHeaderOptions"))
    smoke.addTest(SecondTestCase("test5_VerifyDropdownOptions"))

    # Run all TC Suit
    regression = unittest.TestSuite()
    regression.addTests([TC1,TC2])

    # Define the XML test runner with output directory
    runner = XMLTestRunner(output='test-reports')

    # Run the test suite with XMLTestRunner
    runner.run(smoke)
