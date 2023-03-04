from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from  PIL import Image


def gmail_login(email_id,password):
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--user-data-dir')
        chrome_options.add_argument('--disable-web-security')
        chrome_options.add_argument('--allow-running-insecure-content')
        chrome_options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome()

        driver.get("https://www.gmail.com")

        driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+\
        'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
        '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
        print("yes")
        driver.implicitly_wait(15)
    
        loginBox = driver.find_element('xpath','//*[@id ="identifierId"]')
    
        loginBox.send_keys(email_id)
    
        nextButton = driver.find_elements('xpath','//*[@id ="identifierNext"]')
        nextButton[0].click()
    
        passwordBox = driver.find_element('xpath',
            '//*[@id ="password"]/div[1]/div / div[1]/input')
        passwordBox.send_keys(password)
    
        nextButton = driver.find_elements('xpath','//*[@id ="passwordNext"]')
        nextButton[0].click()
        driver.implicitly_wait(60)
        driver.save_screenshot("ss.png")
        img = Image.open("ss.png")
        img.show()

        
    
        print('Login Successful...!!')
        

    except:
        print("Error")




