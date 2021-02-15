from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import time

# Variables
data = dict()
data = {
    'user': 'seu_usuario',
    'password': 'sua_senha',
    'publication': 'https://www.instagram.com/p/CLPq6VoBEz_/',
    'comments_per_hour': 60,
    'interval_between_hours_in_minutes': 10 
}

# Setup browser

options = Options()
options.set_preference('dom.webnotifications.enabled', False)
browser = webdriver.Firefox(options=options)

browser.get('https://www.instagram.com/')
time.sleep(3)

# Login

user = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
time.sleep(1)
user.send_keys(data['user'])
time.sleep(1)

password = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
time.sleep(1)
password.send_keys(data['password'])
time.sleep(1)

button = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
time.sleep(2)
button.click()

# Acess Publication

time.sleep(5)
browser.get(data['publication'])


# Comment
time.sleep(2)

while(True):
    for i in range(data['comments_per_hour']):
        comment_session = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
        comment_session.click()
        time.sleep(1)
        comment_session = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
        comment_session.send_keys('1')
        time.sleep(1)
        button = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]')
        button.click()

        time.sleep(3600/data['comments_per_hour'])
    
    time.sleep(60*data['interval_between_hours_in_minutes'])