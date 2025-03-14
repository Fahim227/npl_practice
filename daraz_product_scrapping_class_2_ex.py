from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://pages.daraz.com.bd/wow/gcp/route/daraz/mm/upr/router?hybrid=1&data_prefetch=true&prefetch_replace=1&at_iframe=1&wh_pid=%2Flazada%2Fchannel%2Fbd%2Fflashsale%2F8r7TbxhpSH&hide_h5_title=true&lzd_navbar_hidden=true&disable_pull_refresh=true&skuIds=209458762%2C278279920%2C313603687%2C316103715%2C268465263%2C183983642%2C419352635&spm=a2a0e.tm80335411.FlashSale.d_shopMore")

prod_names = []
prod_images = []

for i in range(1,10):
    base_xpath = '//*[@id="campaign-undefined"]/div/div/a[{}]/div/'.format(i)
    product_name_xpath = base_xpath + 'div[2]/div[1]' # //*[@id="campaign-undefined"]/div/div/a[1]/div/div[2]/div[1]
    product_image_xpath = base_xpath + 'div[1]/div/img'
    product_name = driver.find_element(By.XPATH,product_name_xpath).text
    product_image_url = driver.find_element(By.XPATH,product_image_xpath).get_attribute('src')
    prod_names.append(product_name)
    prod_images.append(product_image_url)

print(prod_names)
print(prod_images)
