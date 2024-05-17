#%%
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import os, sys
import pandas as pd
import openpyxl
import random
import re
import requests
import pyperclip

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as bs
from selenium.webdriver.support.ui import Select

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import NoSuchElementException

from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoAlertPresentException,\
     UnexpectedAlertPresentException

#from webdriver_manager.chrome import ChromeDriverManager

import ss_source_file_update
import ss_auto_chromedriver


def log_in(driver):                      
    #url = 'https://blog.naver.com/bizinfo1357'
    url = 'https://blog.naver.com/prologue/PrologueList.nhn?blogId=bizinfo1357&directAccess=true'

    driver.implicitly_wait(2)
    
    driver.get(url)
    driver.implicitly_wait(2)
 
    return driver

def save_html (driver, filename):
    soup_html = bs(driver.page_source, 'html.parser')

    with open(filename, "w", encoding='utf-8') as file:
        file.write(str(soup_html))
    
def get_detail_info(soup_html):

    df = pd.DataFrame()

    for i in range(2):
        for j in range(8):
            #     결산년1_contents :   GMClassReadOnly GMWrap0 GMAlignCenter GMText GMCell IBSheetFont3 HideCol3C1
            #     결산년2_contents :    GMClassReadOnly GMWrap0 GMAlignCenter GMText GMCell IBSheetFont4 HideCol4C1                                              
            column_class = [f"GMWrap0 GMAlignCenter GMHeaderText IBSheetFont3 GMCellHeader IBSheetFont3 HideCol3C{j+1}",
                            f"GMEllipsis GMAlignCenter GMHeaderText IBSheetFont4 GMCellHeader IBSheetFont4 HideCol4C{j+1}"]

            column_content = [f"GMClassReadOnly GMWrap0 GMAlignRight GMFloat GMCell IBSheetFont3 HideCol3C{j+1}",
                              f"GMClassReadOnly GMEllipsis GMAlignRight GMFloat GMCell IBSheetFont4 HideCol4C{j+1}"]
 
            column_name_scr = soup_html.find(class_ = column_class[i])
            
            if j == 0:
                column_content[j] = f"GMClassReadOnly GMWrap0 GMAlignCenter GMText GMCell IBSheetFont{3+i} HideCol{3+i}C1"
                
            column_content_scr = soup_html.find_all(class_ = column_content[i])
            
            if column_name_scr:
                column_name = column_name_scr.get_text()
                print(column_name)
            
                for k in range(len(column_content_scr)):
                    print(k, column_content_scr[k].get_text())
                    
                    df.loc[k, column_name] = column_content_scr[k].get_text()   
    return df

driver = ss_auto_chromedriver.start()
print("try to login...")

#%%
driver.get('https://nid.naver.com/nidlogin.login')
time.sleep(1)


# 로그인 버튼을 찾고 클릭합니다

print("td, pw 입력할 곳을 찾습니다...")
# id, pw 입력할 곳을 찾습니다.
#tag_id = driver.find_element_by_name('id')

tag_id = driver.find_element("id", 'id')
tag_pw = driver.find_element("id", 'pw')
tag_id.clear()

time.sleep(1)

# id 입력
tag_id.click()
pyperclip.copy('    ')
tag_id.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# pw 입력
tag_pw.click()
pyperclip.copy('   ')
tag_pw.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# 로그인 버튼을 클릭합니다
login_btn = driver.find_element("id", 'log.login')
login_btn.click()

time.sleep(4)


driver = log_in(driver)

soup_html = bs(driver.page_source, 'html.parser')

subs = soup_html.findAll(class_="p_photo_d")

for i in range(5):  #len(subs)
    
    sub_url = subs[i].find("a")["href"]
    driver.get(sub_url)

    driver.find_element("class name", '_spi_blog').click()  # spi_btn_blog
    time.sleep(0.5)

    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    
    driver.find_element("id", '_submit').click()  # spi_btn_blog
    time.sleep(0.5)
    driver.switch_to.window(handles[0])
        
    #driver.find_element_by_class_name('pop_btn')
    
save_html(driver, f"blog.html")

# %%

