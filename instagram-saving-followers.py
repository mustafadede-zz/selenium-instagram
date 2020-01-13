from selenium import webdriver
import random
import time
import getpass
browser=webdriver.Chrome()
link = "https://www.instagram.com"
browser.get(link)
time.sleep(2)
login = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a")
login.click()
time.sleep(2)
username_field = input("Your username: ")
password_field = input("Your password: ")
login_area = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input")
passwd_area = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")
login_area.send_keys(username_field)
passwd_area.send_keys(password_field)
loginbutton = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]/button")
loginbutton.click()
time.sleep(5)
message = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[1]/div/label/input")
mtext = input("Check your phone: ")
message.send_keys(mtext)
mverify = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[2]/button")
time.sleep(2)
mverify.click()
time.sleep(5)
browser.close()

