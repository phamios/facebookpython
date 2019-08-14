from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
 
driver = webdriver.Chrome(executable_path="/Users/macbook/Projects/python/autofacebook/chromedriver")
driver.implicitly_wait(15) # seconds
driver.get('https://www.facebook.com/')
print "Opened facebook..."
a = driver.find_element_by_id('email')
a.send_keys('kevin.wirecard@gmail.com')
print "Email Id entered..."
b = driver.find_element_by_id('pass')
b.send_keys('1q2w3e4r5t6y7u8i')
print "Password entered..."
c = driver.find_element_by_id('loginbutton')
c.click()
driver.get("https://www.facebook.com/nathania.laut.3")
post_box=driver.find_element_by_xpath("//*[@name='xhpc_message']")
post_box.click()
post_box.send_keys("Testing using Name not ID.Selenium is easy.")
sleep(2)
post_it=driver.find_element_by_xpath("//*[@id='u_0_1a']/div/div[6]/div/ul/li[2]/button")
post_it.click()
print "Posted..."