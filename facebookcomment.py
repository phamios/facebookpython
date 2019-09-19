# -*- coding: utf-8 -*-
 
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
def main():
 
    # Your Facebook account user and password
    usr = "kevin.wirecard@gmail.com"
    pwd = "1q2w3e4r5t6y7u8i"
    message = "linhcorner.com beauty cosmetic shop online - free shipping worldwide."
    #set multiple fb groups here
    group_links = [
        "https://www.facebook.com/groups/204269436355423"
    ]
 
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.notifications": 2 # 1:allow, 2:block 
    })
 
    driver = webdriver.Chrome(executable_path="/Users/macbook/Projects/python/autofacebook/chromedriver")
    driver.implicitly_wait(15) # seconds
 
    # Go to facebook.com
    driver.get("http://www.facebook.com")
     
    # Enter user email
    elem = driver.find_element_by_id("email")
    elem.send_keys(usr)
    # Enter user password
    elem = driver.find_element_by_id("pass")
    elem.send_keys(pwd)
    # Login
    elem.send_keys(Keys.RETURN)
 
    for group in group_links:
 
        # Go to the Facebook Group
        driver.get(group)
 
        # Click the post box
        post_box=driver.find_element_by_xpath("//*[@name='xhpc_message_text']")
 
        # Enter the text we want to post to Facebook
        post_box.send_keys(message)
 
        sleep(5)
        buttons = driver.find_elements_by_tag_name("button")
        sleep(5)
        for button in buttons:
            if button.text == "Post":
                button.click()
                sleep(10)
 
    # driver.close()
 
if __name__ == '__main__':
  main()