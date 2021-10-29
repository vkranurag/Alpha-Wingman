from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://google.com')

Gmail = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div[1]/div[1]/a')
Gmail.click()

signinButton = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[4]/ul[1]/li[2]/a')
signinButton.click()


