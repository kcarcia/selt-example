from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.options import DesiredCapabilities
import os
import configparser


# selt configs
selt_config = os.path.expanduser('~') + "/.selt.cfg"
config = configparser.ConfigParser()
config.read(selt_config)


class BaseTest(object):
    def __init__(self, browser):
        self.name = "BaseTest"
        self.driver = ""
        self.browser = browser

    def setup(self):
        """
        Default setup method for tests. The browser is passed through the
        command line via the --browser flag OR the default browser specified
        in config.py is used.

        NOTE: Currently, init_browser supports only the latest version of
        Firefox and the latest version of Chrome. It  should be expanded to
        introduce more configurability and browser options. Additionally,
        parallelization is not yet supported.

        :return:
        """
        if "firefox" in self.browser.lower():
            binary = FirefoxBinary(config["WEBDRIVER PATHS"]["firefox_path"])
            firefox_capabilities = DesiredCapabilities.FIREFOX
            firefox_capabilities["marionette"] = True

            if "headless" in self.browser.lower():
                os.environ['MOZ_HEADLESS'] = '1'

            self.driver = webdriver.Firefox(firefox_binary=binary,
                                            executable_path=config["WEBDRIVER PATHS"]["geckodriver_path"])
        elif "chrome" in self.browser.lower():
            chrome_options = Options()
            if "headless" in self.browser.lower():
                chrome_options.add_argument("--headless")
                # User agent necessary to specify browser being used to
                # ensure pages load the same in a headless and non-headless
                # state.
                chrome_options.add_argument("--user-agent=Mozilla/5.0 (X11; "
                                            "Linux x86_64) AppleWebKit/537.36 "
                                            "(KHTML, like Gecko) "
                                            "Chrome/60.0.3112.50 Safari/537.36")
            self.driver = webdriver.Chrome(chrome_options=chrome_options,
                                           executable_path=config["WEBDRIVER PATHS"]["chrome_path"])

    def teardown(self):
        """
        Default teardown method for tests. Close the browser.

        :return:
        """
        self.driver.quit()
