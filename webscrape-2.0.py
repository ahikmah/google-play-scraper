########################## Selector ##############################
# review column = div.LXrl4c
# comments = div.UD7Dzf
# short comment = span[jsname="bN97Pc"]
# long comment = span[jsname="fbQN7e"]
# load more button = span.CwaK9
#################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

start = time.time()

namefile = input('Input file name to export data : ')
# lazyload = input("Number of looping lazy load : ")
count = input("Number of data : ")

PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

def exportfile (dataset):
    comment_list = list(dataset)
    df = pd.DataFrame(data={'comment':comment_list})
    df.to_csv(namefile+'.csv', mode='a', header =False, index =False)

def scrolldown():
    i = 0
    for i in range(12):
        time.sleep(1)
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')               
        i = i+1
# get URL
# add &hl=<language> to change the language
driver.get("https://play.google.com/store/apps/details?id=com.gojek.app&showAllReviews=true&hl=id")

comment_set = set()

try:
    root = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME,'LXrl4c'))
    )
    
  
         
    while len(comment_set) < int(count):
        try:
            i = 0
            button = driver.find_element_by_css_selector('span.CwaK9')
            for i in range(5):
                button.click()   
                scrolldown()
                i = i+1
        except:
            i = 0
            scrolldown()
            for i in range(5):
                button = driver.find_element_by_css_selector('span.CwaK9')
                button.click()  
                scrolldown()
                i = i+1

        # get data
        comments = root.find_elements_by_class_name('UD7Dzf')
        for data in comments:
            # display full comment by removing style attribut
            expand = data.find_element_by_css_selector('span[jsname="fbQN7e"]')
            driver.execute_script('arguments[0].removeAttribute("style")', expand)
            
            if expand.text == '' : 
                comment = data.find_element_by_css_selector('span[jsname="bN97Pc"]')
            else :
                comment = expand        

            if comment.text in comment_set : continue
            comment_set.add(comment.text)
            print(len(comment_set),'data has been added successfully...')
            if len(comment_set)>int(count):break
        
    exportfile(comment_set)
    
    print('\n----------------------------------------------------\n'+
            '\t\tWEB SCRAPING SUCCESS\n'+
            '----------------------------------------------------')

except:
    print('Something wrong happened')
    driver.quit()
    
print('Total Time: ', time.time()-start, 'seconds..')
print('Finished at: ', time.ctime())

driver.quit()