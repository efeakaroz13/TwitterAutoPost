import undetected_chromedriver as uc
import requests
import json 
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By

accounts = open("accounts.txt","r").readlines()
"""
NOTE:Format: username:password:email:phonenumber
"""

class Faraday:
    def __init__(self):
        self.driver = uc.Chrome()

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


    def login(self,username,password,email,phonenumber):
        
        self.driver.get("https://twitter.com/i/flow/login")
        
        script = """
        var username = '"""+username+"""';
        var email    = '"""+email+"""';
        var password = '"""+password+"""';
        var phone = '"""+phonenumber+"""';

        document.getElementsByName('text')[0].value = username;



        """
