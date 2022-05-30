import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from Src.PageObject.j_pet_store_page import HomePage


class TestJpetStore:
    @pytest.fixture(scope="class")
    def home_page(self):
        _url = "https://petstore.octoperf.com/"
        self.home_page = HomePage(_url, headless=True)
        yield self.home_page
        self.home_page.driver.quit()

    def test_heading_title(self, home_page):
        heading_title = home_page.get_heading()
        assert heading_title == "Welcome to JPetStore 6"

    @pytest.mark.asd
    def test_enter_the_store_link(self, home_page):
        enter_store = home_page.get_enter_store()
        enter_store.click()
        allure.attach(home_page.driver.save_screenshot('enter_store'), name="enter_store", attachment_type="PNG")
        wait = WebDriverWait(home_page.driver, 10)
        wait.until(lambda driver: home_page.driver.current_url != "https://petstore.octoperf.com/")
        assert home_page.driver.current_url == "https://petstore.octoperf.com/actions/Catalog.action"
