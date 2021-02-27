from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re

PATH = "/Users/hybriddollar/Documents/Coding/seleniumdriver/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://moodle.iitd.ac.in/login/index.php")
print(driver.title)

user1 = input("Enter your username: ")
user2 = input("Enter your password: ")


search = driver.find_element_by_id("username")
search.send_keys(user1)
search2 = driver.find_element_by_id("password")
search2.send_keys(user2)

#page = driver.page_source

login = driver.find_element_by_id("login")
#prompt = 0

#captcha check begin
def check(string): 
    if (string.find("second") != -1): 
        m = re.search('enter second value (.+?) =', string)
        if m:
            found = m.group(1)
        #print(found)
        x = found.split(" , ")
        print(x[1])
        prompt = x[1]
        search3 = driver.find_element_by_id("valuepkg3")
        search3.send_keys(prompt)


    elif (string.find("first") != -1): 
        m = re.search('enter first value (.+?) =', string)
        if m:
            found = m.group(1)
        #print(found)
        x = found.split(" , ")
        print(x[0])
        prompt = x[0]
        search3 = driver.find_element_by_id("valuepkg3")
        search3.send_keys(prompt)

    elif (string.find("add") != -1): 
        m = re.search('add (.+?) =', string)
        if m:
            found = m.group(1)
        #print(found)
        x = found.split(" + ")
        print(int(x[0])+int(x[1]))
        prompt = int(x[0])+int(x[1])
        search3 = driver.find_element_by_id("valuepkg3")
        search3.send_keys(prompt)

    elif (string.find("subtract") != -1): 
        m = re.search('subtract (.+?) =', string)
        if m:
            found = m.group(1)
        #print(found)
        x = found.split(" - ")
        print(int(x[0])-int(x[1]))
        prompt = int(x[0])-int(x[1])
        search3 = driver.find_element_by_id("valuepkg3")
        search3.send_keys(prompt)
    else:
        print("nothing found")


            
check(login.text) 

#print(login.text)

search2.send_keys(Keys.RETURN)

time.sleep(5)
driver.quit()