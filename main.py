from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from db import Database
from ad_scraper import Ad_scraper

def initialize_driver():
        chrome_options = webdriver.ChromeOptions()

        prefs = {
            "profile.default_content_setting_values.notifications": 1,
            "profile.default_content_setting_values.automatic_downloads": 1,
            "profile.default_content_setting_values.muted": True,
        }

        chrome_options.add_experimental_option("prefs", prefs)

        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--profile-directory=Default")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)

        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        version = driver.capabilities["browserVersion"]
        print("version", version)

        return driver

if __name__ == "__main__":
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # driver = webdriver.Chrome(options=chrome_options)
    driver=initialize_driver()

    database = Database()
    news_websites=database.get_news_websites_from_database()  # got news websites from database

    Ad_scraper=Ad_scraper(driver,news_websites)    
    Ad_scraper.scrape_advertisement()



    database.close_connection()

    input("Press Enter to close the browser...")


