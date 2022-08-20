import random
import passgen
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# getting user data generation
username = str(input('Please,insert your username:\n'))
email = str(input('Please,insert your email:\n'))

if "@" not in email:
    print("@ is missing in email\n")
    exit()
day = str(random.randint(1, 28))
password = passgen.passgen(
    length=12, punctuation=False, digits=True, letters=True, case="both")

# Init selenium
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
actions = ActionChains(driver)
# getting url
driver.get("https://discord.com/register")


months = []
days = []
years = []

for i in range(0, 11):
    month = f'//*[@id="react-select-2-option-{i}"]'
    months.append(month)

for i in range(1, 28):
    day = f'//*[@id="react-select-3-option-{i}"]'
    days.append(day)

for i in range(19, 32):
    year = f'//*[@id="react-select-4-option-{i}"]'
    years.append(year)

# Performing

driver.find_element(By.CSS_SELECTOR, "[aria-label=Email]").click()
driver.find_element(By.CSS_SELECTOR, "[aria-label=Email]").send_keys(email)


driver.find_element(By.CSS_SELECTOR, "[aria-label=Username]").click()
driver.find_element(
    By.CSS_SELECTOR, "[aria-label=Username]").send_keys(username)


driver.find_element(By.CSS_SELECTOR, "[aria-label=Password]").click()
driver.find_element(
    By.CSS_SELECTOR, "[aria-label=Password]").send_keys(password)


# indicatorContainer
# Choosing Month
driver.find_element(By.XPATH, "//*[contains(@class, 'month-')]").click()
driver.find_element(By.XPATH, random.choice(months)).click()

# Choosing day
driver.find_element(By.XPATH, "//*[contains(@class, 'day-')]").click()
driver.find_element(By.XPATH, random.choice(days)).click()


driver.find_element(By.XPATH, "//*[contains(@class, 'year-')]").click()
driver.find_element(By.XPATH, random.choice(years)).click()


driver.find_element(By.CSS_SELECTOR, "[type=submit]").click()
time.sleep(30)


input('Please,solve captcha')

# Getting
token = driver.execute_script(
    'location.reload(); \
  var i=document.createElement("iframe"); \
  document.body.appendChild(i); \
  return i.contentWindow.localStorage.token').split('""')

print(
    f'Username is - {username}\n Email is - {email}\n Password is {password}\n Token is {token}')

actions.perform()
