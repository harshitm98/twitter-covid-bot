from selenium import webdriver
import time
from config import USERNAME, PASSWORD

headers = {
    
}

driver = webdriver.PhantomJS("/home/fakebatman/twitter-covid-bot/phantomjs")
driver.get("https://twitter.com/login")
html = driver.page_source
print(html)

input_login_username = driver.find_elements_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")[0]
input_login_username.send_keys(USERNAME)
input_login_password = driver.find_elements_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")[0]
input_login_password.send_keys(PASSWORD)
login_button = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div")
login_button.click()

print(input_login_username)

time.sleep(10)
