from selenium import webdriver
from selenium.webdriver.common.by import By
import time,math

driver = webdriver.Chrome()

base_url = "https://www.daraz.com.bd/products/white-punjabi-with-chest-contrast-soft-cotton-brand-new-design-for-men-i325255990-s1871312346.html?pvid=24c4448c-4b02-489c-8f0c-19011a05f643&search=jfy&scm=1007.51705.413671.0&spm=a2a0e.tm80335411.just4u.d_325255990"
driver.get(base_url)
driver.refresh()
driver.maximize_window()

height = driver.execute_script('return document.body.scrollHeight')

print("height",height)

# slowly scroll to height
for i in range(0,height+500,50):
    driver.execute_script(f'window.scrollTo(0,{i});')
    time.sleep(0.5)


# get comments
list_of_comments = []
total_comments_page = 5
try:
    total_comments_page = int(driver.find_element(By.XPATH,'//*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[5]').text)
except:
    pass

number_of_iteration = math.ceil(total_comments_page/3)

j = 2
for i in range(number_of_iteration+1):
    button_xpath = f'//*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[{j}]'
    button = driver.find_element(By.XPATH,button_xpath)
    button.click()
    time.sleep(0.5)
    all_comments = driver.find_elements(By.CLASS_NAME,'content')
    for comment in all_comments:
        list_of_comments.append(comment.text)
    j+=1
    if j == 5:
        j = 2
    if i == number_of_iteration:
        print("======button 5 ======")
        button_xpath = f'//*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[5]'
        button = driver.find_element(By.XPATH,button_xpath)
        button.click()
        time.sleep(0.5)
        all_comments = driver.find_elements(By.CLASS_NAME,'content')
        for comment in all_comments:
            list_of_comments.append(comment.text)

print("list_of_comments ====",list_of_comments)
print("list_of_comments length====",len(list_of_comments))