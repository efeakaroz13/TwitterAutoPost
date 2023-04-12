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


    def login(self,username,password,email,phonenumber,sname):
        self.driver = uc.Chrome()
        self.driver.get("https://twitter.com")
        self.driver.add_cookie({"name":"lang","value":"en"})
        time.sleep(10)


        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(10)
        self.driver.find_element(By.NAME,"text").send_keys(username)
        self.checkButton("Next")
        time.sleep(5)

        self.driver.find_element(By.NAME,'password').send_keys(password)

        time.sleep(5)
        self.checkButton('Log')
        #print('Logged in successfully')
        time.sleep(5)
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
        self.driver.quit()





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
