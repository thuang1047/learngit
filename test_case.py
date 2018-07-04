# csdn 登录测试

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.csdn.net")
driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element_by_link_text("登录").click()
driver.find_element_by_xpath("/html/body/div/div/div/div/div/h3/a").click()

driver.find_element_by_id("username").send_keys("your username")
driver.find_element_by_id("password").send_keys("your password")
driver.find_element_by_class_name("logging").click()

sleep(2)
driver.quit()
print("Loggin CSDN successful!")
