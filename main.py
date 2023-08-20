from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

INSTAGRAM_USERNAME = "YOUR INSTAGRAM USERNAME"
INSTAGRAM_PASSWORD = "YOUR INSTAGRAM PASSWORD"

ACCOUNT = "TARGET ACCOUNT USERNAME"

CHROME_DRIVER_PATH = "YOUR CHROME DRIVER PATH"

class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login_instagram(self):
        self.driver.get("https://www.instagram.com/")

        accept_cookies = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[1]')
        accept_cookies.click()
        time.sleep(2)

        username_input = self.driver.find_element(By.NAME, 'username')
        username_input.send_keys(INSTAGRAM_USERNAME)

        password_input = self.driver.find_element(By.NAME, 'password')
        password_input.send_keys(INSTAGRAM_PASSWORD)
        password_input.send_keys(Keys.ENTER)
        time.sleep(3)

        notifications_popup = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
        notifications_popup.click()
        time.sleep(1)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{ACCOUNT}")
        time.sleep(3)

        followers = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(4)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_button.click()

        followers_popup = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_popup)
            time.sleep(2)


bot = InstaFollower()
bot.login_instagram()
bot.find_followers()
bot.follow()
