from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import urllib.request
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
import pandas as pd


def webscrape(website):
    path = "C:\chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(path),options =options)
    driver.get(website)
    '''
    username = "e.rakesh176@gmail.com"
    password = "rakerocks1707"
    phno = "9176206231"
    twt_username = website.split('/')[-1]
    href = '/' + twt_username
    login_button_click = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//a[@data-testid='login']"))).click()
    enter_username = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//input[@autocomplete='username']")))
    time.sleep(2)
    enter_username.click()
    enter_username.send_keys(username)
    enter_username.send_keys(Keys.ENTER)

    enter_phno = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//input[@data-testid='ocfEnterTextTextInput']")))
    time.sleep(2)
    enter_phno.click()
    enter_phno.send_keys(phno)
    enter_phno.send_keys(Keys.ENTER)

    enter_password = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//input[@name='password']")))
    time.sleep(2)
    enter_password.click()
    enter_password.send_keys(password)
    enter_password.send_keys(Keys.ENTER)
    
    time.sleep(5)
    search_box = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")))
    time.sleep(2)
    search_box.click()
    search_box.send_keys(twt_username)
    search_box.send_keys(Keys.ENTER)

    username_select = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[1]/div/div/div/article/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div[2]/div/a"))).click()
    time.sleep(2)
    '''
    profile_pic_click = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div/div[2]/div/a/div[4]/div"))).click()
    time.sleep(2)
    profile_pic = driver.find_element(By.XPATH,"//img[contains(@class,'css-9pa8cd')]").get_attribute('src')
    urllib.request.urlretrieve(str(profile_pic),r"C:\Users\Asus\Documents\miniproject\static\profile_pic.jpg")

    close_button_click = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//div[@role='button']"))).click()

    profile_name = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/h2/div/div/div/div/span[1]/span/span")))
    all_tweets =set()
    time.sleep(2)
    tweets = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH,"//div[@data-testid='tweetText']")))
    for tweet in tweets:
        all_tweets.add(tweet.text)
    time.sleep(1)
    #driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    #time.sleep(2)
    #tweets = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH,"//div[@data-testid='tweetText']")))
    #for tweet in tweets:
    #    all_tweets.add(tweet.text)

    #print(profile_name.text)

    #print(all_tweets,len(all_tweets))

    df = pd.DataFrame(all_tweets,columns=["OriginalTweets"])
    df.to_csv(r'C:\Users\Asus\Documents\miniproject\files\input_files\tweets_after_scraping.csv')

    return profile_name.text



