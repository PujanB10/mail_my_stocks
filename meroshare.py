from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
from webdriver_manager.firefox import GeckoDriverManager




class web_driver():
    options = webdriver.FirefoxOptions()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920x1080')

    # Add user agent
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36')
    options.add_argument("--start-maximized")


    # Function that calls and runs the webdriver
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=options)
    wait = WebDriverWait(driver,30)



def login():

    # Takes login credentials from meroshareCredentials.txt
    with open("meroshareCredentials.txt") as userFile:
            lines = userFile.readlines()
            try:
                username = lines[0].split('=')[1].strip()
                password = lines[1].split('=')[1].strip()
                dpNumber = lines[2].split('=')[1].strip()
            except Exception as e:
                print("Ignored None type",e)

    # Enters meroshare website
    web_driver.driver.get('https://meroshare.cdsc.com.np/#/login')
    web_driver.wait.until(EC.presence_of_element_located((By.TAG_NAME, "app-login")))
    web_driver.wait.until(EC.presence_of_element_located((By.NAME, "selectBranch")))
    web_driver.driver.find_element(By.NAME ,"selectBranch").click()

    # Clicking on dp entry box
    dp_entry = web_driver.driver.find_element(By.CLASS_NAME, "select2-search__field")   
    dp_entry.click()  

    # Adding value to the dp entry box
    dp_entry.send_keys(dpNumber)  
    dp_entry.send_keys(Keys.ENTER)

    # Find and input username in the username text box  
    input_username = web_driver.driver.find_element(By.ID,'username')
    input_username.send_keys(username)

    # Find and input password in the password box
    input_pw = web_driver.driver.find_element(By.ID,'password')
    input_pw.send_keys(password)

    time.sleep(2)

    # Click login
    web_driver.driver.find_element(By.CLASS_NAME ,"sign-in").click()



def my_stocks():
    login()
    dictStocks = {}
    actions = ActionChains(web_driver.driver)

    # Wait for appearance of dashboard and navigates to My Shares of Mero Share
    web_driver.wait.until(EC.presence_of_element_located((By.TAG_NAME,"app-dashboard")))
    web_driver.wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/app-dashboard/div/div[1]/nav/ul/li[3]/a/span")))
    web_driver.driver.find_element(By.XPATH,"/html/body/app-dashboard/div/div[1]/nav/ul/li[3]/a/span").click()

    # Navigates to table containing the information of my shares
    web_driver.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,"tr")))
    rows = web_driver.driver.find_elements(By.TAG_NAME,"tr")
    for row in rows:
        try:
            scriptShort = row.find_elements(By.TAG_NAME,'td')[1]
            quantity = row.find_elements(By.TAG_NAME,'td')[2].text

            # Hovers over the script abbreviations to make its full name appear
            actions.move_to_element(scriptShort)
            actions.perform()
            web_driver.wait.until(EC.presence_of_element_located((By.CLASS_NAME,"tooltip-inner")))

            # Scrapes the full-name of the shares through tooltip
            scriptName = web_driver.driver.find_element(By.CLASS_NAME,"tooltip-inner").text.split("-")[0]
            dictStocks[scriptName[:-1]] = {'quantity':int(quantity)}
        except Exception as e:
            print('Out of range; Ignored')

    web_driver.driver.close()

    return dictStocks



if __name__ == "__main__":
   print(my_stocks())