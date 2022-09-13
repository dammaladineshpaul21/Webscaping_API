from selenium import webdriver

driver = webdriver.Safari(executable_path="/Applications/Safari.app")
print(driver.get(url="www.google.com"))
