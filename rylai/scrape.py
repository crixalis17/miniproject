from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import urllib.request
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\chromedriver.exe"
options = webdriver.ChromeOptions()
#username = 
#password =     
driver = webdriver.Chrome(service=Service("C:\\chromedriver.exe"),options =options)
driver.get("https://twitter.com/RAMESH_ROKETMAN")

#time.sleep(10)
profile_pic_click = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div/div[2]/div/a/div[4]/div"))).click()

profile_pic = driver.find_element(By.XPATH,"//img[contains(@class,'css-9pa8cd')]").get_attribute('src')
urllib.request.urlretrieve(str(profile_pic),r"C:\Users\Asus\Documents\miniproject\files\output_files\profile_pic.jpg")

close_button_click = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//div[@role='button']"))).click()

profile_name = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/h2/div/div/div/div/span[1]/span/span")))
all_tweets =set()
time.sleep(2)
tweets = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH,"//div[@data-testid='tweetText']")))
for tweet in tweets:
    all_tweets.add(tweet.text)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
time.sleep(2)
tweets = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH,"//div[@data-testid='tweetText']")))
for tweet in tweets:
    all_tweets.add(tweet.text)

print(profile_name.text)

print(all_tweets,len(all_tweets))



