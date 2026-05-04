import subprocess
import sys


VALID_EXECUTION_MODES = {"sequential", "parallel"}
MARKERS = {
    "stays": "Stays",
    "flights": "Flights",
    "carrental": "CarRental",
    "car_rental": "CarRental",
    "smoke": "smoke",
}


def buildExecutionArgs(executionMode):
    if executionMode == "parallel":
        return ["-n", "auto", "--dist=loadscope"]
    return []


def runTestCasesByMarker(markerName, executionMode, extraArgs=None):
    print(f"Running {markerName} Test Cases in {executionMode.capitalize()} Mode...")
    reportName = f"{markerName}_Report_Parallel_Execution.html" if executionMode == "parallel" else f"{markerName}_Report.html"
    cmd = [
        sys.executable,
        "-m",
        "pytest",
        "seleniumWebDriver\\TestCases",
        "-m",
        markerName,
        "-v",
        "-s",
        f"--html=reports/{reportName}",
        "--self-contained-html",
    ]
    cmd.extend(buildExecutionArgs(executionMode))
    if extraArgs:
        cmd.extend(extraArgs)
    subprocess.run(cmd)


def runAll(executionMode, extraArgs=None):
    print(f"Running All Test Cases (Regression) in {executionMode.capitalize()} Mode...")
    reportName = "Regression_Report_Parallel_Execution.html" if executionMode == "parallel" else "Regression_Report.html"
    cmd = [
        sys.executable,
        "-m",
        "pytest",
        "seleniumWebDriver\\TestCases",
        "-v",
        "-s",
        f"--html=reports/{reportName}",
        "--self-contained-html",
    ]
    cmd.extend(buildExecutionArgs(executionMode))
    if extraArgs:
        cmd.extend(extraArgs)
    subprocess.run(cmd)


def runSingleTestCase(testCaseId):
    print(f"Running Single Test Case: {testCaseId}")
    cmd = [
        sys.executable,
        "-m",
        "pytest",
        "seleniumWebDriver\\TestCases",
        "-v",
        "-s",
        "-k",
        testCaseId,
    ]
    subprocess.run(cmd)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python Runner.py <markerName|all> <sequential|parallel> OR python Runner.py <testCaseName>")
        sys.exit(1)

    option = sys.argv[1].lower()
    if len(sys.argv) >= 3 and sys.argv[2].lower() in VALID_EXECUTION_MODES:
        markerName = MARKERS.get(option, sys.argv[1])
        executionMode = sys.argv[2].lower()
        extraArgs = sys.argv[3:]
        if option == "all":
            runAll(executionMode, extraArgs)
        else:
            runTestCasesByMarker(markerName, executionMode, extraArgs)
    elif option == "all":
        print("Usage: python Runner.py all <sequential|parallel>")
        sys.exit(1)
    else:
        runSingleTestCase(sys.argv[1])


'''
Command To Execute marker test cases: python seleniumWebDriver\TestCases\Runner.py <markerName> <sequential|parallel>
Command To Execute single test case: python seleniumWebDriver\TestCases\Runner.py <TestCase Name>
Command To Execute test Suites in Headless mode: $env:HEADLESS="true"; python seleniumWebDriver\TestCases\Runner.py <tagName> <sequential|parallel>
Command To Check Env variable: echo $env:HEADLESS
After running in headless mode make sure to undo the env variable changes:
Remove-Item Env:HEADLESS
'''
