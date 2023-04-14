import undetected_chromedriver as uc
import requests
import json 
import time
from selenium.webdriver.common.by import By
from colorama import Fore
import pickle

accounts = open("accounts.txt","r").readlines()
"""
NOTE:Format: username:password:email:phonenumber
"""

class Faraday:
    def __init__(self):
        a=1

    def checkButton(self,buttonName):
        #text clicker 
        sc = """
        function clickButton(name_of_button){
  
            buttons = []
            alldivs = document.getElementsByTagName("div")
            for(d in alldivs){
                
                role = alldivs[d].role
                
                if(role == "button"){
                    buttons.push(alldivs[d])
                }
            }
            for(b in buttons){
                button = buttons[b];
                if(button.textContent.includes( name_of_button) == 1){
                    button.click()
                }
            }
        }
        clickButton('"""+buttonName+"""');
        """
        self.driver.execute_script(sc)
    def checkButton_a_l(self,buttonName):
        #aria label clicker
        sc = """
        function clickButton(name_of_button){
  
            buttons = []
            alldivs = document.getElementsByTagName("div")
            for(d in alldivs){
                
                role = alldivs[d].role
                
                if(role == "button"){
                    buttons.push(alldivs[d])
                }
            }
            for(b in buttons){
                button = buttons[b];
                if(button.getAttribute('aria-label').includes( name_of_button) == 1){
                    button.click()
                }
            }
        }
        clickButton('"""+buttonName+"""');
        """
        self.driver.execute_script(sc)


    def login(self,username,password,email,phonenumber,sname):
        try:
            self.driver = uc.Chrome()

            self.driver.get("https://twitter.com")
            self.driver.add_cookie({"name":"lang","value":"en"})
        except:
            self.driver.quit()

            return {"SCC":False,"err":"Twitter.com'a bağlanılamadı"}
        time.sleep(5)


        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(2)
        try:
            self.driver.find_element(By.NAME,"text").send_keys(username)
        except:
            self.login(username,password,email,phonenumber,sname)
        self.checkButton("Next")
        time.sleep(2)
        try:
            self.driver.find_element(By.NAME,'password').send_keys(password)
        except:
            time.sleep(2)
            try:
                self.driver.find_element(By.NAME,'password').send_keys(password)
            except:
                return {"SCC":False,"err":"Şifre girişi penceresi bulunamadı - Chrome"}

        time.sleep(1)
        self.checkButton('Log')
        #print('Logged in successfully')
        time.sleep(2)
        pickle.dump(self.driver.get_cookies(),open(f'cookies/{username}.pkl','wb'))
        print(Fore.GREEN,f'SUCCESS | {username}.pkl',Fore.RESET,time.ctime(time.time()))
        try:
            dataRead = json.loads(open(f'{sname}.json','r').read())
        except:
            dataRead = {}
        data = {
            'username':username,
            'password':password,
            'email':email,
            'phonenumber':phonenumber,
            'lastLogin':time.time(),
            'timeLoggedIn':time.time(),
            'cookies':f'{username}.pkl'
        }


        dataRead[username] = data

        open(f'{sname}.json','w').write(json.dumps(dataRead,indent=4))
        time.sleep(300)
        self.driver.quit()
        return {"SCC":True,"err":""}





if __name__ == "__main__":
    faraday = Faraday()
    
    for a in accounts:
        allpieces = a.replace('\n','').split(':')
        username = allpieces[0]
        password = allpieces[1]
        email = allpieces[2]
        phone = allpieces[3]


        faraday.login(username,password,email,phone,'s1')

    print(Fore.BLUE,'Task Completed.')
