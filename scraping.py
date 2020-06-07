from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# add &hl=<language> to change the language
driver.get("https://play.google.com/store/apps/details?id=com.gojek.app&showAllReviews=true&hl=id")

# root = W4P4ne
# comments = UD7Dzf
try:
    root = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME,"LXrl4c"))
    )
    
    # auto scroll down
    i = 0
    y = 0
    while y<1:
        driver.execute_script("window.scrollBy(0,200000)","")
        time.sleep(1)
        i=i+1
        if i == 7 :
            button = driver.find_element_by_css_selector('span.CwaK9')
            button.click()
            i=0
            y=y+1

    # get data
    time.sleep(10)
    comments = root.find_elements_by_css_selector('div.UD7Dzf')
    count = 0
    for data in comments:
        comment = data.find_element_by_css_selector('span[jsname="fbQN7e"]')
        driver.execute_script("arguments[0].removeAttribute('style')", comment)
        comment = data.find_element_by_css_selector('span[jsname="fbQN7e"]')
        data = comment.text
        if data == "" : continue
        count= count+1
        print (data,'\n')
    print(count)
except :
    driver.quit()