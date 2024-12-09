import os
import eel

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from playsound import playsound

from engine.config import *
from engine.command import *



#playing assistant sound
def playAssistantSound():
    music_dir = r"www\\assets\\sound.mp3"
    playsound(music_dir)

#playing mic sound
@eel.expose
def playMicSound():
    music_dir = r"www\\assets\\mic_sound.mp3"
    playsound(music_dir)


def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    if query !="":
        speak("opening"+ query)
        os.system('start'+ query)
    else:
        speak("not found")


#search-engine class
class browser_engine():
    def open_google():
        try:
            option = webdriver.ChromeOptions()
            option.add_experimental_option("detach",True)

            driver = webdriver.Chrome(options=option)
            driver.maximize_window()

            driver.get("https://www.google.com")
        except:
            speak("SOMETHING WENT WRONG!, TRY AGAIN")
            
    def google_search(search_item):
        try:
            option = webdriver.ChromeOptions()
            option.add_experimental_option("detach",True)

            driver = webdriver.Chrome(options=option)
            driver.maximize_window()

            driver.get("https://www.google.com")
            my_element = driver.find_element(By.ID,"APjFqb")
            my_element.send_keys(search_item + Keys.ENTER)
        except:
            speak("SOMETHING WENT WRONG!, TRY AGAIN")
