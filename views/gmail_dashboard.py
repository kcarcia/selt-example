from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class GmailDashboard:
    def __init__(self, driver):
        self.name = "GmailDashboard"
        self.driver = driver
        self.elements = dict(compose_btn="//*[@id=':3w']/div/div",
                             email_recipient="//textarea[@aria-label='To']",
                             close_btn=":5m",
                             draft_link="//*[@id=':49']/div/div[2]/span/a",
                             star_btn="//*[@id=':60']")

    def compose_email(self):
        """
        Compose gmail draft.
        :return:
        """
        self.driver.find_element_by_xpath(self.elements["compose_btn"]).click()
        email_recipient = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.elements[
                "email_recipient"])))
        email_recipient.send_keys(
            "test")
        self.driver.find_element_by_id(self.elements["close_btn"]).click()
        time.sleep(1)

    def star_email_draft(self):
        """
        Star 1 gmail draft.

        NOTE: This test is not currently working reliably, therefore, I have
        disabled it in the manifest file.

        :return:
        """
        actions = ActionChains(self.driver)
        self.driver.find_element_by_xpath(self.elements["draft_link"]).click()
        star_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.elements[
                "star_btn"])))
        actions.move_to_element(star_btn).click().perform()

