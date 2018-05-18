import argparse
import yaml
import imp
from termcolor import colored
import os
import configparser


# GLOBAL VARIABLES

# Dictionary of tests loaded
tests_loaded = dict()

# selt configs
selt_config = os.path.expanduser('~') + "/.selt.cfg"
config = configparser.ConfigParser()
config.read(selt_config)

# Command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--browser", help="(String) Browser tests are run on. "
                                      "Options include: firefox, "
                                      "firefox-headless, chrome, "
                                      "chrome-headless. Default is "
                                      "chrome-headless.",
                    default=config["DEFAULTS"]["browser"])

args = parser.parse_args()
browser = args.browser


def import_test(test_path, test_name):
    """
    Imports all test classes. Methods in classes are the tests, therefore,
    we must dynamically import classes containing test methods in order to
    execute tests.

    :param test_path: (array) ordered list of packages in path to the test file
    :param test_name: (string) name of the file w/ test, not including extension
    :return:
    """
    # Define the test class name based on the test file name
    # e.g., a test file named test_example has a class named TestExample
    class_name = ""
    for name in test_name.split("_"):
        class_name = class_name + name.capitalize()

    # Build the full file path to the test as a string
    file_path = generate_file_path(test_path, test_name + ".py")

    # Load module with test class given the file (test) name and file path
    module = imp.load_source(test_name, file_path)

    # Create instance of test class
    test_class = getattr(module, class_name)(browser)

    # Add instance of test class to dictionary
    tests_loaded[test_name] = test_class


def open_file(file_name):
    """
    Opens a file in read only mode and returns its content in yaml.

    :param file_name: (strong) The name of the file to be opened
    :return: (yaml) Contents of file
    """
    try:
        with open(file_name, 'r') as f:
            return yaml.load(f)
    except yaml.YAMLError as e:
        print("ERROR: Check your yaml file for syntax errors")
        print(e)


def generate_file_path(package_path, file_name):
    """
    Dynamically generate full path to file, including filename and extension.

    :param package_path: (array) ordered list of packages in path to test file
    :param file_name: (string) name of the file w/ test, including the extension
    :return: (string) full path to file, including filename and extension
    """
    file_path = ""
    for package in package_path:
        file_path += package + "/"
    return file_path + file_name


def execute_tests(tests):
    """
    Executes specified tests.

    :param tests: (yaml) List of tests to run
    :return:
    """
    for test in tests:
        # If a test has an enabled field set to true OR does not have an
        # enabled field, then we assume the test is enabled and run it
        if not test.get("enabled", True):
            continue

        # Run group of tests
        if test.get("type", "test") == "test-group":
            # Generate the path to the test group's manifest file
            filename = generate_file_path(test["test_name"].split("."),
                                          "manifest.yml")

            # Open manifest file for test group
            tests = open_file(filename)

            # Execute tests in test group
            execute_tests(tests)

        # Run individual test
        else:
            # The test name for an individual test includes the test
            # name. We must parse this out to generate the package path.
            # Example individual test: tests.example_test_1
            # Example group test: tests.group_tests.example_test_2
            test_path = test["test_name"].split(".")
            test_name = test_path[len(test_path) - 1]
            del test_path[-1]

            # Import module if not already imported
            if test_name not in tests_loaded:
                import_test(test_path, test_name)

            # Execute test setup
            getattr(tests_loaded[test_name], "setup")()

            # Execute the test
            getattr(tests_loaded[test_name], test_name)(*test.get(
                "params", []))

            # Execute test teardown
            getattr(tests_loaded[test_name], "teardown")()

            print(colored("PASSED: " + test_name, "green"))


def run():
    """
    Open manifest file with tests and executes tests.

    :return:
    """
    use_cases = open_file("tests/manifest.yml")
    execute_tests(use_cases)


run()