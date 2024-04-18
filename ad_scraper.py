from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

import time
class Ad_scraper:
    def __init__(self, driver,news_websites):
        self.driver = driver
        self.advertisement_infos=[]
        self.news_websites=news_websites

    def scrape_advertisement(self):
        self.driver.get("https://apa.az/")
        time.sleep(10)
        elements = self.driver.find_elements(By.TAG_NAME,"a")
        print(len(elements))
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='GardenBody']"))
        )
            # element=self.driver.find_element(By.XPATH,'//div[@class="GardenBody"]')
            # element.click()
        except TimeoutException:
            print("timeout")
        except NoSuchElementException:
            print("Element not found on the initial page")

        # for website in self.news_websites:
        #     id,website_name, url = website
        #     print(f"Scraping advertisements from {website_name} ({url})")
        #     try:
        #         self.driver.get(url)
        #         time.sleep(4)
        #         # ad_div=self.driver.find_element(By.CLASS_NAME,"left_banner")
        #         ad_url=self.driver.find_element(By.XPATH,'//div[@class="left_banner"]//a')
        #         # ad_url = ad_div.find_element(By.XPATH,'.//a')
        #         print(ad_url.get_attribute('href'))

                
        #         # Example:
        #         # advertisements = self.driver.find_elements_by_css_selector('.advertisement')
        #         # for ad in advertisements:
        #         #     ad_text = ad.text
        #         #     # Store the advertisement data in your database
        #     except Exception as e:
        #         print(f"Error scraping advertisements from {website_name}: {e}")


