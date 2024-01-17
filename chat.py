from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import whatsapp_parser
contants = ["Nikhil"]
name = "Nikhil"

from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
# options = Options()
# profile = webdriver.FirefoxProfile("/Users/umang/Library/Application Support/Firefox/Profiles/yxjrp4op.default")

# profile.update_preferences()
# options.profile = profile
# driver = webdriver.Firefox(options= options)
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

options.add_argument(r"--user-data-dir=/Users/umang/Library/Application Support/Google/Chrome")
options.add_argument(r'--profile-directory=Profile 7')
#options.add_argument("--disable-dev-shm-usage")
#ptions.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=options)

url = "https://web.whatsapp.com/"
driver.get(url)
#time.sleep(10)
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
#         (By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]'))).click(

#         )
while True:
    
        elem = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]')))
        #elem = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]')

        elem.click()
        elem.clear()
        elem.send_keys(name)
        elem.send_keys(Keys.ENTER)
        # new_elem = driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[4]')
        # new_elem.click()
        elem = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
        elem.click()

        elem =WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div[2]/div/div[2]')))
        a = elem.get_attribute('innerHTML')
        soup = BeautifulSoup(a, 'html.parser')
        
        messages = soup.text
        print(messages)

        mess_return = whatsapp_parser.main(messages, name)
        print(mess_return)
        if(mess_return!=None):
            elem = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]')
            elem.click()
            for i in range(50):
                  elem.send_keys(Keys.BACK_SPACE)
            elem.clear()
            elem.send_keys(name)
            elem.send_keys(Keys.ENTER)
            #time.sleep(5)
            elem = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
            elem.click()
            elem.clear()
           # elem = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div[3]')))  
            elem.send_keys(mess_return)
            elem.send_keys(Keys.ENTER)
            time.sleep(5)
            
        driver.refresh()
        
        









