import webbrowser
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Ie()
driver.get("http://lab-iniws01.in.lab/WebAdmins/Login.aspx")

txtusername = driver.find_element(By.XPATH, "//input[@name='ctl00$BaseContent$txtUsername']")
txtpassword = driver.find_element(By.XPATH, "//input[@name='ctl00$BaseContent$txtPassword']")
btnlogin= driver.find_element(By.XPATH, "//span[@id='ctl00_BaseContent_btnLogin_ShadowButtonSpan']")

txtusername.send_keys("_rdbuild")
txtpassword.send_keys("RDBu1ld01")

btnlogin.click()

os.system("TASKKILL /F /IM IEDriverServer.exe")