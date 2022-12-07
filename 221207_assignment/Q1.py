number=input()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup

specific_options = webdriver.ChromeOptions() 
specific_options.add_argument('--headless') 
specific_options.add_argument('--no-sandbox')
driver = webdriver.Chrome('chromedriver', options = specific_options)

driver.get('https://m.dhlottery.co.kr/gameResult.do?method=allWin') 
time.sleep(1)

code_box1 = driver.find_element(By.NAME, 'drwNoStart')
code_box1.send_keys(number)
time.sleep(1)

code_box2 = driver.find_element(By.NAME, 'drwNoEnd')
code_box2.send_keys(number)
time.sleep(1)

b1 = driver.find_element(By.XPATH, '//*[@id="searchBtn"]/span')
b1.click()
time.sleep(1)

soup = BeautifulSoup(driver.page_source, 'html.parser')
winner = soup.find_all('strong')
winner_number=str(winner[1])
if(winner_number[14]=='<'):
  print(winner_number[13])
else: 
  print(winner_number[13]+winner_number[14])