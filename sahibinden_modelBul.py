from selenium import webdriver
from time import sleep
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

options = Options()  
options.add_argument("--headless")  
 
driver = webdriver.Firefox(options=options)
driver.maximize_window()

driver.get('https://www.sahibinden.com/renault-clio-1.5-dci')
sleep(4)

#çerezleri kabul etme
driver.find_element(By.XPATH,'//*[@id="onetrust-accept-btn-handler"]')\
    .click()
sleep(3)


# boş liste
titles_list = []
count_list = []
loca_list = []

for li in driver.find_elements(By.CLASS_NAME,"jspPane"):
    for a in li.find_elements(By.TAG_NAME,"a"):
        if(a.get_attribute("title") == "" ):
            break
        titles_list.append(a.get_attribute("title"))
        
for li in driver.find_elements(By.CLASS_NAME,"jspPane"):
    for a in li.find_elements(By.TAG_NAME,"span"):
        if(a.get_attribute("innerHTML") == "19.916"):
            break
        count_list.append(a.get_attribute("innerHTML"))
        
print(titles_list)
print(count_list)

driver.quit()

dfS = pd.DataFrame(zip(titles_list, count_list),
                           columns=['Araba Modeli', 'Model Sayısı'])
dfS['Model Sayısı'] = dfS['Model Sayısı'].str.replace('(', '')
dfS['Model Sayısı'] = dfS['Model Sayısı'].str.replace(')', '')
a = dfS.to_excel("output_modelBul3.xlsx", sheet_name='arabaBul')