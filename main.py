import undetected_chromedriver as uc
import requests
import json 
from bs4 import BeautifulSoup
import pickle
import time
from selenium.webdriver.common.by import By
import random
import os
import re
import string
alphabet = list(string.ascii_lowercase)

class PosterFaraday:
    def __init__(self,username):
        try:
            self.f = int(open("f.txt","r").read())
        except:
            raise ValueError("frequency needs to be int, f.txt")
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
        try:
            timestart = time.time()

            allData = json.loads(open("postInfo.json","r").read())
            posts = list(allData.keys())
            selectedPost = allData[random.choice(posts)]
            title = selectedPost["title"]+random.choice(alphabet)+str(random.randint(1,9))
            tweet = self.driver.find_element(By.CSS_SELECTOR,"br[data-text='true']")
            import re
            title = title.replace("|","\n")



            emoji_pattern = re.compile("["
                    u"\U0001F600-\U0001F64F" 
                    u"\U0001F300-\U0001F5FF"  
                    u"\U0001F680-\U0001F6FF"  
                    u"\U0001F1E0-\U0001F1FF"  
                                    "]+", flags=re.UNICODE)
            title = emoji_pattern.sub(r'', title) 
            tweet.send_keys(title)
            time.sleep(1)
            s = self.driver.find_element(By.XPATH,"//input[@type='file']")
            for i in selectedPost["images"]:

                s.send_keys(os.getcwd()+"/static/"+i)
                time.sleep(2)
            timeend = time.time()
            button = self.driver.find_element(By.CSS_SELECTOR,"div[data-testid='tweetButtonInline']")
            button.click()

            time.sleep(self.f)
            self.driver.quit()
        
        except Exception as e:
            print(Fore.RED,e,Fore.RESET)

if __name__ == "__main__":
    while True:
        allUsers = json.loads(open("s1.json","r").read())
        for a in allUsers:
            Pfaraday = PosterFaraday(a)
            Pfaraday.postAuto()
    




        