import platform
from selenium import webdriver

def getTextAndSave(url, fileName):
    driver = ""
    if platform.system() == "Window":
        driver = webdriver.PhantomJS('C:\\Users\\user\\Downloads\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
    else:
        driver = webdriver.PhantomJS('../pj/mac/phantomjs')
    driver.get(url)
    delay_time = 2
    driver.implicitly_wait(delay_time)

    html = driver.page_source
    file = open("./" + fileName, "w+")
    file.write(html)