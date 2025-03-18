from selenium import webdriver
from selenium.webdriver.common.by import By
import re
driver = webdriver.Chrome()

prod_names = []
prod_images = []


base_url = "https://www.daraz.com.bd/mens-eyeglasses/"
driver.get(base_url)
driver.maximize_window()
total_item_xpath = '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/span[1]'
total_page = 2
try:
    total_item_text = driver.find_element(By.XPATH,total_item_xpath).text
    match = re.search(r'\d+', total_item_text)
    if match:
        number = match.group()
        total_page = int(number) // 40 
except:
    page_number_xpath = '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[3]/div/ul/li[8]'
    page_number_text = driver.find_element(By.XPATH,page_number_xpath).text
    try:
        total_page = int(page_number_text)
    except:
        pass
    

print(total_page)


for page in range(1,total_page):
    driver.get(base_url+"?page={}".format(page))
    driver.maximize_window()

    for i in range(1,10):
        base_xpath = '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[{}]/'.format(i)
        product_name_xpath = base_xpath + 'div/div/div[2]/div[2]/a'
        product_image_xpath = base_xpath + 'div/div/div[1]/div/a/div/img'
        product_name = driver.find_element(By.XPATH,product_name_xpath).text
        product_image_url = driver.find_element(By.XPATH,product_image_xpath).get_attribute('src')
        prod_names.append(product_name)
        prod_images.append(product_image_url)

print(len(prod_names))

driver.quit()