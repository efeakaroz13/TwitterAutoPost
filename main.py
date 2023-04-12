import undetected_chromedriver as uc
import requests
import json 
from bs4 import BeautifulSoup
import pickle
import time
from selenium.webdriver.common.by import By
import random
import os

class PosterFaraday:
    def __init__(self,username):
        try:
            self.UserData = json.loads(open("s1.json","r").read())[username]
        except:
            raise ValueError("Couldn't find the user you requested")
        self.driver = uc.Chrome()
        cookies = pickle.load(open(f"cookies/{username}.pkl", "rb"))
        self.driver.get("https://twitter.com")
        
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        time.sleep(5)

    def postAuto(self):
        allData = json.loads(open("postInfo.json","r").read())
        posts = list(allData.keys())
        selectedPost = allData[random.choice(posts)]
        title = selectedPost["title"] +" "+ str(random.randint(1, 700))+" "
        tweet = self.driver.find_element(By.CSS_SELECTOR,"br[data-text='true']")
        tweet.send_keys(title)
        time.sleep(1)
        s = self.driver.find_element(By.XPATH,"//input[@type='file']")
        for i in selectedPost["images"]:

            s.send_keys(os.getcwd()+"/static/"+i)
        time.sleep(5)
        button = self.driver.find_element(By.CSS_SELECTOR,"div[data-testid='tweetButtonInline']")
        button.click()
        time.sleep(40)
        self.driver.quit()
        

if __name__ == "__main__":
    while True:
        allUsers = json.loads(open("s1.json","r").read())
        for a in allUsers:
            Pfaraday = PosterFaraday(a)
            Pfaraday.postAuto()
    




        