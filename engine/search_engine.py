from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def google_search(search_item):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach",True)

    driver = webdriver.Chrome(options=option)
    driver.maximize_window()

    driver.get("https://www.google.com")
    my_element = driver.find_element(By.ID,"APjFqb")
    my_element.send_keys(search_item + Keys.ENTER)


def youtube_search(search_item):
    url = f"https://www.youtube.com/results?search_query={search_item}"

    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach",True)

    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    driver.get(url)


def amazon_search(search_item):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach",True)

    driver = webdriver.Chrome(options=option)
    driver.maximize_window()

    driver.get("https://www.amazon.in/")

    ask = input("does it asks code:").lower()
    
    if ask == "yes":
        otp = input("does it asks otp:").upper()
        yo = driver.find_element(By.ID,"captchacharacters")
        yo.send_keys(otp + Keys.ENTER)

        my_element = driver.find_element(By.ID,"twotabsearchtextbox")
        my_element.clear()
        my_element.send_keys(search_item + Keys.ENTER)

    else:
        my_element = driver.find_element(By.ID,"twotabsearchtextbox")
        my_element.clear()
        my_element.send_keys(search_item + Keys.ENTER)





