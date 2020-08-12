from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})

chromedriver = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(chromedriver, chrome_options=option)

def login():
    username = '18189818@smail.ilc.edu.tw'
    password = 'entroy0421'
    url = 'https://www.facebook.com'
    driver.get(url)
    search_username = driver.find_element_by_name('email')
    search_username.send_keys(username)
    search_password = driver.find_element_by_name('pass')
    search_password.send_keys(password)
    submit_button = driver.find_element_by_name('login')
    submit_button.click()
    time.sleep(5)

def npc_go_page():
    url = 'https://www.facebook.com/NPC.OwO/inbox/'
    driver.get(url)
    time.sleep(5)
    with open('html.html', 'w') as f:
        f.write(driver.page_source)
    try:
        search_new_message = driver.find_element_by_css_selector('div._5hhj')
        print(search_new_message)
        # search_new_message.click()
        print('success')
    except:
        print('fail')

login()
npc_go_page()
driver.close()