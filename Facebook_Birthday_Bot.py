from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r"C:\Users\Lenovo\Desktop\APPLICATION1\RESUME_PROJECTS\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.facebook.com/")
time.sleep(2)
email_id = "aapte.kedaar20@gmail.com"
password1 = "narayanapte20"
email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys(email_id)
password = driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys(password1)
time.sleep(10)
log_in_button = driver.find_element_by_xpath('//*[@id="u_0_k_EH"]')
log_in_button.send_keys(Keys.ENTER)
#time.sleep(10)
# driver.switch_to.alert().dismiss()
birthdays = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div[3]/div/div/div[1]/div/div[1]/div/div[2]/div/a/div[1]/div[2]/div/div/div/div/span')
time.sleep(2)
birthdays.click()
time.sleep(2)
birthday_boxes = driver.find_elements_by_css_selector("._1mf._1mj")
count = 0
for els in birthday_boxes:
    try:
        count +=1
        els.send_keys("Happy Birthday!")
        print("Birthday Wish posted for friend" + str(count)) 
    except:
        print("couldn't post")
time.sleep(2)

driver.close()