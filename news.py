import selenium
from selenium.webdriver import Chrome

def getl():
    driver=Chrome(executable_path="C:\webdriver\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://va-news-app.web.app/")
    #link=driver.find_element_by_name("alanBtn")
    #link.click()
    driver.maximize_window()