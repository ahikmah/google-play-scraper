########################## Selector ##############################
# review column = div.LXrl4c
# comments = div.UD7Dzf
# full comment text = span[jsname="fbQN7e"]
# load more button = span.CwaK9
#################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Gojek URL
# add &hl=<language> to change the language
driver.get("https://play.google.com/store/apps/details?id=com.gojek.app&showAllReviews=true&hl=id")

i = 0
y = 0
comment_list = list()
count = 0

try:
    root = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME,'LXrl4c'))
    )

    # auto scroll down
    while y<1000:
        driver.execute_script('window.scrollBy(0,10000)', '')
        time.sleep(1)
        i=i+1
        if i == 7 :
            button = driver.find_element_by_css_selector('span.CwaK9')
            button.click()
            i=0
            y=y+1

    # get data
    comments = root.find_elements_by_class_name('UD7Dzf')
    for data in comments:
        comment = data.find_element_by_css_selector('span[jsname="fbQN7e"]')
        driver.execute_script('arguments[0].removeAttribute("style")', comment)
        comment = data.find_element_by_css_selector('span[jsname="fbQN7e"]')
        if comment.text == '' : continue
        count= count+1
        print(count,'data has been added successfully..')
        comment_list.append(comment.text)

    # export to datasets.csv file
    df = pd.DataFrame(data={'comments':comment_list})
    df.to_csv('./dataset-gojek.csv', sep=',', index =False)

except :
    print('Astaghfirullah....')
    driver.quit()