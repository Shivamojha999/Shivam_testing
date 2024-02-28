import unittest
import HtmlTestRunner
from xmlrunner import XMLTestRunner
from seleniumWebDriver.TestCases.TC2 import SecondTestCase
from seleniumWebDriver.TestCases.TC1 import FirstTestCase


def runSmoke() :
    smoke = unittest.TestSuite()
    smoke.addTest(SecondTestCase("test1_VerifyFiltersOfSearchResults"))
    smoke.addTest(SecondTestCase("test2_VerifyMembersCountChanges"))
    smoke.addTest(SecondTestCase("test3_VerifyUserCanSelectHeaderOptions"))
    #runner = XMLTestRunner(output='test-reports')
    runner = HtmlTestRunner.HTMLTestRunner(output='test-reports')
    runner.run(smoke)
def runAllTcs():
    regression = unittest.TestSuite()
    TC1 = unittest.TestLoader().loadTestsFromTestCase(FirstTestCase)
    TC2 = unittest.TestLoader().loadTestsFromTestCase(SecondTestCase)
    regression.addTests([TC1,TC2])
    #runner = XMLTestRunner(output='test-reports')
    runner = HtmlTestRunner.HTMLTestRunner(output='test-reports')
    runner.run(regression)

if __name__ == '__main__':
    runSmoke()
