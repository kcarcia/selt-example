import keyring
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class GoogleLogin:
    def __init__(self, driver):
        self.name = "GoogleLogin"
        self.driver = driver
        self.url = "https://accounts.google.com/signin/v2"
        self.elements = dict(email_input="identifierId",
                             email_next_btn="identifierNext",
                             password_input="password",
                             password_next_btn="passwordNext")

    def google_login(self):
        """
        Log into Google with specified account.
        :return:
        """
        self.driver.get(self.url)
        email_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.elements[
                "email_input"])))
        email_input.send_keys("test.dummy.1717@gmail.com")
        self.driver.find_element_by_id(self.elements["email_next_btn"]).click()
        password_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.NAME, self.elements[
                "password_input"])))
        password_input.send_keys(keyring.get_password("gmail", "testdummy"))
        self.driver.find_element_by_id(self.elements["password_next_btn"]).click()
