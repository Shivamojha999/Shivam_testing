import os

import pytest
from selenium import webdriver


def _build_driver(downloadPath):
    browserName = os.getenv("BROWSER", "chrome").lower()
    headless = os.getenv("HEADLESS") == "true"

    if browserName == "edge":
        options = webdriver.EdgeOptions()
    else:
        options = webdriver.ChromeOptions()

    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
    else:
        options.add_argument("--force-device-scale-factor=1.25")

    prefs = {
        "download.default_directory": downloadPath,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    }
    options.add_experimental_option("prefs", prefs)

    if browserName == "edge":
        return webdriver.Edge(options=options)
    return webdriver.Chrome(options=options)


'''
created By: Shivam Ojha
since: 04 May 2026
desc: This hook is used to save Screen Shots of Failures on Setup & TC Execution phase
param: none
return: none
'''
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    if report.when in ["setup", "call"] and report.failed:
        instance = getattr(item, "instance", None)
        if instance and hasattr(instance, "driver"):
            driver = instance.driver
            try:
                projectPath = os.getcwd()
                screenShotsDir = os.path.join(projectPath, "ScreenShots")
                os.makedirs(screenShotsDir, exist_ok=True)
                fileName = os.path.join(screenShotsDir, item.name + ".png")
                driver.save_screenshot(fileName)
                print(f"Screenshot saved: {fileName}")
            except Exception as e:
                print(f"Screenshot failed: {e}")


'''
created By: Shivam Ojha
since: 04 May 2026
desc: This fixture is used to setup driver & close driver before & after each TC
param: none
return: none
'''
@pytest.fixture(scope="function", autouse=True)
def driver_setup(request):
    projectPath = os.getcwd()
    downloadPath = os.path.join(projectPath, "downloads")
    os.makedirs(downloadPath, exist_ok=True)
    driver = _build_driver(downloadPath)
    if request.cls:
        request.cls.driver = driver
    yield driver
    driver.quit()


'''
created By: Shivam Ojha
since: 04 May 2026
desc: This fixture is used to make website ready for testing before each TC
param: none
return: none
'''
@pytest.fixture(scope="function", autouse=True)
def setup_All(request, driver_setup):
    instance = getattr(request, "instance", None)
    if instance:
        instance.launchUrl()
        instance.maximizeWindow()
    else:
        print("Test case failed as Instance not found")


'''
created By: Shivam Ojha
since: 04 May 2026
desc: This fixture is used to perform generic cleanup after a TC
param: none
return: none
'''
@pytest.fixture(scope="function")
def teardown_All(request):
    yield
    instance = getattr(request, "instance", None)
    if instance:
        instance.hardRefresh()
    else:
        print("Test case failed as Instance not found")
