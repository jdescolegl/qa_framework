from selenium.webdriver.common.by import By
from qa_commons.WebdriverSetup import Browser
from Src.Locators.j_pet_store_locators import Locator


class HomePage:
    def __init__(self, url, headless=True):
        self.driver = Browser(url, headless).driver
        self.heading = self.driver.find_element(By.TAG_NAME, Locator.heading).text
        self.enter_store = self.driver.find_element(By.XPATH, Locator.enter_store)

    def get_heading(self):
        return self.heading

    def get_enter_store(self):
        return self.enter_store
