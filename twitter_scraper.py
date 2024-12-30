from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def scrape_twitter_trends(proxy=None):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    if proxy:
        chrome_options.add_argument(f'--proxy-server={proxy}')
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get("https://twitter.com/login")
        
        # Login (you'll need to replace with your Twitter credentials)
        username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "text"))
        )
        username.send_keys("Anshzala12cloud")
        
        next_button = driver.find_element(By.XPATH, "//span[text()='Next']")
        next_button.click()
        
        password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password.send_keys("Anshzala12cloud")
        
        login_button = driver.find_element(By.XPATH, "//span[text()='Log in']")
        login_button.click()
        
        # Wait for the trends to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-testid='trend']"))
        )
        
        # ---- Before ----
        # # Extract trending topics
        # trends = driver.find_elements(By.XPATH, "//div[@data-testid='trend']")
        # trending_topics = [trend.text.split('\n')[0] for trend in trends[:5]]
        
        # ---- After ----
        # Extract trending topics
        trends = driver.find_elements(By.XPATH, "//div[@data-testid='trend']")

        # Extract hashtags and remove the # symbol
        trending_topics = [
            part[1:] for trend in trends[:5] for part in trend.text.split('\n') if part.startswith('#')
        ]
                    
        return trending_topics
    
    finally:
        driver.quit()

if __name__ == "__main__":
    print(scrape_twitter_trends())