from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from keyboard import press
import time
from playsound import playsound

username = "username"
password = "password"
driver = webdriver.Chrome()
driver.get("https://booking.bbdc.sg/#/login?redirect=%2Fhome%2Findex")
logu = driver.find_element(By.ID, "input-8")
logu.send_keys(username)
logp = driver.find_element(By.ID,  "input-15")
logp.send_keys(password)
login = driver.find_element(By.CLASS_NAME, "v-btn.v-btn--is-elevated.v-btn--has-bg.theme--light.v-size--default.primary")
login.send_keys(Keys.ENTER)
time.sleep(4)
driver.get("https://booking.bbdc.sg/#/booking/index")
time.sleep(2)
practical = driver.find_element(By.CLASS_NAME, "v-tab")
practical.send_keys(Keys.TAB)
press("enter")
time.sleep(3)
bkslt = driver.find_element(By.CSS_SELECTOR, "button.v-btn--is-elevated.v-btn--has-bg.theme--light.v-size--default.primary")
bkslt.click()
time.sleep(2)
bknext = "https://booking.bbdc.sg/#/booking/instructorType?subStageSubNo&instructorType="
cur = driver.current_url
while cur == bknext:
    next = driver.find_element(By.CSS_SELECTOR, "button.v-btn--is-elevated.v-btn--has-bg.theme--light.v-size--default.primary")
    next.click()
    time.sleep(7)
    cur = driver.current_url
    time.sleep(30)
playsound("soundfile.mp3")
time.sleep(120)
driver.close()