from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback

import re,time

def scroll_down(driver,height= 200):
    # slowly scroll to height
    for i in range(0,height,100):
        driver.execute_script(f'window.scrollTo(0,{i});')
        time.sleep(0.5)


phone_number = []

# Chrome options setup
chrome_options = Options()
chrome_options.add_argument(r"user-data-dir=C:\Users\mdash\AppData\Local\Google\Chrome\User Data")
# chrome_options.add_argument("profile-directory=Profile 1")



driver = webdriver.Chrome(options=chrome_options)

base_url = "http://google.com/"
driver.get(base_url)
driver.maximize_window()
search_key = "laptop shop near me"

time.sleep(1)

try:
    # search for laptop shop new me
    search_text_field = driver.find_element(By.ID,"APjFqb")
    search_text_field.send_keys(search_key+ Keys.ENTER)
    time.sleep(10)

    # click on more places
    height = driver.execute_script('return document.body.scrollHeight')

    print("height",height)

    scroll_down(driver)

   

    driver.find_element(By.XPATH,'//*[@id="Odp5De"]/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div[3]/div/h3/g-more-link/a/div').click()
    time.sleep(3)

    # find and click on each shop using class = "VkpGBb"

    all_shops = driver.find_elements(By.CLASS_NAME,'VkpGBb')
    print(len(all_shops))

    for shop in all_shops:
        shop.click()
        time.sleep(1)

        try:
            phone_number_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".LrzXr.zdqRlf.kno-fv"))
            )
            phone_number  = phone_number_element.text


            # Combined regex for USA and Bangladesh phone numbers
            pattern = r"^(\+1|1)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$|^(\+8801|01)\d{9}$"
        
            if re.match(pattern,phone_number ):
                phone_number.append(phone_number)

            print("phone_number == ",phone_number)
            time.sleep(1)
        except:
            pass



    # find/extract and regex match phone number using class = "class = LrzXr zdqRlf kno-fv"

except Exception as e:
    print(f"An error occurred: {e}")
    traceback.print_exc()  # This will print the full stack trace
    print(phone_number)
    input("Press Enter to close Chrome...")  # Keeps the browser open until you press Enter

finally:
    input("Press Enter to exit and close Chrome...")  # Ensures Chrome stays open until you manually close it
    print(phone_number)
    driver.quit()
