from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys  

import time

options = Options()
options.binary_location = "C:\Program Files (x86)\Google\Chrome Beta\Application\chrome.exe"
driver = webdriver.Chrome(chrome_options = options, executable_path='chromedriver.exe')


driver.get("http://54.95.177.240:38080/index/page")
driver.implicitly_wait(3)


elem_user = driver.find_element_by_name("userName")
print('---------------------')

elem_user.clear
elem_user.send_keys("123")  

elem_pwd = driver.find_element_by_name("userPassword")
elem_pwd.clear
elem_pwd.send_keys("123")  
elem_pwd.send_keys(Keys.RETURN)

time.sleep(3)

driver.get('http://54.95.177.240:38080/report/getIncomeDetail')


#driver.quit()