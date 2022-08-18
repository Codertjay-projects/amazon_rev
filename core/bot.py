import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "http://deepyeti.ucsd.edu/jianmo/amazon/index.html"


class AmazonBotAutomation:
    def __init__(self, teardown=True):
        s = Service(ChromeDriverManager().install())
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.teardown = teardown
        # keep chrome open
        self.options.add_experimental_option("detach", True)
        self.options.add_experimental_option(
            "excludeSwitches",
            ['enable-logging']
        )
        self.driver = webdriver.Chrome(
            options=self.options,
            service=s)
        self.driver.implicitly_wait(50)
        self.json_urls = []
        super(AmazonBotAutomation, self).__init__()

    def __enter__(self):
        self.driver.get(BASE_URL)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.driver.quit()

    def land_page(self):
        self.driver.get(BASE_URL)

    def download_all_reviews(self):
        with open("./automation.json", "r") as f:
            data = json.load(f)
            element = self.driver.find_element(by=By.CSS_SELECTOR, value=data.get("item_selector"))
            elements = element.find_elements(by=By.CSS_SELECTOR, value=data.get("item_items_selectors"))
            for item in elements:
                json_url = item.get_attribute("href")
                self.json_urls.append(json_url)


bot = AmazonBotAutomation(teardown=True)
bot.land_page()
bot.download_all_reviews()

