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

sahibinden_arama = "renault clio"
ara = sahibinden_arama.split(" ")

driver.get('https://www.sahibinden.com/')
sleep(4)
    
#arama
driver.find_element(By.XPATH,'//*[@id="searchText"]')\
    .send_keys(sahibinden_arama)
driver.find_element(By.XPATH,'//*[@id="searchSuggestionForm"]/button')\
    .click()
sleep(3)

#çerezleri kabul etme
driver.find_element(By.XPATH,'//*[@id="onetrust-accept-btn-handler"]')\
    .click()
sleep(3)


driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchResultsSearchForm"]/div/div[3]/div[3]/div[2]/ul/li[2]/a'))))

sleep(3)
# boş liste
titles_list = []
prices_list = []
loca_list = []
date_list = []
km_list = []
for i in range(0,1000,20):
    driver.get("https://www.sahibinden.com/renault-clio-1.5-dci-joy?pagingOffset={2}".format(ara[0],ara[1],i))    
    sleep(4)
    item_titles = driver.find_elements(By.XPATH,'//*[@id="searchResultsTable"]/tbody/tr[*]/td[3]')
    item_prices = driver.find_elements(By.XPATH,'//*[@id="searchResultsTable"]/tbody/tr[*]/td[7]')
    item_loca = driver.find_elements(By.XPATH,'//*[@id="searchResultsTable"]/tbody/tr[*]/td[9]')
    item_date = driver.find_elements(By.XPATH,'//*[@id="searchResultsTable"]/tbody/tr[*]/td[4]')
    item_km = driver.find_elements(By.XPATH,'//*[@id="searchResultsTable"]/tbody/tr[*]/td[5]')



# Loop over the item_titles and item_prices
    for title in item_titles:
        titles_list.append(title.text)
    for prices in item_prices:
        prices_list.append(prices.text)
    for locat in item_loca:
        loca_list.append(locat.text)
    for dat in item_date:
        date_list.append(dat.text)
    for k in item_km:
        km_list.append(k.text)

print(titles_list)
print(prices_list)
print(loca_list)
print(date_list)

driver.quit()

dfS = pd.DataFrame(zip(titles_list, prices_list, loca_list, date_list, km_list), columns=['İlan Başlığı', 'Fiyat', 'Lokasyon', 'Yıl', 'Km'])
dfS['Fiyat'] = dfS['Fiyat'].str.replace('TL', '')
dfS['Lokasyon'] = dfS['Lokasyon'].str.replace('\n', '/')
a = dfS.to_excel("output_araCliojoy.xlsx",sheet_name='renaultClio') 
 