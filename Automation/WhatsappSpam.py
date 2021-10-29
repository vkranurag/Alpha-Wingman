# import pywhatkit
# pywhatkit.sendwhatmsg('+918547914830','hello',13,45)

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')

name = input('Enter the name of user or group : ')
msg = input('Enter your message : ')
count = int(input('Enter the count : '))


user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_2Ujuu')
    button.click()