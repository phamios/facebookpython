from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.get('https://accounts.google.com/ServiceLogin?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Fhl%3Den%26feature%3Dcomment%26app%3Ddesktop%26next%3D%252Fall_comments%253Fv%253DLAr6oAKieHk%26action_handle_signin%3Dtrue&uilel=3&service=youtube&passive=true&hl=en')

# log in
driver.find_element_by_id('Email').send_keys('username')
driver.find_element_by_id('Passwd').send_keys('password')
driver.find_element_by_id('signIn').click()

# post a comment
comment = "test"

box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "box")))
box.click()

frame = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//iframe[@title="+1"]')))
driver.switch_to.frame(frame)

driver.find_element_by_xpath('//div[@onclick]').click()

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@jsname="msEQQc"]/following-sibling::div//div[@g_editable="true"]')))
driver.execute_script("arguments[0].innerHTML='%s';" % comment, element)