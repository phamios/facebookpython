from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-infobars")
chrome_options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.notifications": 2 # 1:allow, 2:block 
})

usr = "kevin.wirecard@gmail.com"
pwd = "1q2w3e4r5t6y7u8i"

driver = webdriver.Chrome(executable_path="C:\Projects\python\facebookpython/chromedriver")
driver.implicitly_wait(15) # seconds
driver.get('https://www.facebook.com/login.php?login_attempt=1&lwv=110')
print("Opened facebook...")
email = driver.find_element_by_xpath("//input[@id='email' or @name='email']")
email.send_keys(usr)
print("email entered...")
password = driver.find_element_by_xpath("//input[@id='pass']")
password.send_keys(pwd)
print("Password entered...")
button = driver.find_element_by_xpath("//button[@id='loginbutton']")
button.click()
print("facebook opened")
sleep(20)
filepath = '/Users/macbook/Projects/python/autofacebook/nanacorner_product.txt'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
   	driver.refresh();
   	sleep(100) 
	print("Line {}: {}".format(cnt, line.strip()))
	sleep(100) 
	status= driver.find_element_by_xpath("//textarea[@name='xhpc_message']")
	status.send_keys( line.strip() +  ' #beauty #cosmetic #waxing #skincare #homedecor #canvas #art #bodyart #tatoo #love #healthcare #facecare #lipstick Get more best product what you want at here ');
	sleep(135) 
	print("Add Status trying")
	sleep(15)
	# postbutton = driver.find_element_by_xpath("//button[contains(.,'Post')]")
	# postbutton.click()
	post_it=driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[3]/div[2]/button")
	post_it.click()
	sleep(260) 
	line = fp.readline()
	cnt += 1

print("post done")


