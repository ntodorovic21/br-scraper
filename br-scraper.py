from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from twilio.rest import Client
import time

# Log into Twilio
account_sid = 'ACaff4b68bbd238f9ce1c9399fd5e80f94'
auth_token = '0aa4d73cb39daff1dc176b8cad67b037'
client = Client(account_sid, auth_token)


def send_text():
    message = client.messages \
        .create(
        body="Hey Nick, the Maverick Tan Castello is finally available!",
        from_='+15085909648',
        to='+19175307727'
    )


while True:
    chrome_browser = webdriver.Chrome('./chromedriver')
    chrome_browser.get(
        'https://bananarepublic.gap.com/browse/product.do?pid=795829022&cid=1174308&pcid=873&vid=1&nav=meganav%3AMen%3AMen%27s%20Clothing%3ACasual%20Shirts#pdp-page-content')
    try:
        time.sleep(1)
        chrome_browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
        color_btn = chrome_browser.find_element(By.ID, 'buybox-color-swatch--Maverick-Tan')
        color_btn.click()
        time.sleep(1)
        size_btn = chrome_browser.find_element(By.ID, 'variant-1-sizeDimension1-S')
        size_btn.click()
        time.sleep(1)
        add_to_bad_btn = chrome_browser.find_element(By.ID, 'AddToBagFromBuyBox_add-to-bag__button')
        if add_to_bad_btn.is_enabled():
            print('In STOCKKKKKKK!!!!')
            send_text()
            break
        else:
            print('Not in stock :(')
            chrome_browser.quit()
            time.sleep(300)
    except:
        chrome_browser.quit()
        time.sleep(300)